from django.forms import widgets


class DateWidget(widgets.DateInput):
    template_name = 'widgets/date.html'
