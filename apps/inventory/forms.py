from django import forms

from apps.inventory.models import Dalis
from apps.main.forms import CarbonFormMixin


class DalisForm(CarbonFormMixin, forms.ModelForm):
    class Meta:
        model = Dalis
        exclude = ("prognozuojamas_poreikis",)


class LikutisForm(CarbonFormMixin, forms.ModelForm):
    """Mechanics may only adjust the stock level."""

    class Meta:
        model = Dalis
        fields = ("likutis",)
