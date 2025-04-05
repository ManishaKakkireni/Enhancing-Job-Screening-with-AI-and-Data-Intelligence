from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_match_score(jd_keywords, cv_keywords):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([jd_keywords, cv_keywords])
    return cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0] * 100
