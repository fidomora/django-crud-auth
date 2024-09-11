from django.urls import path
from tasks.views import home,  signup, tasks, signout, signin, create_task, task_detail, complete_task, delete_task, tasks_completed

urlpatterns = [
    path(route='', view=home, name='home'),
    path(route='signup/', view=signup, name='signup'),
    path(route='logout/', view=signout, name='logout'),
    path(route='signin/', view=signin, name='signin'),    
    path(route='tasks/', view=tasks, name='tasks'),
    path(route='tasks/completed/', view=tasks_completed, name='tasks_completed'),
    path(route='tasks/create/', view=create_task, name='create_task'),
    path(route='tasks/<int:task_id>/', view=task_detail, name='task_detail'),
    path(route='tasks/<int:task_id>/complete', view=complete_task, name='complete_task'),
    path(route='tasks/<int:task_id>/delete', view=delete_task, name='delete_task'),
]
