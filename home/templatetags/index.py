from django import template
register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i]

@register.filter
def getitem(indexable, i):
    return indexable[i]

@register.filter
def gave_exam(indexable):
    from home.models import Result
    result = Result.objects.filter(idt=indexable.pk)
    if result:
        return True
    else:
        return False
    