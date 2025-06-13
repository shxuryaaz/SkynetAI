import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text: str):
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])
