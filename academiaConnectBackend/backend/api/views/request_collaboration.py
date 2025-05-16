from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from api.models import Project, CollaborationRequest

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def request_collaboration(request, project_id):
    user = request.user

    if user.role != 'Student':
        return Response({'error': 'Only students can request to collaborate'}, status=403)

    if CollaborationRequest.objects.filter(student=user, status='approved').exists():
        return Response({'error': 'You are already part of another project.'}, status=400)

    if CollaborationRequest.objects.filter(student=user, project_id=project_id).exists():
        return Response({'error': 'You have already requested to join this project.'}, status=400)

    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return Response({'error': 'Project not found'}, status=404)

    collab = CollaborationRequest.objects.create(student=user, project=project)

    return Response({
        'message': 'Request submitted successfully',
        'request': {
            'id': collab.id,
            'status': collab.status,
            'project': project.title
        }
    }, status=201)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def approve_collaboration(request, request_id):
    user = request.user

    if user.role != 'Professor':
        return Response({'error': 'Only professors can approve requests'}, status=403)

    try:
        collab = CollaborationRequest.objects.select_related('project', 'student').get(id=request_id)
    except CollaborationRequest.DoesNotExist:
        return Response({'error': 'Collaboration request not found'}, status=404)

    if collab.project.created_by != user:
        return Response({'error': 'You are not authorized to approve this request'}, status=403)

    if collab.status != 'pending':
        return Response({'error': f'Request is already {collab.status}'}, status=400)

    # Check if student is already in a project
    already_in_project = CollaborationRequest.objects.filter(
        student=collab.student,
        status='approved'
    ).exists()
    if already_in_project:
        return Response({'error': 'Student is already in a project'}, status=400)

    collab.status = 'approved'
    collab.save()

    return Response({
        'message': 'Collaboration request approved',
        'student': collab.student.full_name,
        'project': collab.project.title
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_project_requests(request, project_id):
    user = request.user

    if user.role != 'Professor':
        return Response({'error': 'Only professors can view collaboration requests'}, status=403)

    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return Response({'error': 'Project not found'}, status=404)

    if project.created_by != user:
        return Response({'error': 'You are not authorized to view this project\'s requests'}, status=403)

    requests = CollaborationRequest.objects.filter(project=project).select_related('student')
    result = []

    for r in requests:
        result.append({
            'id': r.id,
            'student_name': r.student.full_name,
            'student_email': r.student.email,
            'status': r.status,
            'requested_at': r.requested_at,
        })

    return Response(result)    