from django.urls import path
from . import views

app_name = "teachers"

urlpatterns = [
    path(
        route='',
        view=views.TeacherListView.as_view(),
        name='list'
    ),
    path(
        route='add/',
        view=views.TeacherCreateView.as_view(),
        name='add'
    ),
    path(
        route='<slug:slug>',
        view=views.TeacherDetailView.as_view(),
        name='detail'
    ),
]