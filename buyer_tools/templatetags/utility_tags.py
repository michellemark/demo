from django import template

register = template.Library()


@register.filter(is_safe=True)
def money(value):

    try:
        value = int(value)
    except ValueError:
        if isinstance(value, str):
            value = f"${value}"
    else:
        value = f"${value:,}"

    return value
