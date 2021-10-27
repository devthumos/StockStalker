![SignUp Mobile](imgs_readme/banner.png)

<p align="center">Projeto Transversal em Redes de comunicação da Universidade de Brasília (UnB), realizado pelos alunos Luís Fernando Ferreira Pereira Lopes e Gabriel Filipe de Oliveira Cardoso.</p>
<p align="center">Aplicação GUI que mostra os principais indicadores financeiros dos fundos imobiliários, fundos de investimento, ações, bdrs e tesouro a partir de seu código de negociação (ações fii, bdrs) ou nome (tesouro, fundo de investimento)</p>

<h4 align="center"> 
	🚧  ActionStalker 🚀 Em construção...  🚧
</h4>

### Pré-requisitos

---

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [XAMPP](https://www.apachefriends.org/index.html), [Python 3.8+](https://www.python.org/). 
Além disto é bom ter um editor, recomendável o [Pycharm Community](https://code.visualstudio.com/), para trabalhar com o código

## Passo a Passo Para a Primeira Inicialização do Action Stalker

---

### 🎲 Clonando o Repositório e Instalando os Requerimentos (passo 1)
```bash
# Clone este repositório
$ git clone <https://https://github.com/devthumos/ActionStalker>

# Acesse a pasta do projeto no terminal/cmd e instale os requisitos
$ pip install pymysql
$ pip install beautifulsoup4
$ pip install requests
$ pip install webdriver-manager
$ pip install ttkbootstrap

# Se tudo ocorreu bem, vamos para o próximo passo

```

### 🎲 Execute o XAMPP e clique em start para MySQL e APACHE (passo 2)
![SignUp Mobile](imgs_readme/xampp.png)

### 🎲  Execute o script create_table_login_registros.py para a criação dos bancos e tabelas iniciais (passo 3)
```bash
# 
# Acesse a pasta do projeto/src/MySQL/ no terminal/cmd e execute o script create_table_login_registros.py
$ python create_table_login_registros.py

# Se tudo ocorreu bem, vamos para o próximo passo

```

### 🎲  Execute o script window_login_class_atualizado.py para a iniciar o programa (passo 4)
```bash
# 
# Acesse a pasta do projeto/src/MySQL/ no terminal/cmd e execute o script create_table_login_registros.py
$ python window_login_class_atualizado.py

# Se tudo ocorreu bem, vamos para o próximo passo

```

## Action Stalker inicializado e agora??

---

### 🎲  Vamos se Cadastrar?? (passo 1)
![SignUp Mobile](imgs_readme/login.png)<br>
- Caso não tenha se registrado ainda, insira um usuário e senhar para se cadastrar no banco local
- Logue com a sua conta recém cadastrada para ter acesso à sua carteira<br>
_Lembre-se que o servidor local deve estar rodando para que o Action Stalker funcione_ 

### 🎲  Certo, estou na carteira, o que eu faço?? (passo 2)
![SignUp Mobile](imgs_readme/carteira.png)<br>
- Insira o código da FII/Ação/BDRS que deseja acompanhar ou o nome do fundo de investimento/tesouro, com "-" em vez de espaços, e aperte no botão "Registrar"
- Caso não saiba que código colocar ou o nome do fundo de investimento/tesouro, navegue pelo [statusinvest](https://statusinvest.com.br) e copie a parte final do link
![SignUp Mobile](imgs_readme/link.png)

### 🎲  Código adicionado (passo 3)
![SignUp Mobile](imgs_readme/adicionado.png)<br>
- Parabéns, você tem o seu primeiro negócio adicionado à sua carteira 😃
- Com o código adicionado, poderá ser lido todos os indicadores principais a cerca do que foi adicionado
- Todos os códigos adicionados serão atualizados de 1 em 1 minuto ou no momento em que for apertado o botão "Atualizar", bem simples neh?

## Não quero Mais ver sobre esse negócio!! 😡
### 🎲  Removendo items (passo 1)
![SignUp Mobile](imgs_readme/remover.png)<br>
- Para remover qualquer negócio, clique em apenas um ou utilize o "Ctrl" e selecione vários negócios
- Clique no botão "Remover" e pronto!!
### 🛠 Tecnologias

---

As seguintes ferramentas foram usadas na construção do projeto:

- [python](https://docs.python.org/3/)
- [tkinter](https://tkdocs.com/tutorial/index.html)
- [pymysql](https://pymysql.readthedocs.io/en/latest/)
- [bs4](https://beautiful-soup-4.readthedocs.io/en/latest/)

### Autor

---

<a href="https://www.linkedin.com/in/luís-fernando-ferreira-pereira-lopes">
 <img style="border-radius: 50%;" src="https://media-exp1.licdn.com/dms/image/C5603AQFfQUIj_QemJA/profile-displayphoto-shrink_400_400/0/1607378780137?e=1640822400&v=beta&t=hird4Q98yHn-6HHWSigqxnKb1IlxY6Hp7KuHqpZUcZc" width="100px;" alt=""/>
 <br />
<sub><b>Luís Fernando</b></sub></a> <a href="https://www.linkedin.com/in/luís-fernando-ferreira-pereira-lopes" title="Linkedin">🚀
</a>

<a href="#Gabriel">
 <img style="border-radius: 50%;" src="" width="100px;" alt=""/>
 <br />
<sub><b>Gabriel Filipe</b></sub></a> <a href="" title="Linkedin">🚀
</a>


Feito por Luís Fernando Ferreira Pereira Lopes e Gabriel Filipe de Oliveira Cardoso 👋🏽 Entre em contato!
