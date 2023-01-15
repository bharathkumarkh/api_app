import pathlib
import uuid

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse

from .utils import update_app_data

# Create your models here.
choices = (
    (50, 50),
    (100, 100),
    (150, 150),
    (200, 200),
    (250, 250),
    (300, 300),
    (350, 350),
    (400, 400),
    (450, 450),
    (500, 500),
)
choices1 = (
    ("PENDING", "pending"),
    ("APPROVED", "Approved"),
)


class App(models.Model):
    id = models.BigAutoField(primary_key=True)
    app_name = models.CharField(max_length=220)
    app_url = models.CharField(max_length=220)
    app_category = models.CharField(max_length=220, blank=True, null=True)
    app_rating = models.FloatField(blank=True, null=True, default=0.00)
    app_description = models.TextField(blank=True, null=True)
    app_image_url = models.TextField(blank=True, null=True)
    app_points = models.IntegerField(choices=choices, default=50)

    class Meta:
        managed = True
        db_table = "app"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


def apps_post_save(sender, instance, created, *args, **kwargs):
    # print('post_save')
    if created:
        update_app_data(instance)


post_save.connect(apps_post_save, sender=App)


def image_upload_handler(instance, filename):
    fpath = pathlib.Path(filename)
    new_fname = str(uuid.uuid1())  # uuid1 >> uuid + Timestamp
    return f"apps/tasks/{new_fname}{fpath.suffix}"


class Tasks(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    app = models.ForeignKey(
        App,
        related_name="app_task",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to=image_upload_handler)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=8,
        choices=choices1,
        default="PENDING",
    )

    class Meta:
        managed = True
        db_table = "tasks"

    @property
    def user_name(self):
        return self.user.username

    @property
    def application_id(self):
        return self.app.id

    @property
    def application_name(self):
        return self.app.app_name

    @property
    def application_category(self):
        return self.app.app_category

    @property
    def application_rating(self):
        return self.app.app_rating

    @property
    def application_description(self):
        return self.app.app_description

    @property
    def application_points(self):
        return self.app.app_points
