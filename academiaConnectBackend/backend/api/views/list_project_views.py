from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from api.models import Project

@api_view(['GET'])
@permission_classes([AllowAny])
def list_projects(request):
    projects = Project.objects.select_related('created_by').order_by('-created_at')

    paginator = PageNumberPagination()
    paginator.page_size = 3  # 👈 Custom pagination size
    result_page = paginator.paginate_queryset(projects, request)

    data = []
    for project in result_page:
        data.append({
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'created_by': project.created_by.full_name,
            'created_at': project.created_at,
        })

    return paginator.get_paginated_response(data)
