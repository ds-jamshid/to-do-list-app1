from django.urls import path
from .views import home_page, create_post, delete_task,edit_task
urlpatterns = [
    path("",home_page, name="home"),
    path("create/",create_post, name="create"),
    path('delete/<int:id>/',delete_task, name="delete"),
    path('edit/<int:id>/',edit_task,name='edit')

]

