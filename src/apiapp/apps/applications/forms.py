from django import forms

from .models import App, Tasks


class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ["app_name", "app_url", "app_points"]

    def clean(self):
        data = self.cleaned_data
        app_name = data.get("app_name")
        app_url = data.get("app_url")
        qs = App.objects.filter(app_name__contains=app_name)
        qs1 = App.objects.filter(app_url__contains=app_url)
        if qs.exists():
            self.add_error(
                "app_name",
                f'"{app_name}" is already in use. Please pick another app.',
            )
        if qs1.exists():
            self.add_error(
                "app_url",
                f'"{app_url}" is already in use. Please pick another url.',
            )
        return data


class ApprovalForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["status"]
