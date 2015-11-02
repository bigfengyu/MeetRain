from django import template
from blog.models import *
register = template.Library()

@register.filter
def ordered_by(queryset, order):
    return queryset.order_by(order)

@register.filter
def get_range( value ):
  """
    Filter - returns a list containing range made from given value
    Usage (in template):

    <ul>{% for i in 3|get_range %}
      <li>{{ i }}. Do something</li>
    {% endfor %}</ul>

    Results with the HTML:
    <ul>
      <li>0. Do something</li>
      <li>1. Do something</li>
      <li>2. Do something</li>
    </ul>

    Instead of 3 one may use the variable set in the views
  """
  return range( value )

@register.filter
def orderbycustom(tagitem):
  if tagitem.normalOrder:
    return tagitem.pages.all().order_by('id')
  else:
    return tagitem.pages.all().order_by('-id')

#
# @register.inclusion_tag('blog/elements/tagitem.html',takes_context=True)
# def getPagesOfCat(context):
#   Cat = context['tagitem']
#   if Cat.normalOrder is True:
#     return {'pages':Cat.pages.all().order_by('date')}
#   else:
#     return {'pages':Cat.pages.all().order_by('-date')}