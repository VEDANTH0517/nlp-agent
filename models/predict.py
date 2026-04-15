import pickle
from preprocessing.text_cleaning import clean_text

model = pickle.load(open("models/model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

def predict(text):
    text = clean_text(text)
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]