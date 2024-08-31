from django.shortcuts import render

from rest_framework import generics

from NoteApp.api.serializers import NoteSerializer
from NoteApp.models import Note
# Create your views here.

class NoteCreateAPIView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    
    def get_queryset(self):

        queryset = Note.objects.all()
        title = self.request.query_params.get('title', None)
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

class NoteDetailsAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        return Note.objects.filter(id = pk)
    
