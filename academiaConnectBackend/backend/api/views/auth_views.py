from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from api.models import User

@csrf_exempt
def signup(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST method required'}, status=400)

    data = json.loads(request.body)

    full_name = data.get('fullName')
    email = data.get('email')
    role = data.get('role')
    password = data.get('password')
    confirm_password = data.get('confirmPassword')

    if not all([full_name, email, role, password, confirm_password]):
        return JsonResponse({'error': 'All fields are required'}, status=400)

    if password != confirm_password:
        return JsonResponse({'error': 'Passwords do not match'}, status=400)

    if role not in ['Professor', 'Student']:
        return JsonResponse({'error': 'Invalid role'}, status=400)

    if User.objects.filter(email=email).exists():
        return JsonResponse({'error': 'Email already registered'}, status=400)

    user = User.objects.create_user(email=email, full_name=full_name, role=role, password=password)
    return JsonResponse({'message': 'User created successfully'})

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import User

@api_view(['POST'])
def login_view(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get(email=email)
        if not user.check_password(password):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)

        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': {
                'id': user.id,
                'email': user.email,
                'role': user.role,
                'full_name': user.full_name
            }
        })

    except Exception as e:
        return Response({'error': str(e)}, status=500)