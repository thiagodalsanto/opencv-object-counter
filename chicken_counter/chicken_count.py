import cv2

def count_chicken(image, min_area=10):
    if image is not None:
        if len(image.shape) == 3 and image.shape[2] == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        valid_contours = [contour for contour in contours if cv2.contourArea(contour) >= min_area]

        num_chickens = len(valid_contours)
        return num_chickens

    return 0
