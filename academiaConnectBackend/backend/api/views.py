# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from .models import User

# @csrf_exempt
# def signup(request):
#     if request.method != 'POST':
#         return JsonResponse({'error': 'POST method required'}, status=400)

#     data = json.loads(request.body)

#     full_name = data.get('fullName')
#     email = data.get('email')
#     role = data.get('role')
#     password = data.get('password')
#     confirm_password = data.get('confirmPassword')

#     if not all([full_name, email, role, password, confirm_password]):
#         return JsonResponse({'error': 'All fields are required'}, status=400)

#     if password != confirm_password:
#         return JsonResponse({'error': 'Passwords do not match'}, status=400)

#     if role not in ['Professor', 'Student']:
#         return JsonResponse({'error': 'Invalid role'}, status=400)

#     if User.objects.filter(email=email).exists():
#         return JsonResponse({'error': 'Email already registered'}, status=400)

#     user = User.objects.create_user(email=email, full_name=full_name, role=role, password=password)
#     return JsonResponse({'message': 'User created successfully'})
