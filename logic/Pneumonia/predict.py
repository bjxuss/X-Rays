from logic.Pneumonia.config import get_model, prepare


class Predict2():
    def __init__(self):
        self.model = get_model()

    
    def predict_image(self, image_path):
        labels = ["NORMAL", "PNEUMONIA"]
        prepare_image = prepare(image_path)
        prediction = self.model.predict([prepare_image])
        final_prediction = labels[int(prediction.item(0))]
        return final_prediction


