import cv2
import reg_of_selection
import chicken_count

# Nome da imagem
image_path = "../assets/galinha.png"

img = cv2.imread(image_path)

if img is None:
    print("Erro ao carregar a imagem.")
    exit()

cv2.namedWindow('Imagem Carregada')

cv2.setMouseCallback('Imagem Carregada', reg_of_selection.draw_rectangle)

while True:
    img_copy = img.copy()

    if reg_of_selection.selecting:
        cv2.rectangle(img_copy, (reg_of_selection.start_x, reg_of_selection.start_y), (reg_of_selection.end_x, reg_of_selection.end_y), (0, 0, 255), 2)

    # Exibir a imagem com o retângulo
    cv2.imshow('Imagem Carregada', img_copy)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()
