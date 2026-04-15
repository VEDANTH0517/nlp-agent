from transformers import pipeline

# Load pretrained sentiment model
classifier = pipeline("sentiment-analysis")

def bert_predict(text):
    result = classifier(text)[0]

    if result['label'] == 'POSITIVE':
        return 1
    else:
        return 0