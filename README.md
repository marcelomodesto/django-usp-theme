# django-usp-theme

Tema visual USP para aplicações Django — design system, componentes e templates reutilizáveis.

## Instalação

```bash
pip install django-usp-theme
```

## Configuração

Adicione `django_usp_theme` ao `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'django_usp_theme',
]
```

## Uso

### Template base

Estenda o template base em seus templates:

```html
{% extends "usp_theme/base.html" %}
{% load static usp_filters %}

{% block title %}Minha Aplicação{% endblock %}

{% block header_logo %}
<a href="https://www.usp.br">
    <img src="{% static 'usp_theme/img/usp-logo-f.png' %}" alt="Logo USP">
</a>
{% endblock %}

{% block brand %}Minha Aplicação{% endblock %}

{% block nav %}
<a class="nav-link" href="{% url 'home' %}">INÍCIO</a>
<a class="nav-link" href="{% url 'lista' %}">LISTA</a>
{% endblock %}

{% block nav_user %}
<div class="nav-user">
    <span>{{ user.username }}</span>
    <form action="{% url 'logout' %}" method="post" class="mb-0">
        {% csrf_token %}
        <button type="submit" class="btn btn-sm btn-outline-secondary">
            <i class="bi bi-door-open"></i> Sair
        </button>
    </form>
</div>
{% endblock %}

{% block content %}
<!-- Conteúdo da página -->
{% endblock %}
```

### Componentes

#### Page Header

```html
{% include "usp_theme/components/page_header.html" %}
```

Ou com bloco:

```html
{% include "usp_theme/components/page_header.html" with title="Minha Página" %}
```

#### Content Card

```html
{% include "usp_theme/components/content_card.html" with card_title="Título do Card" %}
```

#### Empty State

```html
{% include "usp_theme/components/empty_state.html" %}
```

Ou customizado:

```html
{% include "usp_theme/components/empty_state.html" with empty_icon="bi-folder" empty_text="Nenhum item encontrado." %}
```

#### Loading Button

```html
{% include "usp_theme/components/loading_button.html" with text="Salvar" icon="bi-check-lg" loading=False %}
```

### Template Tags

#### usp_moeda

Formata valor para formato brasileiro:

```html
{% load usp_filters %}

{{ valor|usp_moeda }}
<!-- Saída: R$ 1.234,56 -->
```

#### usp_filename

Extrai nome do arquivo de um caminho:

```html
{% load usp_filters %}

{{ caminho|usp_filename }}
<!-- Saída: arquivo.docx -->
```

## CSS

O design system é composto por módulos CSS:

- `tokens.css` — Variáveis CSS (cores, tipografia, espaçamento)
- `base.css` — Reset e tipografia
- `components.css` — Botões, formulários, tabelas, cards, alertas
- `layout.css` — Header, navegação, container
- `utilities.css` — Espaçamento, impressão, acessibilidade

Para usar apenas parte do CSS:

```html
<link href="{% static 'usp_theme/css/tokens.css' %}" rel="stylesheet">
<link href="{% static 'usp_theme/css/base.css' %}" rel="stylesheet">
```

Ou usar o CSS unificado:

```html
<link href="{% static 'usp_theme/css/usp_theme.css' %}" rel="stylesheet">
```

## Variáveis CSS

O tema utiliza CSS custom properties com prefixo `--usp-*`. Para customizar:

```css
:root {
    --usp-color-primary: #0066cc; /* Cor primária personalizada */
}
```

## Licença

MIT
