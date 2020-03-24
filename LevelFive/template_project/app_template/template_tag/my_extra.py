from django import template


register = template.library()

@register.filter(name='cut')  #use of decorator

def cut(value,arg):
    """
    this cuts out all values of 'arg' from the string
    """  #this is a doc

    return value.replace(arg,'')


# register.filter('cut',cut)
