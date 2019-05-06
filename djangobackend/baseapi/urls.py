from django.urls import path

from . import views


app_name = 'api'

urlpatterns = [
    path(
        'react-paths/',
        views.build_react_pathes_view,
        name='react-paths',
    ),
]
