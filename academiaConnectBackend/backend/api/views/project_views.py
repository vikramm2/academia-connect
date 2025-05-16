from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from api.models import Project
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_project(request):
    if request.user.role != 'Professor':
        return Response({'error': 'Only professors can create projects'}, status=status.HTTP_403_FORBIDDEN)

    title = request.data.get('title')
    description = request.data.get('description')

    if not title or not description:
        return Response({'error': 'Title and description are required'}, status=status.HTTP_400_BAD_REQUEST)

    project = Project.objects.create(
        title=title,
        description=description,
        created_by=request.user
    )

    return Response({
        'message': 'Project created successfully',
        'project': {
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'created_by': request.user.email,
            'created_at': project.created_at
        }
    }, status=201)
