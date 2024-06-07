import os  # biblioteca para trabajar con archivos y directorios
import torch  # biblioteca para trabalhar com redes neuronales
from PIL import Image  # biblioteca para trabajar con imágenes
import cv2  # biblioteca para trabajar con imágenes
from PIL import ImageFile  # biblioteca para trabajar con imágenes
# import sys # biblioteca para trabajar con el sistema operativo
import matplotlib.pyplot as plt

import config


ImageFile.LOAD_TRUNCATED_IMAGES = True  # Cargar imágenes truncadas
transform = config.get_transform()
model = config.get_model()
diretorioValidacao = '../data/BonesFracture/Validacion' # Directorio de validación
model.load_state_dict(torch.load("../data/BonesFracture/Modelos Entrenados/modelo6_full_100_epochs.pth", map_location=torch.device('cpu')))
acertos = 0
erros = 0
model.eval()
model.state_dict()
device = config.device

# Función para realizar una predicción en una imagen dada
def predict_image(image_path):
    # Cargar la imagen y aplicar transformaciones
    image = Image.open(image_path)
    image = transform(image).unsqueeze(0)
    # Realizar la predicción
    with torch.no_grad():
        outputs = model(image)
    _, predicted = torch.max(outputs, 1)
    return predicted.item()

# # Ruta de la imagen que deseas predecir
# image_path = "/content/a00412f04.jpg"

# # Realizar la predicción en la imagen especificada
# prediction = predict_image(image_path)

def preparar_imagem(image_path):
    imagem = cv2.imread(image_path) # Lee la imagen
    imagem = config.preprocess_image(imagem) # Pre-procesar la imagen
    imagem = Image.fromarray(imagem) # Convertir la imagen al formato PIL
    imagem = imagem.convert('L')  # Convertir imagen a escala de grises (modo L)
    imagem = transform(imagem).unsqueeze(0) # Aplicar transformaciones y agregar una dimensión.
    return imagem

# Function to visualize sample images from a DataLoader
# def visualize_image(image, label):
#     image = Image.open(image)



#     # Mostrar la imagen
#     plt.imshow(image)
#     plt.axis('off')
#     plt.title(f'{label}')
#     plt.show()

# # Visualize batches

# visualize_image(image_path, f"La predicción es: {'Fracturada' if prediction == 0 else 'No fracturada'}")
