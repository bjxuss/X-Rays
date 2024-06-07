import numpy as np


class Predict:

    def __init__(self, label:str):
        self.label = label

    def __str__(self) -> str:
        return f"Predict --> {self.value}" 