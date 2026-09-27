from django import template
from django.conf import settings
from django.urls import reverse, NoReverseMatch

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


# usp_filters.py do tema
@register.simple_tag
def theme_login_url_name():
    return getattr(settings, 'THEME_LOGIN_URL_NAME', 'login')


@register.simple_tag
def theme_logout_url_name():
    return getattr(settings, 'THEME_LOGOUT_URL_NAME', 'logout')