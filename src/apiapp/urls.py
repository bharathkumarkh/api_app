"""apiapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from accounts.views import login_view, logout_view, profile_view, register_view
from api.views import (
    APIView,
    Approval,
    ApprovedList,
    CreateApp,
    DetailApproval,
    PendingList,
    UpdateApproval,
    UploadImage,
)
from applications.views import (
    add_apps_view,
    approvals,
    detail_app_view,
    points,
    tasks,
    tasks_view,
    update,
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import home

urlpatterns = [
    path("", home, name="home"),
    path("apps/add/", add_apps_view, name="add"),
    path("apps/<int:id>/", detail_app_view, name="detail"),
    path("tasks/", tasks_view, name="tasks_list"),
    path("tasks/<int:id>/", update, name="update"),
    path("approvals/", approvals, name="approvals"),
    path("points/", points, name="points"),
    path("apps/<int:parent_id>/tasks/", tasks, name="tasks"),
    path("admin/", admin.site.urls),
    path("accounts/login/", login_view, name="login"),
    path("accounts/logout/", logout_view, name="logout"),
    path("accounts/register/", register_view, name="register"),
    path("accounts/profile/", profile_view, name="profile"),
    path("api/", APIView.as_view()),
    path("api/pending-list/", PendingList.as_view()),
    path("api/approved-list/", ApprovedList.as_view()),
    path("api/approval/", Approval.as_view()),
    path("api/approval/<int:pk>/", DetailApproval.as_view()),
    path("api/approval/<int:pk>/approve/", UpdateApproval.as_view()),
    path("api/create-app/", CreateApp.as_view()),
    path("api/create-task/", UploadImage.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
