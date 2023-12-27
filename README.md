# Titulo
Espaço ``Subtitulo``  Framework [Django](https://docs.djangoproject.com/en/5.0/)

---

## Versão Número da versão

&nbsp;

> ### Pré-requisitos

Quais pre-requisitos o sistema irá precisar para funcionar
 
&nbsp;
  
> ### Bibliotécas
 
[Django](https://docs.djangoproject.com/en/5.0/)

[Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

[SQLite](https://www.sqlite.org/docs.html)

&nbsp;

> ### Funcionalidades:

* Salvar os dados em um banco [SQLite](https://www.sqlite.org/docs.html)

&nbsp; 

> ### Pré-code
> > virtual environment
#### Feito via terminal, instalação de um ambiente virtual
    python -m venv env
    .\env\Scripts\activate

> > #### Instalando as bibliotécas

    python -m pip install --upgrade pip
    pip install django 

&nbsp;
> ### Code
> > #### Criação do projeto
 
    django-admin startproject nome_do_projeto .
&nbsp;

>> #### Criação dos App's

    python manage.py startapp app_nome_app
&nbsp;
* obs>> navege até ``./nome_do_projeto/settings.py``
em `INSTALLED_APPS` e adicione o `app_nome_app`
&nbsp;

>>> ##### Sequencia de criação

1. Criar a rota, `link` (urls.py)
2. Criar o que fazer quando chegar ao link (views.py)
3. Criar oque exibir quando chegar ao link (html e css)

&nbsp;

   1. Em ``./nome_do_projeto/urls.py`` vamos criar a rota para a pagina inicial
&nbsp;
    
   2. Em ``./nome_do_projeto/app_nome_app/views.py``  vamos criar a função ``home``
&nbsp;

   3. Em ``./nome_do_projeto/app_nome_app/templates/usuarios`` vamos criar o arquivo ``home.html`` e ``base.html``
&nbsp;

>> #### Visulizar projeto e estilização
    python manage.py runserver

Nas documentações do [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) vamos buscar uma estilização para compor nossa ``home`` e etc...
&nbsp;

>>>###### teste web em terminal
    


&nbsp;

* Faremos um template base pra não precisar reescrever todas as informaçoes e componetes do bootstrap em ``./nome_do_projeto/app_nome_app/templates/usuarios/base.html``
&nbsp;

**Fizemos a estilização da página de usuarios**

&nbsp;

> ### Uso
* Em terminal.
&nbsp;  
    python manage.py makemigrations

        python manage.py migrate 

            python manage.py runserver

* Depois em navegador
  
        http://127.0.0.1:8000

&nbsp;

> ### Implementação

 [Django](https://docs.djangoproject.com/en/5.0/) em uso para codificação.

&nbsp;

> Créditos

Código inicial baseado no canal [Canal](https://www.youtube.com).


Documentação e melhorias adicionadas por [Wesley Pereira](https://github.com/wesleyp846)

&nbsp;
> Licença
> > MIT


Espero que a documentação os ajude a entender a aplicação! 
Por favor, sinta-se a vontade para melhorá-la.