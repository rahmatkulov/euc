from django.db import models
from django.db.models.deletion import SET_NULL, CASCADE 
from django.utils.translation import gettext_lazy as _


class GroupCategory(models.Model):
    title = models.CharField(_("title"), max_length=256)

    class Meta:
        db_table = "group categories"
        verbose_name = "group category"
        verbose_name_plural = "group categories"

    def __str__(self):
        return f"{self.title}"


class Teacher(models.Model):
    name = models.CharField("name", max_length=256)
    age = models.PositiveIntegerField("age")
    birth_date = models.DateField("birth_date")
    address = models.CharField("address",max_length=256)
    
    class Meta:
        db_table = "teachers"
        verbose_name = "teacher"
        verbose_name_plural = "teacher"

    def __str__(self):
        return f"{self.name}"


class Group(models.Model):
    group_number = models.PositiveIntegerField("group_number")
    category = models.ForeignKey(
        GroupCategory, null=True, on_delete=SET_NULL, related_name="group_category"
    )
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=SET_NULL, related_name="teacher")

    class Meta:
        db_table = "groups"
        verbose_name = "group"
        verbose_name_plural = "groups"

    def __str__(self):
        return f"{self.group_number}"


class Student(models.Model):
    name = models.CharField("name", max_length=256)
    age = models.PositiveIntegerField("age")
    birth_date = models.DateField("birth_date")
    address = models.CharField("address",max_length=256)
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=SET_NULL)
    monthly_payment = models.IntegerField("monthly_payment") 
    phone_number_or_email = models.CharField("phone_or_email", max_length=256)
    debt = models.IntegerField("debt")     

    class Meta:
        db_table = "students"
        verbose_name = "student"
        verbose_name_plural = "students"

    def __str__(self):
        return f"{self.name}"
