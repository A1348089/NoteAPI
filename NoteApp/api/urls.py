from django.urls import path

from NoteApp.views import NoteCreateAPIView, NoteDetailsAPIView

urlpatterns = [
    path('', NoteCreateAPIView.as_view(), name='Note-create-list'),
    path('<int:pk>/', NoteDetailsAPIView.as_view(), name='Note-details'),
]
