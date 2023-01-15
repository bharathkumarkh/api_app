from applications.models import App, Tasks
from applications.serializers import AppSerializers, TasksSerializer, UploadSerializer
from django.shortcuts import get_object_or_404
from rest_framework import authentication, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


class APIView(generics.ListAPIView):
    serializer_class = TasksSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Tasks.objects.filter(user=user)


class PendingList(generics.ListAPIView):
    serializer_class = TasksSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Tasks.objects.filter(user=user, status="PENDING")


class ApprovedList(generics.ListAPIView):
    serializer_class = TasksSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Tasks.objects.filter(user=user, status="APPROVED")


class Approval(generics.ListAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]


class DetailApproval(generics.ListAPIView):
    serializer_class = TasksSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Tasks.objects.filter(pk=pk)


class UpdateApproval(generics.UpdateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def perform_update(self, serializer):
        instance = serializer.save()


class CreateApp(generics.ListCreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializers
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()


class UploadImage(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = UploadSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
