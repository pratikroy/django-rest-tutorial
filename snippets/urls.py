from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/',
        views.SnippetList.as_view(),
        name='snippets'),
    path('snippets/<int:pk>/',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
