🛠️ Sistema de Gerenciamento de Equipamentos — API REST

Este projeto é uma API REST desenvolvida em Django + Django REST Framework para gestão completa de equipamentos dentro de uma organização.
O objetivo é fornecer uma solução robusta, escalável e segura para registrar, acompanhar e controlar o ciclo de vida dos equipamentos.

🚀 Funcionalidades

✔️ Cadastro de categorias
✔️ Cadastro e controle de equipamentos
✔️ Registro de movimentações (entrada/saída)
✔️ Controle de funcionários envolvidos nas movimentações
✔️ Registro de unidades/locais
✔️ Autenticação baseada em JWT (access + refresh)
✔️ Permissões — somente administradores podem criar, editar ou excluir
✔️ Filtros avançados (nome, status, datas e categoria)
✔️ Arquitetura limpa com separação de responsabilidades (services, views, filters, permissions)

🔒 Autenticação

A API utiliza JWT para garantir segurança ao acessar e manipular os dados.
Usuários não autenticados podem apenas visualizar; usuários administradores podem alterar.

Endpoints de autenticação:

/gerenciador/token/ – Gera access e refresh tokens

/gerenciador/token/refresh/ – Renovação do access token

🧩 Organização do Projeto

Models: representação das entidades principais

Serializers: conversão entre modelos e JSON

ViewSets: lógica das rotas e operações CRUD

Services: regras de negócio (ex.: movimentações)

Filters: filtros personalizados com django-filter

Permissions: controle de acesso baseado em regras

🧪 Tecnologias Utilizadas

Python 3

Django

Django REST Framework

SimpleJWT

django-filter

SQLite (padrão, pode ser trocado por PostgreSQL)

📚 Objetivo

Este projeto foi desenvolvido para estudo, prática profissional e como base para aplicações reais que exigem controle de ativos e gestão de fluxo operacional.