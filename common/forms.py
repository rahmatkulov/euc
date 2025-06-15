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
            'group_name',
            'category',
            'teacher',
            'days',
            'time',
            'date_started',
            'duration_months',
        ]
        widgets = {
            'group_name': forms.TextInput(attrs={'class' : 'form-control',"placeholder" : "Enter a group name",}),
            'category': forms.Select(attrs={'class' : 'form-control',"placeholder" : "Select a group category", }),
            'teacher' : forms.Select(attrs={'class' : 'form-control',"placeholder" : "Select a teacher"}),
            'days' : forms.Select(attrs={'class' : 'form-control',"placeholder" : "Select days "}),
            'time' : forms.TimeInput(attrs={'class' : 'form-control',"placeholder" : "Select days "}),
            'date_started' : forms.DateInput(attrs={'class' : 'form-control', }),
            'duration_months' : forms.NumberInput(attrs={'class' : 'form-control',"placeholder" : "Select days "})
         }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = [
            "name",
            "last_name",
            "birth_date",
            'address',
            'phone_or_email'
        ]
        widgets = {
            "name" : forms.TextInput(attrs={"class" : "form-control"}),
            "last_name" : forms.TextInput(attrs={"class" : "form-control"}),
            "birth_date" : forms.DateInput(attrs={"class" : "form-control"}),
            'address' : forms.TextInput(attrs={"class" : "form-control"}),
            'phone_or_email' : forms.TextInput(attrs={"class" : "form-control"}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = [
            'name',
            'last_name',
            'birth_date',
            'group',
            'address',
            'monthly_payment',
            'phone_number_or_email',
            'balance',
        ]
        widgets={
            "name" : forms.TextInput(attrs={"class" : "form-control"}),
            "last_name" : forms.TextInput(attrs={"class" : "form-control"}),
            "birth_date" : forms.DateInput(attrs={"class" : "form-control"}),
            'group' : forms.Select(attrs={"class" : "form-control"}),
            'address' : forms.TextInput(attrs={"class" : "form-control"}),
            'monthly_payment' : forms.NumberInput(attrs={"class" : "form-control", "min" : "1"}),
            'phone_number_or_email' : forms.TextInput(attrs={"class" : "form-control"}),
            'balance' : forms.NumberInput(attrs={"class" : "form-control"}),
        }


        
class PaymentForm(forms.ModelForm):
    class Meta:
        model = models.Payment
        fields = [
            "student",
            "amount",
            "date",
        ]
        widgets = {
            "student" : forms.Select(attrs={"class" : "form-control"}),
            "amount" : forms.NumberInput(attrs={"class" : "form-control", "min" : "1"}),
            "date" : forms.DateInput(attrs={"class" : "form-control"}),
        }
