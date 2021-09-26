from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import GitApiViewSet

repo_details = GitApiViewSet.as_view({
    'get': 'get_repo_details'
})

urlpatterns = format_suffix_patterns([
    path('repo_details/<str:account>/<str:repo>', repo_details),
    path('repo_details/<str:account>/<str:repo>/<str:param>', repo_details),
])
