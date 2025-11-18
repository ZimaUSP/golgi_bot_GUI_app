# Interface gráfica do Golgi Bot
Repositório que organiza o código usado na Interface Gráfica (GUI) para o Golgi Bot, a Automação da Farmácia do Hospital Universitário.

---

## 📌 Características do ambiente utilizado

Este projeto foi desenvolvido em uma Labrador v2, que possui um processador ARM de 32 bits. O sistema operacional utilizado é o Debian 12, com a versão do Python 3.11.x.

![Imagem labrador](readme_images/labrador.png)

---

## 🔧 Ambiente virtual  
Este projeto utiliza o `venv` para organizar as bibliotecas utilizadas.

### Instalação e criação do venv
```bash
# Instalar o venv
sudo apt install python3 python3-venv python3-pip

# Criar e ativar ambiente virtual
python3 -m venv venv
source venv/bin/activate
```

## 📦 Dependências

As bibliotecas utilizadas nesse projeto, que também estão no arquivo `requirements.txt`, são:
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
Apenas uma das bibliotecas foi instalada no ambiente virtual criado utilizando o pip, pois não está presente nos repositórios do Debian:
```bash
source venv/bin/activate
pip install customtkinter
```
As demais bibliotecas foram instaladas diretamente no sistema a partir do APT:
```bash
sudo apt install python3-packagename
```
Essa abordagem se mostrou necessária devido à limitação do chip de 32 bits, que impossibilita o pacote `numpy`, dependência do `pandas`, de ser instalado a partir do pip. Nota-se, no entanto, que caso uma placa com chip de 64 bits tivesse sido usada, tudo poderia ter sido instalado a partir do pip.

### 🔹 Tornando os pacotes do sistema visíveis no ambiente virtual

Por padrão, o ambiente virtual criado com o `venv` não acessa os pacotes do sistema.  
A configuração responsável por isso está no arquivo:

📄 `venv/pyvenv.cfg`

Nele, havia a linha:
```bash
include-system-site-packages = false
```
Essa linha foi alterada para:
```bash
include-system-site-packages = true
```
Isso permite que o ambiente virtual utilize os pacotes instalados no sistema.

---

## ▶️ Como inicializar a interface


Para inicializar a interface, basta rodar os seguintes comandos no diretório correto:
```bash
source venv/bin/activate
python3 golgi_main.py
```
![Tela de login](readme_images/login.png)

Assim, a tela de login do enfermeiro será exibida (para testes, o login era feito com "0" e a senha "admin"). Se for a primeira vez utilizando a interface, depois que o login é efetuado, é importante verificar se a porta de comunicação serial com o Golgi está devidamente selecionada em "Configurações". Nessa tela, deve-se clicar no botão em azul com o nome de alguma porta serial já utilizada no passado (por exemplo, pode estar escrito "port: COM6"), e depois disso, selecionar a devida porta de comunicação serial com o Golgi para que a interface possa se comunicar com o robô.

![Tela de configurações](readme_images/settings.png)

Quando as configurações estiverem corretas, já é possível ir até a tela de coleta, onde, em uma primeira parte (opcional), será solicitado o dado do paciente para quem o remédio será coletado, e depois a seleção e a coleta dos remédios poderá ser feita. 

![Tela de coleta](readme_images/search.png)

A partir dessa tela de coleta, depois de pesquisar um remédio e clicar o nome correspondente da lista, é possível selecionar a quantia desejada do remédio, adicionar esse (e outros) pedido(s) no carrinho e, por fim, clicar no botão de coleta para que o Golgi realize seu trabalho.

![Tela de exemplo da coleta](readme_images/ex_collect.png)