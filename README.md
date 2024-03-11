## Ambiente Python para desenvolvimento do curso on line
https://www.youtube.com/watch?v=0sOvCWFmrtA

#Instalar Compilador Python diretamente do site
#Instalar VSCode
#Abrir Pasta do projeto FASTAPI

## Criar o ambiente virtual

python -m venv ./venv

## Para ativar o ambiente virtual

source venv/bin/activate


# pode ser necessário rodar o update do pip
pip install update pip

## se criar o ambiente virtual diretamente no windows, ou seja, sem atach ## no ambiente shell de um docker, e apresente mensagem de erro abaixo,
## digitar em seguida: 

Set-ExecutionPolicy Unrestricted

# Ou Tente

Set-ExecutionPolicy -Scope CurrentUser

## responda: 

Unrestricted

## Alterar o compilador python para o compilador do venv

menu-> view->command pallet->Python Selected Interpreter 
Selecione o interpretador dentro de .\venv\Script\python.exe

## Rodando a API Produtos utilizando o framework Django

pip install django #se der erro use abaixo

pip install --upgrade pip
python -m pip install django==4.2.7
pip install --upgrade pip
```

Criar um arquivo txt com as dependências do projeto

```
pip freeze > requirements.txt
```

iniciar um projeto
# django-admin startproject setup .
setup . é obrigatório em projetos django

Para executar o servidor Django


```
python manage.py runserver 0.0.0.0:8000
```

alterar em setup/settings.py

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

Para criar um app no Django
Ele cria uma pasta com mesmo nome: lancamento
```
#python  manage.py startapp produto
python  manage.py startapp lancamento
```
...
dentro da pasta lancamento-> admin.py editar:
...
from lancamento.models import Producao
admin.site.register(Producao)

INSTALLED_APPS = [
    ...,
    'lancamento',


...
dentro da pasta lanacmento-> models.py
...
class Producao(models.Model):
    producao_id = models.AutoField(primary_key=True, db_column="td01_producao_id")
    leitura = models.CharField(max_length=24, db_column="td01_leitura")
    cod_produto = models.CharField(max_length=15, db_column="td01_cod_produto")
    descricao = models.CharField(max_length=30, db_column="td01_descricao")
    status = models.IntegerField(db_column="td01_status")
    id = models.CharField(max_length=6, db_column="td01_id")
    dt = models.DateTimeField(db_column="td01_dt")
    hr = models.TimeField( db_column="td01_hr")
    serie = models.CharField(max_length=6,db_column="td01_serie")
    re = models.CharField(max_length=6, db_column="td01_re")
    local = models.CharField(max_length=4, db_column="td01_local")
    os = models.IntegerField(db_column="td01_os")
class Meta:
        # Definindo o nome da tabela no banco de dados
        db_table = 'td01_producao'

def __str__(self):
        return self.name


Criar a migração dos modelos Django no banco de dados

```
python manage.py makemigrations
```

```
python manage.py migrate
```

Criar um super usuário para o Django Admin

```
python manage.py createsuperuser
```

## Rodando a API Produtos utilizando o framework FastAPI

Acessar o diretório fastapi-produtos

```
cd /referencial/src/fastapi-produtos
```

Para instalar os pacotes necessários para rodar o servidor FastAPI

```
pip install fastapi uvicorn
```

Para executar o servidor FastAPI

```
uvicorn app:app --host 0.0.0.0 --port 8080 --reload
```
