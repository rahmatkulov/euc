from django import forms
from common import models
from helpers import widgets


class GroupCategoryForm(forms.ModelForm):
    class Meta:
        model = models.GroupCategory
        fields = [
            "title",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Enter category title",
                    "class": "form-control",
                }
            ),
        }

class GroupForm(forms.ModelForm):
    class Meta:
        model = models.Group 
        fields = [
            'group_number',
            'category',
            'teacher'
        ]
        widgets = {
            'group_number': forms.NumberInput(attrs={"placeholder" : "Enter a group number", "min" : "1",}),
            'category': forms.Select(attrs={"placeholder" : "Select a group category", }),
            'teacher' : forms.Select(attrs={"placeholder" : "Select a teacher"}),
         }
