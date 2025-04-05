import spacy

nlp = spacy.load("en_core_web_sm")

def parse_cv(cv_text):
    doc = nlp(cv_text)
    skills = [ent.text for ent in doc.ents if ent.label_ in ["SKILL", "ORG", "WORK_OF_ART"]]
    return " ".join(set(skills))
