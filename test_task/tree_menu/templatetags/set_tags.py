from django import template


register = template.Library()


@register.simple_tag()
def start_with(request, val):
    return request.path.startswith(val)
