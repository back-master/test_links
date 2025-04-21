from django import forms

from apps.shorter.models import Link


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ["url"]
        widgets = {
            "url": forms.URLInput(
                attrs={"placeholder": "Вставь свою ссылку", "style": "width:300px"}
            ),
        }
