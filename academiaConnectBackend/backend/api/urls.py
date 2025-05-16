from django.urls import path
from api.views.project_views import create_project
from api.views.request_collaboration import request_collaboration
from api.views.request_collaboration import approve_collaboration
from api.views.post_views import create_post
from api.views.public_post_views import list_posts
from api.views.list_project_views import list_projects
from api.views.auth_views import signup, login_view
from api.views.request_collaboration import get_project_requests

urlpatterns = [
    path('signup/', signup, name='signup'),
     path('login/', login_view, name='login'),
     path('posts/', create_post),
    path('projects/', create_project),
    path('projects/<int:project_id>/request/', request_collaboration),
    path('requests/<int:request_id>/approve/', approve_collaboration),
    path('projects/<int:project_id>/requests/', get_project_requests),
    path('listposts/', list_posts),
    path('list_projects/', list_projects),
]
