from django.urls import path
from todolist.views import get_json_data, login_user
from todolist.views import register
from todolist.views import logout_user
from todolist.views import show_todolist
from todolist.views import create_task
from todolist.views import get_json_data
from todolist.views import add_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('json/', get_json_data, name='get_json_data'),
    path('add/', add_task, name='add_task'),
]