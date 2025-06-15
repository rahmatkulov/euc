from django.db import models
from django.db.models.deletion import SET_NULL, CASCADE
from django.utils.translation import gettext_lazy as _
from django.utils import timezone 

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
    last_name = models.CharField("last name", max_length=256, null=True)
    birth_date = models.DateField("birth date")
    phone_or_email = models.CharField("phone or email", max_length=256)
    address = models.CharField("address", max_length=256)

    class Meta:
        db_table = "teachers"
        verbose_name = "teacher"
        verbose_name_plural = "teacher"

    def __str__(self):
        return f"{self.name}"


class Group(models.Model):
    day_choices = [
        ("Du Chor Ju", "Du Chor Ju"),
        ("Se Pay Shan", "Se Pay Shan"),
    ]
    group_name = models.CharField("group name", max_length=256)
    category = models.ForeignKey(
        GroupCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="category",
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=SET_NULL,
        related_name="teacher",
        null=True,
    )
    days = models.CharField("days", choices=day_choices)
    slug = models.SlugField('slug', unique=True, max_length=256)
    time = models.TimeField("time")
    date_started = models.DateField("date started", null=True)
    duration_months = models.PositiveIntegerField('duration months',default=12)

    class Meta:
        db_table = "groups"
        verbose_name = "group"
        verbose_name_plural = "group"

    @property
    def progress_percentage(self):
        today = timezone.now().date()
        total_days = self.duration_months * 30
        passed_days = (today - self.date_started).days

        if passed_days <= 0:
            return 0
        elif passed_days >= total_days:
            return 100
        else:
            return round((passed_days / total_days) * 100)

    def __str__(self):
        return f"{self.group_name}"


class Student(models.Model):
    name = models.CharField("name", max_length=256)
    last_name = models.CharField("last name", max_length=256, null=True, blank=True)
    birth_date = models.DateField("birth date")
    joined = models.DateField("joined", auto_now=True)
    group = models.ForeignKey(
        Group, on_delete=SET_NULL, related_name="students", null=True
    )
    address = models.CharField("address", max_length=256)
    monthly_payment = models.IntegerField("monthly payment")
    phone_number_or_email = models.CharField("phone or email", max_length=256)
    balance = models.IntegerField("balance", null=True, blank=True)

    class Meta:
        db_table = "students"
        verbose_name = "student"
        verbose_name_plural = "students"

    def __str__(self):
        return f"{self.name}"

class Payment(models.Model):
    student = models.ForeignKey(
        Student,
        null=True,
        blank=False,
        on_delete=CASCADE,
        related_name='payments'  # исправили тут
    )
    amount = models.PositiveIntegerField("amount")
    date = models.DateField("date")

    class Meta:
        db_table = "payments"
        verbose_name = "payment"
        verbose_name_plural = "payments"

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.student.balance is None:
                self.student.balance = 0
            self.student.balance += self.amount
            self.student.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.pk:
            self.student.balance -= self.amount
            self.student.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.student}"
