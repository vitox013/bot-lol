# Lol queue acceptor
Bot com interface gráfica que automatiza o processo de abertura de jogo, escolha de modos, escolha de lanes, processo de aceitar a fila, escolha de campeões e banimento.

Não precisará esperar encontrar uma partida para ir no banheiro ou pegar café, pois agora o bot fará isso automaticamente para você.

## Download
* ### Instalador
  * #### [Clique aqui](https://github.com/vitox013/bot-lol/releases/tag/v4.0.0) para baixar o instalador. 
* ### Antivirus 
  * #### Provavelmente o Windows Defender Smart Screen irá informar que protegeu o computador, pois o programa não possui certificado (tem que pagar), basta clicar em "Mais informações" e clicar em "Executar assim mesmo".
* ### Código fonte aberto.
  #### Como o código é aberto, você poderá conferir o código fonte por si mesmo, caso se sinta inseguro em instalar.
  
## Compilar (ignore caso vá usar o instalador)
### Caso queira compilar por conta própria, basta:
* #### Vá até uma pasta de sua preferência e digite: 
```shell
git clone https://github.com/vitox013/bot-lol.git
```
* #### Será necessario ter o [python3](https://www.python.org/downloads/) instalado.
* #### Instalar o [PyAutoGUI](https://pypi.org/project/PyAutoGUI/), abra seu terminal e digite:
```shell
pip install PyAutoGUI
```
* #### Instalar o [PySimpleGUI](https://pypi.org/project/PySimpleGUI/), abra seu terminal e digite:
```shell
pip install PySimpleGUI
```
* #### Instalar o [opencv-python](https://pypi.org/project/opencv-python/), abra seu terminal e digite:
```shell
pip install opencv-python
```
  

## Pré-requisitos
### Como o bot utiliza de reconhecimento de imagem, é necessário:

* #### Resolução da tela do seu computador ser 1920x1080

* #### Cliente do lol estar no Tamanho da janela 1280x720
   ![Captura de tela 2022-06-28 163726](https://user-images.githubusercontent.com/85710199/176270354-a9169d12-702c-4b82-a9b7-0261ba7237cb.png) 
<br>No cliente do lol ir em Configurações ![eng](https://user-images.githubusercontent.com/85710199/176270865-fd3c763f-4714-48f1-9e3e-5534073c6c40.png)
 -> Cliente/Geral
 
* #### Após abrir o bot e escolher lanes, modo de jogo e campeões, é recomendado não mexer no mouse para não causar erros.


## Como usar

* ### Abertura do bot
  * #### Pode ser aberto a qualquer momento, se o lol estiver fechado o bot abrirá. Porém o bot precisa ser aberto antes de clicar em Encontrar Partida.
  
* ### Selecionar lanes
  * #### Basta selecionar a(s) lane(s) desejada(s) e clicar em "Confirmar Lane"
    ![laneprincipal](https://user-images.githubusercontent.com/85710199/176275371-3ea7564c-d977-4223-b22e-9ffbb299311e.png)
![lanesecundaria](https://user-images.githubusercontent.com/85710199/176275383-99c3d419-be7e-4832-a5e2-b4781eb910b6.png)

    #### Após confirmar a(s) lane(s) o bot mostrará as lanes escolhidas. 
    ![lanesConfirmadas](https://user-images.githubusercontent.com/85710199/176275584-e54f25f6-1fd4-492b-9109-f1b15f466623.png)
    #### Isso significa que podemos ir pra próxima etapa.
    
  * #### Caso usuário tenha aberto o bot com as lanes já selecionadas, não será mostrado a opção selecionar lanes.
  
* ### Selecionar modo de jogo 

  * #### Basta escolhar uma das 3 opções disponíveis:
    ![image](https://user-images.githubusercontent.com/85710199/176276977-4e0a3559-89ef-43b7-8043-d56f6ed08fdb.png)
    
  * #### Caso selecionar modo esteja disponivel e não for selecionado nenhuma opção, o bot NÃO INICIARÁ e a mensagem "Selecione modo de jogo ficará em CAPS".
    ![image](https://user-images.githubusercontent.com/85710199/176278459-93f767c8-1be9-44cd-9604-b13418365a6c.png)

  * #### Caso "Selecione modo de jogo" esteja desativado, no lugar aparecerá "Modo de jogo já selecionado".
    ![image](https://user-images.githubusercontent.com/85710199/176278187-b0d2c76d-80a5-4c6a-8b27-7bcfef7f16dc.png)

* ### Escolha de campeões e quem banir
  * #### Basta preencher os campos e clicar no botão "Iniciar BOT".
    ![image](https://user-images.githubusercontent.com/85710199/176280311-18a861d1-c251-4c5d-ab7d-10ffa605feef.png)

  * #### Pode ser deixado em branco, porém, após encontrar partida o bot não escolherá campeões ou banirá.

* ### Início do bot
   #### Após clicar em "Iniciar Bot", o bot começará a fazer tudo sozinho, como dito anteriormente, após o início não é recomendado ficar mexendo no mouse.
  
## Funcionalidades
* #### Abre o jogo (caso não esteja aberto)
* #### Seleciona o modo de jogo que foi pré selecionado pelo o usuário. (caso usuário ainda selecionou)
* #### Escolhe as lanes no saguão que foram pré selecionadas. (caso ainda não foram escolhidas)
* #### Fica em modo monitoramento, esperando uma partida ser encontrada para aceitar
* #### Após aceitar, bane o campeão pré estabelecido pelo usuário.
* #### Seleciona a 1° opção de campeão,se ele não for banido, caso isso aconteça o bot selecionará a 2° opção fornecida.
* #### Após início da partida o bot fechará automaticamente

## Ferramentas e bibliotecas utilizadas
* Python 3
  * pyautogui
  * opencv-python
  * cx_freeze
  * webbrowser
  * pygetwindow
