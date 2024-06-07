import torch
from torchvision import datasets, transforms
import torch.nn as nn  # biblioteca para redes neuronales
import torch.optim as optim # biblioteca para optimizacion
import cv2  # biblioteca para vision computacional


def get_device(): # Verificar disponibilidad de GPU
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print("Usando GPU.")
    else:
        device = torch.device("cpu")
        print("Usando CPU.")
    return device


device = get_device()


def get_transform(): # Transformacion d epreprocesamiento de datos
    return transforms.Compose([
        # transforms.Resize((500, 500)),  # Redimensiona imagen para 500x500 pixels
        transforms.Resize((224, 224)),  # Redimensiona imagen para 224x224 pixels
        transforms.Grayscale(num_output_channels=1),  # Convierte a imagem para escala 
        transforms.ToTensor(),  # Converte a imagem para un tensor PyTorch
        transforms.Normalize((0.5), (0.5))  # Normaliza los valores de píxeles para que estén entre -1 y 1
    ])


def get_model(): # Arquitectura de red neuronal
    return nn.Sequential(
        nn.Conv2d(1, 16, 3),
        nn.ReLU(),
        nn.MaxPool2d(2, 2),
        nn.Conv2d(16, 32, 3),
        nn.ReLU(),
        nn.MaxPool2d(2, 2),
        nn.Flatten(),
        # Ajustar el tamaño de entrada lineal según el tamaño de la imagen
        nn.Linear(32 * 54 * 54, 128), # Se for 224x224
        # nn.Linear(32 * 123 * 123, 128), # se for 500x500
        nn.ReLU(),
        nn.Linear(128, 2)
    ).to(device)


def get_criterion():
    return nn.CrossEntropyLoss() # Función de pérdida


def get_optimizer(model):
    return optim.Adam(model.parameters(), lr=0.001) # Optimizador


def preprocess_image(imagem): # Preprocesamiento de imágenes
    img_suavizada = cv2.GaussianBlur(imagem, (13, 13), 3)  # 13x13 es el tamaño del grano y 3 es la desviación estándar
    img_detalhes = 3 * cv2.subtract(imagem, img_suavizada)  # 3 es el factor de mejora
    img_realcada = cv2.add(imagem, img_detalhes)  # Agrega detalles a la imagen original.
    return img_realcada




