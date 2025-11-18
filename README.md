# golgi_bot_GUI_app  
Interface Gráfica (GUI) para o projeto **Zima’s GolgiBot**

---

## 📌 Pré-requisitos

Este projeto foi desenvolvido e testado em:

- **Debian 12**
- **Python 3.12.1** (A ser verificado)

---

## 🔧 Ambiente virtual  
Este projeto utiliza **pyenv + pyenv-virtualenv** para gerenciar versões do Python e ambientes.

### Instalação e configuração do pyenv
```bash
# Instalar pyenv
curl https://pyenv.run | bash

# Instalar versão específica do Python
pyenv install 3.12.1

# Criar e ativar ambiente virtual
pyenv virtualenv 3.12.1 venv
pyenv activate venv
```

## 📦 Dependências

As bibliotecas utilizadas nesse projeto, que também estão no arquivo requirements.txt, são:
```bash
customtkinter==5.2.2
darkdetect==0.8.0
numpy==2.1.1
packaging==24.1
pandas==2.2.3
pillow==10.4.0
pyserial==3.5
python-dateutil==2.9.0.post0
pytz==2024.2
six==1.16.0
tk==0.1.0
tzdata==2024.2
```
### 🔹 Instalando as dependências

#### 1. Instalar bibliotecas no ambiente virtual
Uma das bibliotecas foi instalada no ambiente virtual criado:
```bash
pyenv activate venv
pip install customtkinter
```
As demais bibliotecas foram instaladas diretamente no sistema a partir do APT:
```bash
sudo apt install python3-packagename
```
### 🔹 Tornando os pacotes do sistema visíveis no ambiente virtual

Por padrão, o ambiente virtual criado pelo pyenv **não acessa** os pacotes do sistema.  
A configuração responsável por isso fica no arquivo:

📄 **`venv/pyvenv.cfg`**

Nele, havia a linha:
```bash
include-system-site-packages = false
```
Essa linha foi alterada para:
```bash
include-system-site-packages = true
```
Isso permite que o ambiente virtual utilize os pacotes instalados via APT.

---

## ▶️ Como inicializar a interface


Para inicializar a interface, basta rodar os seguintes comandos no diretório certo:
```bash
pyenv activate venv
python3 golgi_main.py
```
![Tela de login](readme_images/login.png)

Assim, a tela de login do enfermeiro será exibida (para testes, o login era feito com "0" e a senha "admin"). Se for a primeira vez utilizando a interface, depois que o login é efetuado, é importante verificar se a porta de comunicação com o Golgi está devidamente selecionada em "Configurações". 

![Tela de configurações](readme_images/settings.png)

Quando as configurações estiverem corretas, já é possível ir até a tela de coleta, onde, numa primeira parte (opcional), é requisitado o dado do paciente para quem o remédio será coletado, e depois a seleção e a coleta dos remédios pode ser feita. 

![Tela de coleta](readme_images/search.png)