from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Event
from app.serializers import EventSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html')

class EventList(APIView):
    def get(self, request):
        Event1 = Event.objects.all()
        serializer = EventSerializer(Event1, many=True)
        return Response(serializer.data)
    def post(self):
        pass

class EventDetail(APIView):
    def get(self, request, pk):
        Event1 = Event.objects.get(id=pk)
        serializer = EventSerializer(Event1, many=False)
        return Response(serializer.data)
    def post(self):
        pass

class EventCreate(APIView):
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class EventUpdate(APIView):
    def post(self, request, pk):
        Event1 = Event.objects.get(id=pk)
        serializer = EventSerializer(instance=Event1, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class EventDelete(APIView):
    def delete(self, request, pk):
        Event1 = Event.objects.get(id=pk)
        Event1.delete()
        return Response('Event Successfully Deleted')