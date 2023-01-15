from django.contrib.auth.decorators import login_required, permission_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AppForm, ApprovalForm
from .models import App, Tasks

# Create your views here.


def check_admin(user):
    return user.is_superuser


@login_required
def detail_app_view(request, id=None):
    parent_obj = None
    if id is not None:
        # app_obj = App.objects.get(id=id)
        parent_obj = App.objects.get(id=id)
        try:
            tasks_obj = Tasks.objects.get(app_id=id, user=request.user)
        except:
            tasks_obj = None
    context = {
        "object": parent_obj,
        "tasks_obj": tasks_obj,
    }
    return render(request, "apps/detail.html", context=context)


@login_required
@permission_required("App.add_apps")
def add_apps_view(request):
    form = AppForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        app_object = form.save()
        context["form"] = AppForm()
        return redirect(app_object.get_absolute_url())

    return render(request, "apps/create.html", context=context)


@login_required
def tasks(request, parent_id=None):
    my_file = None
    template_name = "apps/upload-image.html"
    try:
        parent_obj = App.objects.get(id=parent_id)
    except:
        parent_obj = None
    if parent_obj is None:
        raise Http404
    my_file = request.FILES.get("file")
    if request.method == "POST":
        Tasks.objects.create(user=request.user, app=parent_obj, image=my_file)
    return render(request, template_name)


@login_required
def tasks_view(request, *args, **kwargs):
    task_list = Tasks.objects.filter(user=request.user)
    if task_list.exists():
        context = {
            "object_list": task_list,
        }
        return render(request, "apps/tasks-view.html", context=context)
    return render(request, "apps/notasks.html")


@login_required
def points(request, *args, **kwargs):
    task_list = Tasks.objects.filter(user=request.user, status="APPROVED")
    sum = 0
    for x in task_list:
        sum = sum + x.app.app_points
    context = {
        "object_list": task_list,
        "sum": sum,
    }
    return render(request, "apps/points.html", context=context)


@login_required
@permission_required("App.add_apps")
def approvals(request, *args, **kwargs):
    task_list = Tasks.objects.filter(status="PENDING")
    context = {
        "object_list": task_list,
    }
    return render(request, "apps/approvals.html", context=context)


@login_required
@permission_required("App.add_apps")
def update(request, id):
    task = Tasks.objects.get(id=id)
    if request.method == "POST":
        form = ApprovalForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            print("dei")
            return redirect("/approvals/")
    else:
        form = ApprovalForm(instance=task)
    return render(
        request,
        "apps/update-status.html",
        {"form": form, "object": task},
    )

    # if form.is_valid():
    #     print(form.is_valid())
    #     obj = form.save(commit=False)
    #     obj.user = request.user
    #     print(obj.user)
    #     obj.app = parent_obj
    #     print(obj.app)
    #     obj.save()
    # return render(request,template_name,{})
