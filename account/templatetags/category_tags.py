# templatetags/category_tags.py
from django import template
from home.models import Category

register = template.Library()

@register.filter
def tree_display(categories):
    output = '<ul>'
    for category in categories:
        output += f'<li>{category.title}'
        if category.children.exists():
            output += tree_display(category.children.all())
        output += '</li>'
    output += '</ul>'
    return output