#from django import template
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

#register = template.Library()
#
#@register.simple_tag()
#def reset(user):
#    try:
#        Token.objects.get(user=user).delete()
#        Token.objects.create(user=user)
##    except:
#        Token.objects.create(user=user)
