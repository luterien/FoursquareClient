from django import forms

from .models import Search


class SearchForm(forms.ModelForm):

    class Meta:
        model = Search
        fields = ["query", "location",]
        widgets = {
            "query": forms.TextInput(attrs={"placeholder": "I'm looking for..."}),
            "location": forms.TextInput(attrs={"placeholder": "Location"})
        }

