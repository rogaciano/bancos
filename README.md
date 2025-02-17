# Sistema de Controle Bancário

Sistema desenvolvido em Django para controle de contas bancárias e movimentações financeiras.

## Funcionalidades

- Dashboard com saldo geral e individual das contas
- Cadastro de contas bancárias (banco, número da conta, gerente e contato)
- Registro de movimentações (créditos e débitos)
- Cálculo automático de saldos
- Interface administrativa completa

## Tecnologias Utilizadas

- Python 3.12
- Django 5.0.2
- Bootstrap 5
- Crispy Forms com Bootstrap 5

## Instalação

1. Clone o repositório
```bash
git clone https://github.com/rogaciano/bancos.git
cd bancos
```

2. Crie um ambiente virtual e ative-o
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Execute as migrações
```bash
python manage.py migrate
```

5. Crie um superusuário
```bash
python manage.py createsuperuser
```

6. Inicie o servidor
```bash
python manage.py runserver
```

O sistema estará disponível em `http://127.0.0.1:8000/`

## Uso

1. Acesse a área administrativa em `http://127.0.0.1:8000/admin/`
2. Cadastre as contas bancárias
3. Registre as movimentações
4. Visualize o dashboard com os saldos

## Licença

Este projeto está sob a licença MIT.
