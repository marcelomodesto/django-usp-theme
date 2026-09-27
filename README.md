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


{% block nav_items %}
  <a class="nav-link" href="#"><i class="bi bi-house"></i>home</a>
  <div class="nav-item dropdown">
    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
      <i class="bi bi-menu-button"></i>
      dropdown
    </a>
    <ul class="dropdown-menu dropdown-menu-end">
      <li><a class="dropdown-item" href="#">dropdown item 1</a></li>
      <li><a class="dropdown-item" href="#">dropdown item 2</a></li>
    </ul>
  </div>
{% endblock %}


{% block content %}
<!-- Conteúdo da página -->
{% endblock %}
```

### Rotas de login e logout
Rotas de login e logout

O tema não registra rotas. O roteamento é responsabilidade da aplicação cliente,
que decide quais views de autenticação usar (login local, Senha Única, OIDC, etc.).

Por padrão, o tema procura pelas rotas login e logout. O botão Entrar só
aparece se a rota de login existir, e o botão Sair só aparece se a rota de
logout existir. Se não existirem, os botões são simplesmente omitidos — sem erros.


### Nomes de rotas customizados
Se sua aplicação usa nomes diferentes (ex: oauth_login), defina no settings.py:

```python
THEME_LOGIN_URL_NAME = 'oauth_login'
THEME_LOGOUT_URL_NAME = 'logout'
```

Ou, se preferir ler de variáveis de ambiente:


```python
import os

THEME_LOGIN_URL_NAME = os.environ.get('THEME_LOGIN_URL_NAME', 'login')
THEME_LOGOUT_URL_NAME = os.environ.get('THEME_LOGOUT_URL_NAME', 'logout')
```


Importante: essas settings são nomes de rotas (usados em {% url %}),
não caminhos. Não confunda com LOGIN_URL, LOGIN_REDIRECT_URL e
LOGOUT_REDIRECT_URL, que são settings nativas do Django e esperam caminhos
(ou nomes de rota, no caso de LOGIN_REDIRECT_URL e LOGOUT_REDIRECT_URL).

Settings nativas do Django

As settings abaixo não são do tema, mas do próprio Django. Elas controlam os
redirecionamentos do fluxo de autenticação:
Setting	O que faz	Exemplo

LOGIN_URL	Caminho para onde redirecionar usuários não autenticados	'/login/'

LOGIN_REDIRECT_URL	Para onde ir após o login bem-sucedido	'/'

LOGOUT_REDIRECT_URL	Para onde ir após o logout	'login'

Se LOGOUT_REDIRECT_URL não for definida, o Django redireciona para /admin/
(ou para a página de logout padrão do admin). Para voltar à tela de login após
sair, defina:



```python
LOGOUT_REDIRECT_URL = 'login'
```




Exemplo mínimo em urls.py:

```python

from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html'
        ),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]
```

O import necessário é:


```python
from django.contrib.auth import views as auth_views
```


Se sua aplicação usar a Senha Única da USP, a rota de login pode apontar para a
view da django-oauth-usp:


```python
from django_oauth_usp.accounts.views import accounts_login

urlpatterns = [
    path('login/', accounts_login, name='oauth_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
```

E no settings.py:

```python
THEME_LOGIN_URL_NAME = 'oauth_login'
LOGOUT_REDIRECT_URL = 'oauth_login'  # volta para o login da Senha Única
```



    Nota: o LogoutView do Django exige requisição POST. O template do tema
    já envia o logout via formulário com {% csrf_token %}, então nenhuma
    configuração adicional é necessária.


#### Ocultar ou substituir os botões

Para ocultar ou substituir os botões padrão, sobrescreva os blocos
nav_login e nav_logout no seu template:

```python
{% extends "usp_theme/base.html" %}

{% block nav_login %}
  <a href="{% url 'oauth_login' %}" class="btn btn-sm btn-link">
    <i class="bi bi-box-arrow-in-left"></i> Senha Única
  </a>
{% endblock %}

{% block nav_logout %}{% endblock %}
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
