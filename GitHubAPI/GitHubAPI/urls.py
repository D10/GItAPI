from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('git_api.urls'))
]


def response_404(request, status=200, message='Not Found', data=None):
    message = {'message': message}
    return JsonResponse(message)


handler404 = response_404
handler500 = response_404
