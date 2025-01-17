from django import template

register = template.Library()

@register.filter
def range_filter(value):
    """Generates a range based on the value."""
    try:
        value = int(value)  # Ensure the value is an integer
    except (ValueError, TypeError):
        value = 0  # Default to 0 if the value is None or cannot be converted to an int
    return range(1, value + 1) if value > 0 else range(0)
