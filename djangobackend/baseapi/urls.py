from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


app_name = 'api'

urlpatterns = [
    path(
        'react-paths/',
        views.build_react_pathes_view,
        name='react-paths',
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
