from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter()
def currency(dollars):
    if (dollars == ''):
        dollars = 0

    dollars = round(float(dollars), 2)
    return "$%s%s" % (intcomma(int(dollars)), ("%0.2f" % dollars)[-3:])
