# Automation Practice

## Cenários de Testes

Este repositório contém modelos de testes automatizados realizados para o site [Automation Pratice](http://automationpractice.pl/index.php?controller=authentication&back=myaccount). Foram escolhidos três cenários de testes conforme descritos abaixo.

- Cenário 1: Verificar a criação de um novo usuário.
  - Dado que o usuário esteja na página de login "Authentication" do “automation practice”
  - Quando o usuário preencher o campo "email address" na categoria "Create an Account" e em seguida clicar no botão "Create an account"
  - Então o usuário será redirecionado para a página "Create an account"
  - Dado que o usuário esteja na página "Create an accout"
  - Quando o usuário preencher todos os dados solicitados e em seguida clicar em "Register"
  - Então será redirecionado para a página "My account" e também será exibido um alert na cor verde com o texto "Your account has been created.".

- Cenário 2: Verificar o cadastro de um novo endereço.
  - Dado que o usuário esteja na página "My account"
  - Quando o usuário clicar em "My address"
  - Então será redirecionado para a página "My address"
  - Dado que o usuário esteja na página "My address"
  - Quando o usuário clicar em "Add a new address"
  - Então será redirecionado para a página "Your address"
  - Dado que o usuário esteja na página "My address"
  - Quando o usuário clicar em "Add a new address"
  - Então será redirecionado para a página "Your address"
  - Dado que o usuário esteja na página "Your address"
  - Quando o usuário preencher todos os dados solicitados e clicar no botão "Save"
  - Então será redirecionado para a página "My address" e também box com o resumo do endereço anteriormente cadastrado.

- Cenário 3: Verificar o Sign out e o Login de um usuário cadastrado.
  - Dado que o usuário esteja na página "My address" ou qualquer tela que tenha a navbar
  - Quando o usuário clicar em "Sign out"
  - Então será redirecionado para a página "Authentication"
  - Dado que o usuário esteja na página "Authentication"
  - Quando o usuário preencher os dados de "email address" e "password" e em seguida clicar em "Sign in"
  - Então será redirecionado para a página "My address" ou a mesma outra tela que estiva aberta.

- Cenário 4: Verificar a função "esqueceu sua senha?"
  - Dado que o usuário esteja na página "Authentication"
  - Quando o usuário clicar em "Forgot your password?"
  - Então será redirecionado para a página "Forgot your password?"
  - Dado que o usuário esteja na página "Forgot your password?"
  - Quando o usuário preencher o campo "email address" com um email válido cadastrado e em seguida clicar em "Retrive password"
  - Então Então será redirecionado para a página "Forgot your password?" com uma confirmação de um parágrafo na cor verde contendo o texto "A confirmation email has been sent to your address: endereco_email".

O arquivo contendo os testes em um fluxo contínuo do 1° cenário ao 3° cenário é [test_cenarios.py](https://github.com/geissonlucaso/automation_pratice/blob/5a62ea00b88be67f429e0b2eed0b4db741a855d7/test_cenarios.py).

No diretório `tests` há cada um dos cenários para serem executados de forma isolada.

## Settings e Setup

- Ambiente de desenvolvimento.

  - `VS Code`, `Selenium Webdriver`, `Python`, `venv`.

- Configuração para execução.
  - Foi utilizado nesse projeto o conceito de `Virtual Environment`para restringir as dependência para apenas o projeto de testes. Ao fazer o clone do repositorio, crie um `venv` por meio do comando `python -m venv venv` e então será criada um diretório `venv` .
  - As dependências necessárias para o funcionamento do projeto estão listadas no arquivo `requiriments.txt` e para instalar basta fazer o comando `pip install -r requirements.txt`.
  - Ative o seu `venv` para acessar as dependências por meio do comando `.\venv\Scripts\Activate.ps1` pelo terminal PowerShell.
  - O script está pronto para ser executado.
