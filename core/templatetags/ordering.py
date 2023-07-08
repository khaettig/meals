from django import template
from django.utils.html import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def hx_ordering(context, name):
    prefix = "-" if context["ordering"] == name else ""
    return f"hx-get=?ordering={prefix}{name}"


@register.simple_tag(takes_context=True)
def ordering_icon(context, name):
    if context["ordering"].replace("-", "") != name:
        return ""
    if context["ordering"].startswith("-"):
        return mark_safe(' <i class="fa-solid fa-caret-up"></i>')
    return mark_safe(' <i class="fa-solid fa-caret-down"></i>')
