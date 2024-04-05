## Ambiente Python para desenvolvimento do curso on line
https://www.youtube.com/watch?v=0sOvCWFmrtA

#Instalar Compilador Python diretamente do site
#Instalar VSCode
#Abrir Pasta do projeto FASTAPI

## Criar o ambiente virtual

python -m venv ./venv

## Para ativar o ambiente virtual
## (no windows a ativação é feita por .ps1)

.\venv\Scripts\Activate.ps1 


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
