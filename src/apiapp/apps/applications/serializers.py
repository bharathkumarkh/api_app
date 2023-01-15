from rest_framework import serializers

from .models import App, Tasks


class AppSerializers(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = "__all__"
        read_only_fields = [
            "id",
            "app_category",
            "app_rating",
            "app_description",
            "app_image_url",
        ]


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = [
            "id",
            "status",
            "user",
            "user_name",
            "image",
            "app",
            "application_id",
            "application_name",
            "application_category",
            "application_rating",
            "application_description",
            "application_points",
        ]
        read_only_fields = [
            "id",
            "user",
            "user_name",
            "image",
            "app",
            "application_id",
            "application_name",
            "application_category",
            "application_rating",
            "application_description",
            "application_points",
        ]


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = [
            "id",
            "status",
            "user",
            "user_name",
            "image",
            "app",
            "application_id",
            "application_name",
            "application_category",
            "application_rating",
            "application_description",
            "application_points",
        ]
        read_only_fields = [
            "id",
            "status",
            "user",
            "application_category",
            "application_rating",
            "application_description",
            "application_points",
        ]
