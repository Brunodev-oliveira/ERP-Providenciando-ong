# 🧠 Sistema de Gestão para ONGs — Providenciando a Favor da Vida

## 📋 Sobre o Projeto

O Sistema de Gestão para ONGs é uma aplicação web desenvolvida para apoiar as operações da ONG **Providenciando a Favor da Vida**, oferecendo ferramentas para o gerenciamento de beneficiários, voluntários, projetos sociais, doações e controle de estoque.

A plataforma centraliza informações importantes da instituição em um único ambiente, permitindo maior organização dos processos internos, rastreabilidade das ações sociais e melhor utilização dos recursos disponíveis.

O sistema foi desenvolvido utilizando **Django** e segue uma arquitetura baseada em aplicações modulares, facilitando a manutenção, escalabilidade e evolução contínua da solução.

---

## 🚀 Principais Funcionalidades

### 👥 Gestão de Beneficiários

* Cadastro, edição e consulta de beneficiários;
* Armazenamento de informações cadastrais e histórico de participação;
* Organização e acompanhamento dos atendimentos realizados.

### ❤️ Gestão de Doações

* Registro e acompanhamento de doações recebidas;
* Controle das entradas de recursos e itens doados;
* Histórico completo das movimentações.

### 📂 Gestão de Projetos Sociais

* Cadastro e gerenciamento de projetos desenvolvidos pela ONG;
* Associação de beneficiários aos projetos;
* Acompanhamento das ações realizadas.

### 📝 Gestão de Inscrições

* Vinculação de beneficiários aos projetos sociais;
* Controle de participação em atividades e programas.

### 📦 Controle de Estoque

* Registro de entradas de produtos e materiais;
* Controle de fornecedores;
* Geração automática de números de lote;
* Rastreamento de movimentações de estoque.

### 🔐 Controle de Acesso

* Autenticação de usuários;
* Controle de permissões por perfil;
* Proteção de áreas administrativas.

---

## 🛠️ Tecnologias Utilizadas

### Backend

* Python
* Django
* Django ORM

### Frontend

* HTML5
* CSS3
* JavaScript
* Django Templates

### Segurança e Infraestrutura

* Sistema de autenticação do Django
* Middleware personalizado
* Validação de formulários com Django Forms

---

## 📂 Estrutura do Projeto

```text
erp-ong/

├── beneficiaries/     # Gestão de beneficiários
├── donations/         # Gestão de doações
├── projects/          # Gestão de projetos sociais
├── stock/             # Controle de estoque
├── accounts/          # Autenticação e usuários
├── core/              # Configurações e middlewares
├── manage.py
└── requirements.txt
```

---

## ⚙️ Instalação e Execução

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
```

### 2. Acessar o diretório do projeto

```bash
cd erp-ong
```

### 3. Criar e ativar um ambiente virtual

Linux/macOS:

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Executar as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Criar usuário administrador

```bash
python manage.py createsuperuser
```

### 7. Iniciar o servidor

```bash
python manage.py runserver
```

A aplicação estará disponível em:

```text
http://localhost:8000
```

---

## 📸 Demonstração

Adicione capturas de tela das principais funcionalidades:

* Dashboard principal;
* Cadastro de beneficiários;
* Gestão de projetos sociais;
* Controle de doações;
* Controle de estoque;
* Administração do sistema.

---

## 🎯 Objetivo

Este projeto foi desenvolvido com o propósito de apoiar a transformação digital da ONG **Providenciando a Favor da Vida**, reduzindo processos manuais e proporcionando maior controle, transparência e eficiência na gestão de ações sociais.

A solução busca facilitar o acompanhamento dos beneficiários atendidos, otimizar a distribuição de recursos e fortalecer a capacidade administrativa da instituição.

---

## 🤝 Contribuições

Contribuições são bem-vindas.

Para colaborar:

1. Faça um fork do projeto;
2. Crie uma branch para sua funcionalidade;

```bash
git checkout -b feature/minha-funcionalidade
```

3. Realize suas alterações;
4. Faça commit das mudanças;

```bash
git commit -m "feat: descrição da funcionalidade"
```

5. Envie para seu fork;

```bash
git push origin feature/minha-funcionalidade
```

6. Abra um Pull Request.

---

## 📝 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais informações.

---

## 👨‍💻 Autor

Desenvolvido por Bruno Oliveira como parte do processo de modernização e gestão tecnológica da ONG **Providenciando a Favor da Vida**.
