## OpenCV Object Counter
Este repositório contém um conjunto de scripts e recursos para a detecção de objetos utilizando a poderosa combinação de Python e OpenCV. O projeto é dividido em duas etapas distintas, cada uma focada na identificação de objetos específicos.

Na primeira etapa, foi utilizado técnicas de processamento de imagem com OpenCV para identificar galinhas em imagens. As etapas incluem thresholding para segmentar a área de interesse das galinhas, Canny Edge Detection para realçar bordas importantes, blur para suavizar a imagem e remover ruídos, e Colormap "BONE" para uma representação visual mais clara.

Na segunda etapa do projeto, a ênfase é na detecção de bolas de bocha em várias cores e geração de círculos ao redor delas. Isso é alcançado por meio de técnicas, incluindo combinação de imagens para criar imagens que realcem os objetos de interesse, thresholding para segmentar as bolas de bocha, e adição, subtração e multiplicação de imagem para criar máscaras precisas.

## Sobre o trabalho:

* Disciplina: OP63I-CC8 - Processamento De Imagens E Reconhecimento De Padrões	
* Turma: 2023/2 - 8º Período
* Docente: Pedro Luiz de Paula Filho

## Recursos 
##### Etapa 1:
- **Seleção da Área para Análise:** O usuário pode clicar e arrastar dentro da janela criada para a imagem, escolhendo o lugar que receberá a contagem de galinhas.
- **Visualização das Etapas:** Após selecionar a área de análise, a aplicação devolverá 5 telas:
    1. A área selecionada convertida para o COLORMAP_BONE;
    2. A imagem gerada pelo COLORMAP_BONE com um Threshold Inverso, com peso de 108;
    3. A imagem do Threshold Inverso para Tons de Cinza;
    4. A imagem de Tons de Cinza convertida para Threshold com peso de 128;
    5. Por fim é feito a conversão de Threshold para Canny, entre os limiares de 100 e 200.
- **Contagem das Galinhas:** A contagem é feita utilizando o método findContours do OpenCV.

##### Etapa 2:
- **Identificação de Bolas:** A aplicação é capaz de identificar bolas e circular sua área para as cores branco, azul e vermelho.
- **Visualização das Etapas:** Após carregar a imagem, a aplicação executa mostrando na tela as seguintes etapas:
    1. Aplica Threshold na imagem original e mostra o resultado;
    2. Faz o contorno da única bola que sobrou com a aplicação do Threshold (branca);
    3. Passa o filtro de adição na imagem com a bola branca identificada, somando com a imagem original novamente;
    4. Aplica um Threshold Inverso e mais fraco que o primeiro, deixando na imagem apenas as 4 bolas restantes e o circulo da bola branca;
    5. Mostra na tela o resultado com os 5 circulos ao redor das bolas.

## Dependências
Siga essa ordem de instalação para ambos os sistemas operacionais, para garantir que não exista conflito de versões:

### Para o Linux:
1. Python 3 `pip install python3`
2. OpenCV (cv2) `pip install opencv-python`

### Para o Windows:
1. Python 3.11.5 ([Instalador 64-bit](https://www.python.org/downloads/windows/))
2. OpenCV `pip install opencv-python`

## Como Utilizar

1. Clone o repositório do GitHub: `git clone https://github.com/thiagodalsanto/opencv-object-counter.git`
2. Instale as [dependências](#dependências) utilizadas.
3. Execute o aplicativo em uma IDE com o comando => para Linux: `python3 main.py` e para Windows: `python main.py` 

## Imagens do Aplicação

##### Etapa 1:

Imagem 1 - Teste em uma região com alta intensidade de luz, com 4 galinhas presentes e 4 galinhas identificadas.
![Imagem1](https://i.imgur.com/Kfnj9Yp.png)

Imagem 2 - Teste em uma região com média intensidade de luz, com 2 galinhas presentes e 2 galinhas identificadas.
![Imagem2](https://i.imgur.com/QRCz5Yh.png)  

PS.: Para regiões mais escuras da imagem, a aplicação tende a contar um número menor de galinhas.

##### Etapa 2:

Imagem 1 - Etapas da aplicação demonstrando seu funcionamento da direita para a esquerda.
![Imagem1](https://i.imgur.com/rStcN1u.png)

Imagem 2 - Imagem resultante com os circulos ao redor das bolas de bocha, comparando com a imagem original.
<p align="center">
    <img src="https://i.imgur.com/zsPGJmG.jpg"><img src="https://i.imgur.com/22NkMao.jpg">
</p>
