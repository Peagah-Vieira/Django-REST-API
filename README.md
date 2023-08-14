# Django REST API

Projeto concretizado com o objetivo de showcase do conhecimento adquirido através do Roadmap, destinado a servir como um exemplar ilustrativo.

## Executando localmente

Clone o projeto

```bash
git clone https://github.com/Peagah-Vieira/Django-REST-API.git
```

Crie um ambiente virtual

```bash
# Linux
sudo apt-get install python3-venv
python3 -m venv .venv
source .venv/bin/activate

# macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
py -3 -m venv .venv
.venv\scripts\activate
```

Atualize o pip

```bash
py -m pip install --upgrade pip
```

Instale as dependências

```bash
pip install -r requirements.txt
```

Copie o arquivo env de exemplo e faça as alterações de configuração necessárias no arquivo .env

```bash
cp .env.example .env
```

Realize as migrações

```bash
py manage.py migrate
```

Inicie o servidor

```bash
py manage.py runserver
```

## Endpoints

Criar token

```
127.0.0.1:8000/api/token/
```

Atualizar token

```
127.0.0.1:8000/api/token/refresh/
```

Verificar token

```
127.0.0.1:8000/api/token/verify/
```

Listar todos os usuários (Somente Staff)

```
127.0.0.1:8000/accounts/users/
```

Recuperar usuário logado

```
127.0.0.1:8000/accounts/me/
```

Listar(GET) e criar(POST) Artigos

```
127.0.0.1:8000/articles/api/
```

Recuperar(GET), corrigir(PATCH) e excluir(DELETE) Artigo

```
127.0.0.1:8000/articles/api/{id}
```

Listar(GET) e criar(POST) Categorias

```
127.0.0.1:8000/articles/categories/api/
```

Recuperar(GET), corrigir(PATCH) e excluir(DELETE) Categoria

```
127.0.0.1:8000/articles/categories/api/{id}
```

## Aprendizado

[API](https://www.linkedin.com/posts/pedro-henrique-vieira-073b62236_desenvolvedorbackend-roadmap-explorandoapis-activity-7094829637951770624-IrZM?utm_source=share&utm_medium=member_desktop)

[REST](https://www.linkedin.com/posts/pedro-henrique-vieira-073b62236_desenvolvedorbackend-roadmap-explorandoapis-activity-7095101433598926848-X-uT?utm_source=share&utm_medium=member_desktop)

[Decidindo entre IDs e UUID](https://www.linkedin.com/posts/pedro-henrique-vieira-073b62236_arquiteturadebancodedados-idsvsuuids-activity-7095502863371542528-OXIB?utm_source=share&utm_medium=member_desktop)

[API Authentication](https://www.linkedin.com/posts/pedro-henrique-vieira-073b62236_desenvolvedorbackend-roadmap-explorandoapis-activity-7096913363972108288-SPjn?utm_source=share&utm_medium=member_desktop)

## Documentação

[Python](https://www.python.org)

[Django](https://www.djangoproject.com)
