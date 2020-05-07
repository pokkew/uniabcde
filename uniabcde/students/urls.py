from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path(
        route='',
        view=views.StudentListView.as_view(),
        name='list'
    ),
    path(
        route='add/',
        view=views.StudentCreateView.as_view(),
        name='add'
    ),
    path(
        route='<slug:slug>',
        view=views.StudentDetailView.as_view(),
        name='detail'
    ),
]