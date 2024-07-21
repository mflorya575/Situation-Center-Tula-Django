from django import forms

from .models import REGION_CHOICES


class RegionForm(forms.Form):
    region = forms.ChoiceField(
        choices=REGION_CHOICES,
        label='Выберите регион',
        required=True,
    )
