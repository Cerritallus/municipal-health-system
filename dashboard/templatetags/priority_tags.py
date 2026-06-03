from django import template

register = template.Library()

@register.simple_tag
def priority_class(level):

    if level == "CRITICAL":
        return "table-danger"

    if level == "HIGH":
        return "table-warning"

    if level == "MEDIUM":
        return "table-info"

    return ""