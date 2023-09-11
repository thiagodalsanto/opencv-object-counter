import cv2
import numpy as np

image = cv2.imread('../assets/bocha.JPG')
cv2.imshow('Imagem Original', image)
cv2.waitKey(0)

image_with_white = image.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresholded = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
cv2.imshow('Imagem Threshold', thresholded)
cv2.waitKey(0)

borders, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for border in borders:
    if cv2.contourArea(border) > 100:
        (x, y, w, h) = cv2.boundingRect(border)
        cv2.circle(image_with_white, (int(x + w / 2), int(y + h / 2)), int(w / 2), (0, 255, 0), 2)

cv2.imwrite('bola_branca_circulo.jpg', image_with_white)

image2 = cv2.imread('../assets/bocha.JPG')
add_image = cv2.add(image, image2)

for border in borders:
    if cv2.contourArea(border) > 100:
        (x, y, w, h) = cv2.boundingRect(border)
        cv2.circle(add_image, (int(x + w / 2), int(y + h / 2)), int(w / 2), (0, 255, 0), 2)

cv2.imshow('Imagem com Adicao', add_image)
cv2.waitKey(0)

gray_add_image = cv2.cvtColor(add_image, cv2.COLOR_BGR2GRAY)
ret, thresholded_add_image = cv2.threshold(gray_add_image, 164, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Imagem com Threshold e Adicao ', thresholded_add_image)
cv2.waitKey(0)

blurred_add_image = cv2.GaussianBlur(thresholded_add_image, (5, 5), 0)

borders_add_image, _ = cv2.findContours(thresholded_add_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for border in borders_add_image:
    if cv2.contourArea(border) > 100:
        (x, y, w, h) = cv2.boundingRect(border)
        cv2.circle(add_image, (int(x + w / 2), int(y + h / 2)), int(w / 2), (0, 0, 255), 2)

cv2.imwrite('bolas_azuis_vermelhas_circulo.jpg', add_image)

black_areas = cv2.bitwise_not(blurred_add_image)
borders_black, _ = cv2.findContours(black_areas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for border in borders_black:
    (x, y, w, h) = cv2.boundingRect(border)
    cv2.rectangle(add_image, (x, y), (x + w, y + h), (0, 0, 0), 2)

cv2.imshow('Imagem com Circulos na Adicao e Regioes Pretas', add_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
