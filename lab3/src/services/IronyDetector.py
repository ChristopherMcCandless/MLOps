from transformers import AutoTokenizer, AutoModelForSequenceClassification
import numpy as np
from scipy.special import softmax


class IronyDetector:
    """
    Класс в котором инкапсулирована логика по настройке модели
    """

    @classmethod
    def init(self):
        model_id = "cardiffnlp/twitter-roberta-base-irony"
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_id)

    @classmethod
    def analyze(self, text_to_detect: str):
        labels = ["non-irony", "irony"]
        encoded_input = self.tokenizer(text_to_detect, return_tensors="pt")
        output = self.model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)

        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        rslt = {}
        for i in range(scores.shape[0]):
            lb = labels[ranking[i]]
            sc = scores[ranking[i]]
            rslt[lb] = np.round(float(sc), 3)
        return rslt
