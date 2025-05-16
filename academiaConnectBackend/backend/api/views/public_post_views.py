from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from api.models import Post

@api_view(['GET'])
@permission_classes([AllowAny])
def list_posts(request):
    posts = Post.objects.select_related('author', 'project').order_by('-created_at')

    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(posts, request)

    data = []
    for post in result_page:
        data.append({
            'id': post.id,
            'text': post.text,
            'author': post.author.full_name,
            'email': post.author.email,
            'role': post.role,
            'project': post.project.title if post.project else None,
            'project_id': post.project.id if post.project else None,
            'created_at': post.created_at,
        })

    return paginator.get_paginated_response(data)
