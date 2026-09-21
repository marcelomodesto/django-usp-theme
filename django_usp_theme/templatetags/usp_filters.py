from django import template
import os

register = template.Library()


@register.filter(name='usp_moeda')
def usp_moeda(value):
    """Formata valor para formato brasileiro (R$ 1.234,56)."""
    if value is None or value == '':
        return ""
    try:
        val = float(value)
        return f"R$ {val:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except (ValueError, TypeError):
        return value


@register.filter(name='usp_filename')
def usp_filename(value):
    """Extrai nome do arquivo de um caminho."""
    if value is None:
        return ""
    return os.path.basename(str(value))
