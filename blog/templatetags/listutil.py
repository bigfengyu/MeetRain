"""
Template tags for working with lists.

You'll use these in templates thusly::

    {% load listutil %}
    {% for sublist in mylist|parition:"3" %}
        {% for item in mylist %}
            do something with {{ item }}
        {% endfor %}
    {% endfor %}
"""

from django import template

register = template.Library()

@register.filter
def partition(thelist, n):
    """
    Break a list into ``n`` pieces. The last list may be larger than the rest if
    the list doesn't break cleanly. That is::

        >>> l = range(10)

        >>> partition(l, 2)
        [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]

        >>> partition(l, 3)
        [[0, 1, 2], [3, 4, 5], [6, 7, 8, 9]]

        >>> partition(l, 4)
        [[0, 1], [2, 3], [4, 5], [6, 7, 8, 9]]

        >>> partition(l, 5)
        [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]

    """
    try:
        n = int(n)
        thelist = list(thelist)
    except (ValueError, TypeError):
        return [thelist]
    p = len(thelist) / n
    return [thelist[p*i:p*(i+1)] for i in range(n - 1)] + [thelist[p*(i+1):]]

@register.filter
def partition_horizontal(thelist, n):
    try:
        n = int(n)
        thelist = list(thelist)
    except (ValueError, TypeError):
        return [thelist]
    newlists = [list() for i in range(n)]
    for i, val in enumerate(thelist):
        newlists[i%n].append(val)
    return newlists

@register.filter
def partition_col(thelist,n):
    try:
        n = int(n)
        thelist = list(thelist)
    except(ValueError,TypeError):
        return thelist
    res = [[] for i in range(n)]
    l = len(thelist)
    for i in range(l):
        res[i%n].append(thelist[i])
    return res



