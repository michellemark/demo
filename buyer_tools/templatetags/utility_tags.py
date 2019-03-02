from django import template

register = template.Library()


@register.filter(is_safe=True)
def money(value):

    try:
        value = int(value)
    except ValueError:
        pass
    else:
        value = f"${value:,}"

    return value
