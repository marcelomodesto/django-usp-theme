from django import template
from django.urls import NoReverseMatch, reverse

register = template.Library()


@register.filter
def url_exists(url_name):
    """
    Retorna True se a URL com o nome informado existir no projeto.
    Útil para templates de módulos reutilizáveis que não podem
    assumir a presença de rotas específicas.
    """
    try:
        reverse(url_name)
        return True
    except NoReverseMatch:
        return False