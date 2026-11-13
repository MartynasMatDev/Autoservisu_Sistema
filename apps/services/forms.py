from django import forms

from apps.main.forms import CarbonFormMixin
from apps.services.models import Paslauga


class PaslaugaForm(CarbonFormMixin, forms.ModelForm):
    class Meta:
        model = Paslauga
        fields = "__all__"
        widgets = {"aprasymas": forms.Textarea(attrs={"rows": 4})}
