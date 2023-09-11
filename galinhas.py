import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tempfile
import os

# Variáveis globais
start_x, start_y, end_x, end_y = -1, -1, -1, -1
selecting = False
image_path = "assets/galinha.png"
roi = None

# Função de callback para lidar com eventos de mouse
def draw_rectangle(event, x, y, flags, param):
    global start_x, start_y, end_x, end_y, selecting, roi

    if event == cv2.EVENT_LBUTTONDOWN:
        start_x, start_y = x, y
        end_x, end_y = x, y
        selecting = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if selecting:
            end_x, end_y = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        selecting = False
        if start_x != end_x and start_y != end_y:
            roi = (start_x, start_y, end_x, end_y)
            show_roi_window()

# Função para copiar a Reg dentro do retângulo
def copy_region(image):
    global roi
    if roi is not None:
        x1, y1, x2, y2 = roi
        roi_image = image[y1:y2, x1:x2]
        return roi_image
    return None

# Função para mostrar a ROI em uma janela separada com filtros
def show_roi_window():
    global roi
    if roi is not None:
        roi_image = copy_region(cv2.imread(image_path))
        if roi_image is not None:

            channel = roi_image[:, :, 2]
            pink_image = cv2.applyColorMap(channel, cv2.COLORMAP_BONE)

            _, thresholding = cv2.threshold(pink_image, 148, 255, cv2.THRESH_BINARY)

            gray2 = cv2.cvtColor(thresholding, cv2.COLOR_BGR2GRAY)

            # blurred2 = cv2.GaussianBlur(gray2, (5, 5), 2)

            _, binary_image = cv2.threshold(gray2, 128, 255, cv2.THRESH_BINARY)

            # Aplicar o filtro Canny para detecção de bordas
            edges = cv2.Canny(binary_image, 100, 200)

            # Criar janelas separadas para as três imagens
            cv2.imshow("Etapa 1: ROI", pink_image)
            cv2.imshow("Etapa 3: Threshold (128)", thresholding)
            cv2.imshow("Etapa 4: GreyTones 2", gray2)
            cv2.imshow("Etapa 6: Threshold 2 (1)", binary_image)
            cv2.imshow("Etapa 7: Canny (128, 200)", edges)

            # Conte o número de galinhas com base nos contornos da imagem Canny
            num_galinhas = count_galinhas(edges)

            # Imprima o número de galinhas no console
            print(f"Quantidade de Galinhas na ROI: {num_galinhas}")

            cv2.waitKey(0)
            cv2.destroyAllWindows()

def count_galinhas(image, min_area=10):
    if image is not None:
        contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Filtrar contornos por área mínima
        valid_contours = [contour for contour in contours if cv2.contourArea(contour) >= min_area]

        num_galinhas = len(valid_contours)
        return num_galinhas

    return 0


# Carregar a imagem
img = cv2.imread(image_path)

# Verificar se a imagem foi carregada corretamente
if img is None:
    print("Erro ao carregar a imagem.")
    exit()

# Nome da janela
cv2.namedWindow('Galinha')

# Configurar o callback do mouse
cv2.setMouseCallback('Galinha', draw_rectangle)

while True:
    img_copy = img.copy()

    # Desenhar o retângulo na cópia da imagem
    if selecting:
        cv2.rectangle(img_copy, (start_x, start_y), (end_x, end_y), (0, 0, 255), 2)

    # Exibir a imagem com o retângulo
    cv2.imshow('Galinha', img_copy)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()
