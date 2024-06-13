import os  # Biblioteca para trabajar con archivos y directorios
import torch  # Biblioteca para trabajar con redes neuronales
from PIL import Image  # Biblioteca para trabajar con imágenes
import cv2  # Biblioteca para trabajar con imágenes
from PIL import ImageFile  # Biblioteca para trabajar con imágenes

import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'logic'))

from logic.Bones.config import get_device, get_model, get_transform, preprocess_image  
from entity.parametros import Parametro

class Predict(): 
    def __init__(self):
        self.device = get_device()
        self.model = get_model()
        self.model.load_state_dict(torch.load("data/BonesFracture/Modelos Entrenados/modelo6_full_100_epochs.pth", map_location=self.device))
        self.model.eval()  # Poner el modelo en modo evaluación

    def preparar_imagem(self, image_path):
        transform = get_transform()
        imagem = cv2.imread(image_path)  # Leer la imagen
        imagem = preprocess_image(imagem)  # Preprocesar la imagen
        imagem = Image.fromarray(imagem)  # Convertir la imagen al formato PIL
        imagem = imagem.convert('L')  # Convertir imagen a escala de grises (modo L)
        imagem = transform(imagem).unsqueeze(0)  # Aplicar transformaciones y agregar una dimensión
        return imagem.to(self.device)

    # Función para realizar una predicción en una imagen dada
    def predict_image(self, image_path):
        ImageFile.LOAD_TRUNCATED_IMAGES = True  # Cargar imágenes truncadas

        # Preparar la imagen
        image = self.preparar_imagem(image_path)

        # Realizar la predicción
        with torch.no_grad():
            outputs = self.model(image)
        _, predicted = torch.max(outputs, 1)

        return predicted.item()

