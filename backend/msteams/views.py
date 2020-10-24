from django.shortcuts import render
from rest_framework import viewsets
from msteams.models import Msteams
from msteams.serializers import MsteamsSerializer
from rest_framework.response import Response
from rest_framework import status
from subprocess import run,PIPE
import sys
# Create your views here.

class MsteamsView(viewsets.ModelViewSet):
    serializer_class = MsteamsSerializer
    queryset = Msteams.objects.all()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print(serializer.data)
        output = run([sys.executable,"/home/ark/Downloads/reactSchedule/scheduler/src/scheduler.py",
        str(serializer.data['id']),
        request.data['email'],
        request.data['password'],
        request.data['subject'],
        request.data['prof'],
        request.data['time'],
        request.data['days']],shell=False,stdout=PIPE)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        req = str(request)
        start = len(req) - 5
        end = len(req) - 3
        print(req[start:end])
        run([sys.executable,"/home/ark/Downloads/reactSchedule/scheduler/src/scheduler.py",
        str(req[start:end])],shell=False,stdout=PIPE)
        return Response(status=status.HTTP_204_NO_CONTENT)