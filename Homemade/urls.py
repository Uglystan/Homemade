"""
URL configuration for Homemade project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers
import authentication.views as authentication
import home.views as home
import task.views as task
import schedule.views as schedule
import game.views as game
from api.views import TaskViewset, UserViewset, AdminTaskViewset, EventViewset, EventParticipationViewset
from Homemade.settings import MEDIA_URL, MEDIA_ROOT
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()
router.register('task', TaskViewset, basename='task')
router.register('user', UserViewset, basename='user')
router.register('event', EventViewset, basename='event')
router.register('event_participation', EventParticipationViewset, basename='event_participation')
router.register('admin/task', AdminTaskViewset, basename='admin-task')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', authentication.login_page, name='login'),
    path('home/', home.home, name='home'),
    path('logout/', authentication.logout_view, name='logout'),
    path('register/', authentication.register, name='register'),
    path('edit_profil/', authentication.edit_profil, name='edit-profil'),
    path('task/', task.TaskView.as_view(), name='task'),
    path('task/create/', task.task_create, name='task-create'),
    path('task/<int:id>/', task.task_detail, name='task-detail'),
    path('task/<int:id>/edit/', task.task_edit, name='task-edit'),
    path('task/<int:id>/done/', task.task_done, name='task-done'),
    path('task/<int:id>/delete/', task.task_delete, name='task-delete'),
    path('schedule/', schedule.schedule, name='schedule'),
    path('schedule/event/create/', schedule.event_create, name='event-create'),
    path('schedule/event/<int:id>/', schedule.event_detail, name='event-detail'),
    path('schedule/<int:id>/participate/', schedule.event_participate, name='event-participate'),
    path('schedule/<int:id>/delete/', schedule.event_delete, name='event-delete'),
    path('schedule/<int:id>/edit', schedule.event_edit, name="event-edit"),
    path('game/', game.game, name='game'),
    path('game/rank', game.game_rank, name='game-rank'),
]

urlpatterns += static(
	MEDIA_URL, document_root=MEDIA_ROOT
)


# "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNjY0NTExNSwiaWF0IjoxNzE2NTU4NzE1LCJqdGkiOiJlM2VlZTM3MjE4ZWY0MGM3YTA3NDNlYWUwNzEyYTkzNSIsInVzZXJfaWQiOjJ9.HbVI_D8JvTA_LbMZ_keyJ4zEZFEtHzdSKQ-xYSYQylc",
# "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2NTU5MjQwLCJpYXQiOjE3MTY1NTg3MTUsImp0aSI6ImNhODEwNTU0NDQ5YTQxNTBiMGQyZTA2NzQwOWNkMjhkIiwidXNlcl9pZCI6Mn0.D50jMbCw6AQlpixK0GLq4NVbwT1cOG2jvFmtzqcaD08"