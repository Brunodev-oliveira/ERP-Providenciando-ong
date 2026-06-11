
# 🧠 Sistema de Gestão para ONGs — Providenciando a Favor da Vida

## 📋 Sobre o Projeto

O Sistema de Gestão para ONGs é uma aplicação web desenvolvida para apoiar as operações da ONG **Providenciando a Favor da Vida**, oferecendo ferramentas para o gerenciamento de beneficiários, voluntários, projetos sociais, doações e controle de estoque.

A plataforma centraliza informações importantes da instituição em um único ambiente, permitindo maior organização dos processos internos, rastreabilidade das ações sociais e melhor utilização dos recursos disponíveis.

O sistema foi desenvolvido utilizando **Django** e segue uma arquitetura baseada em aplicações modulares, facilitando a manutenção, escalabilidade e evolução contínua da solução.

----------

## 🚀 Principais Funcionalidades

### 👥 Gestão de Beneficiários

-   Cadastro, edição e consulta de beneficiários;
    
-   Armazenamento de informações cadastrais e histórico de participação;
    
-   Organização e acompanhamento dos atendimentos realizados.
    

### ❤️ Gestão de Doações

-   Registro e acompanhamento de doações recebidas;
    
-   Controle das entradas de recursos e itens doados;
    
-   Histórico completo das movimentações.
    

### 📂 Gestão de Projetos Sociais

-   Cadastro e gerenciamento de projetos desenvolvidos pela ONG;
    
-   Associação de beneficiários aos projetos;
    
-   Acompanhamento das ações realizadas.
    

### 📝 Gestão de Inscrições

-   Vinculação de beneficiários aos projetos sociais;
    
-   Controle de participação em atividades e programas.
    

### 📦 Controle de Estoque

-   Registro de entradas de produtos e materiais;
    
-   Controle de fornecedores;
    
-   Geração automática de números de lote;
    
-   Rastreamento de movimentações de estoque.
    

### 🔐 Controle de Acesso

-   Autenticação de usuários;
    
-   Controle de permissões por perfil;
    
-   Proteção de áreas administrativas.
    

----------

## 🛠️ Tecnologias Utilizadas

### Backend

-   Python
    
-   Django
    
-   Django ORM
    

### Frontend

-   HTML5
    
-   CSS3
    
-   JavaScript
    
-   Django Templates
    

### Segurança e Infraestrutura

-   Django Authentication
    
-   Django Forms
    
-   Django Middleware
    
-   Python Decouple
    
-   Variáveis de ambiente (.env)
    

----------

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
├── requirements.txt
├── .env.example
└── README.md

```

----------

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

----------

## 🔐 Configuração das Variáveis de Ambiente

Este projeto utiliza o **python-decouple** para gerenciar configurações sensíveis e variáveis de ambiente.

### Criando o arquivo `.env`

Copie o arquivo de exemplo:

```bash
cp .env.example .env

```

Ou crie manualmente um arquivo chamado `.env` na raiz do projeto.

### Gerando uma SECRET_KEY

Execute o comando abaixo para gerar uma chave segura para o Django:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

```

Copie o valor gerado para a variável `SECRET_KEY` do arquivo `.env`.

### Exemplo de configuração

```env
SECRET_KEY=sua-chave-gerada-aqui
DEBUG=True

DB_NAME=db.sqlite3
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

```

> **Importante:** Nunca envie o arquivo `.env` para o GitHub. Apenas o arquivo `.env.example` deve ser versionado.

----------

### 5. Executar as migrações

```bash
python manage.py makemigrations
python manage.py migrate

```

### 6. Criar um usuário administrador

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

----------

## 💻 Como Utilizar

Após iniciar a aplicação:

1.  Acesse `http://localhost:8000`;
    
2.  Faça login utilizando uma conta autorizada;
    
3.  Cadastre beneficiários atendidos pela instituição;
    
4.  Registre doações recebidas;
    
5.  Crie e acompanhe projetos sociais;
    
6.  Vincule beneficiários aos projetos;
    
7.  Gerencie o estoque e acompanhe as movimentações de entrada e saída.
    

----------

## 🎯 Objetivo

Este projeto foi desenvolvido com o propósito de apoiar a transformação digital da ONG **Providenciando a Favor da Vida**, reduzindo processos manuais e proporcionando maior controle, transparência e eficiência na gestão de ações sociais.

A solução busca facilitar o acompanhamento dos beneficiários atendidos, otimizar a distribuição de recursos e fortalecer a capacidade administrativa da instituição.

----------

## 📸 Demonstração

Adicione aqui capturas de tela das principais funcionalidades do sistema:

-   Dashboard principal;
    
-   Cadastro de beneficiários;
    
-   Gestão de projetos sociais;
    
-   Controle de doações;
    
-   Controle de estoque;
    
-   Painel administrativo;
    
-   Relatórios e indicadores.
    

----------

## 🤝 Contribuições

Contribuições são bem-vindas.

1.  Faça um Fork do projeto;
    
2.  Crie uma branch para sua funcionalidade:
    

```bash
git checkout -b feature/minha-funcionalidade

```

3.  Realize suas alterações;
    
4.  Faça commit das mudanças:
    

```bash
git commit -m "feat: descrição da funcionalidade"

```

5.  Envie para seu fork:
    

```bash
git push origin feature/minha-funcionalidade

```

6.  Abra um Pull Request.
    

----------

## 📝 Licença

Este projeto está licenciado sob a Licença MIT.

Consulte o arquivo `LICENSE` para mais informações.

----------

## 👨‍💻 Autor

Desenvolvido por **Bruno Oliveira** como parte do processo de modernização e gestão tecnológica da ONG **Providenciando a Favor da Vida**.

----------

## 💙 Sobre a ONG

A **Providenciando a Favor da Vida** é uma organização social dedicada ao desenvolvimento humano e ao apoio de mãe e gestantes em situação de vulnerabilidade social, promovendo projetos, ações comunitárias e iniciativas voltadas à melhoria da qualidade de vida da população atendida.

Este sistema foi desenvolvido para auxiliar a instituição na gestão de suas atividades e ampliar sua capacidade de impacto social.
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
