from django import template
import random


register = template.Library()


@register.filter
def first(mylist):

    if mylist is not None and len(mylist):
        return mylist[0]


@register.filter
def suit(list, suit_type):
    return [item for item in list if item.get_suit_display() == suit_type]


@register.filter
def rank(list, rank_type):
    return [item for item in list if item.rank == rank_type]


@register.filter
def shuffle(list):
    return random.shuffle(list)


@register.filter
def deal(list, amount):
    return list[:amount]
