from django import forms

from apps.billing.models import Saskaita
from apps.main.forms import CarbonFormMixin, DateInput


class SaskaitaForm(CarbonFormMixin, forms.ModelForm):
    class Meta:
        model = Saskaita
        exclude = ("apmokejimo_data",)
        widgets = {
            "israsymo_data": DateInput(),
            "apmokejimo_terminas": DateInput(),
        }
