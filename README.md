## OpenCV Object Counter
Projeto desenvolvido utilizando Python e OpenCV, divido em duas etapas. A primeira, sendo representada pela identificação de quantas galinhas estão presentes em uma seleção da imagem. Enquanto, a segunda etapa refere-se a identificação de bolas de bocha, e contagem das mesmas.

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
- **Em desenvolvimento**

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