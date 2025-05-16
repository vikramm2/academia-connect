from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from api.models import Post

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    text = request.data.get('text')

    if not text:
        return Response({'error': 'Text is required'}, status=status.HTTP_400_BAD_REQUEST)

    user = request.user
    post = Post.objects.create(author=user, text=text, role=user.role)

    return Response({
        'message': 'Post created successfully',
        'post': {
            'id': post.id,
            'text': post.text,
            'author': user.email,
            'role': post.role,
            'created_at': post.created_at
        }
    }, status=201)