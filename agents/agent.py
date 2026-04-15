from models.bert_model import bert_predict

def agent_decision(text):
    result = bert_predict(text)

    if result == 1:
        return "Positive → Send Outreach Message"
    else:
        return "Negative → Do Not Send"