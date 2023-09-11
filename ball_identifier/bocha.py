import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('../assets/bocha.JPG')

# Inicializar a flag para controlar as etapas de detecção de círculos
etapa_deteccao = 'threshold'

# Definir cores das bolas
cores_bolas = ['azul', 'vermelho', 'branca']

# Função para alternar a etapa de detecção de círculos
def alternar_etapa_deteccao():
    global etapa_deteccao
    if etapa_deteccao == 'threshold':
        etapa_deteccao = 'adicao'
    elif etapa_deteccao == 'adicao':
        etapa_deteccao = 'subtracao'
    elif etapa_deteccao == 'subtracao':
        etapa_deteccao = 'multiplicacao'
    elif etapa_deteccao == 'multiplicacao':
        etapa_deteccao = 'deteccao'
    elif etapa_deteccao == 'deteccao':
        etapa_deteccao = 'threshold'
    else:
        etapa_deteccao = 'threshold'

# Função para aplicar a etapa de processamento especificada
def aplicar_etapa_processamento(imagem, etapa):
    if etapa == 'threshold':
        # Converter a imagem para tons de cinza
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        # Aplicar threshold para segmentar as bolas
        _, resultado = cv2.threshold(imagem_cinza, 200, 255, cv2.THRESH_BINARY)
        return resultado
    elif etapa == 'adicao':
        return cv2.add(imagem, imagem)
    elif etapa == 'subtracao':
        return cv2.subtract(imagem, cv2.bitwise_not(imagem))
    elif etapa == 'multiplicacao':
        return cv2.multiply(imagem, cv2.bitwise_not(imagem))

# Função para detectar círculos na imagem de uma cor específica
def detectar_circulos_cor(imagem, cor):
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagem_circulos = imagem.copy()
    limite_inferior = None
    limite_superior = None

    if cor == 'azul':
        limite_inferior = np.array([90, 50, 50])
        limite_superior = np.array([130, 255, 255])
    elif cor == 'vermelho':
        limite_inferior1 = np.array([0, 50, 50])
        limite_superior1 = np.array([10, 255, 255])
        limite_inferior2 = np.array([160, 50, 50])
        limite_superior2 = np.array([180, 255, 255])
        mascara1 = cv2.inRange(imagem, limite_inferior1, limite_superior1)
        mascara2 = cv2.inRange(imagem, limite_inferior2, limite_superior2)
        mascara = cv2.add(mascara1, mascara2)
    elif cor == 'branca':
        limite_inferior = np.array([200, 200, 200])
        limite_superior = np.array([255, 255, 255])

    if cor == 'vermelho':
        circulos = cv2.HoughCircles(mascara, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                                    param1=50, param2=30, minRadius=0, maxRadius=0)
    else:
        circulos = cv2.HoughCircles(imagem_cinza, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                                    param1=50, param2=30, minRadius=0, maxRadius=0)

    if circulos is not None:
        circulos = np.uint16(np.around(circulos))
        for i in circulos[0, :]:
            centro = (i[0], i[1])
            raio = i[2]
            cv2.circle(imagem_circulos, centro, raio, (0, 255, 0), 2)

    return imagem_circulos

while True:
    imagem_etapa = aplicar_etapa_processamento(imagem, etapa_deteccao)

    # Converter a imagem de efeito para BGR (3 canais) para concatenação
    if len(imagem_etapa.shape) == 2:
        imagem_etapa = cv2.cvtColor(imagem_etapa, cv2.COLOR_GRAY2BGR)

    imagem_concatenada = np.hstack((imagem, imagem_etapa))

    cv2.imshow('Efeito e Etapa Atual', imagem_concatenada)

    # Aguardar pela tecla ENTER
    tecla = cv2.waitKey(0)
    if tecla == 13:  # Código da tecla ENTER
        alternar_etapa_deteccao()
    elif tecla == 27:  # Código da tecla ESC para sair
        break

# Mostrar etapas de detecção das cores uma de cada vez
for cor in cores_bolas:
    imagem_etapa = aplicar_etapa_processamento(imagem, 'threshold')
    imagem_concatenada = np.hstack((imagem_etapa, detectar_circulos_cor(imagem, cor)))

    cv2.imshow(f'Efeito e Deteccao de Bolas {cor.capitalize()}', imagem_concatenada)
    cv2.waitKey(0)

cv2.destroyAllWindows()
