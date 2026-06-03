from django import template

register = template.Library()

@register.simple_tag
def priority_class(level):

    mapping = {
        "CRITICAL": "danger",
        "HIGH": "warning",
        "MEDIUM": "info",
        "LOW": "success",
    }

    return mapping.get(level, "secondary")