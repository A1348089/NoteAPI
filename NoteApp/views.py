from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
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
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            "message": "Note created successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)
    

class NoteDetailsAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        return Note.objects.filter(id = pk)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({
            "message": "Note updated successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
