import cv2
import chicken_count 

start_x, start_y, end_x, end_y = -1, -1, -1, -1
selecting = False
reg_of_image = None

image_path = "../assets/galinha.png"

def draw_rectangle(event, x, y, flags, param):
    global start_x, start_y, end_x, end_y, selecting, reg_of_image

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
            reg_of_image = (start_x, start_y, end_x, end_y)
            show_reg_of_image_window()

def copy_region(image):
    global reg_of_image
    if reg_of_image is not None:
        x1, y1, x2, y2 = reg_of_image
        converted_image = image[y1:y2, x1:x2]
        return converted_image
    return None

def show_reg_of_image_window():
    global reg_of_image
    if reg_of_image is not None:
        converted_image = copy_region(cv2.imread(image_path))
        if converted_image is not None:
            channel = converted_image[:, :, 2]
            pink_image = cv2.applyColorMap(channel, cv2.COLORMAP_BONE)

            _, thresholding = cv2.threshold(pink_image, 148, 255, cv2.THRESH_BINARY)

            gray2 = cv2.cvtColor(thresholding, cv2.COLOR_BGR2GRAY)

            _, binary_image = cv2.threshold(gray2, 128, 255, cv2.THRESH_BINARY)

            edges = cv2.Canny(binary_image, 100, 200)

            cv2.imshow("Etapa 1: ColorMap Bone", pink_image)
            cv2.imshow("Etapa 2: Threshold (128)", thresholding)
            cv2.imshow("Etapa 3: GreyTones 2", gray2)
            cv2.imshow("Etapa 4: Threshold 2 (1)", binary_image)
            cv2.imshow("Etapa 5: Canny (128, 200)", edges)

            num_chicken = chicken_count.count_chicken(edges)

            print(f"Quantidade de Galinhas na Selecao: {num_chicken}")

            cv2.waitKey(0)
            cv2.destroyAllWindows()
