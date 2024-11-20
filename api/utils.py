
import pickle
# from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import sklearn
print(sklearn.__version__)
vectorizer = joblib.load('api/model_weights/tfidf_vectorizer2.pkl')

with open('api/model_weights/random_forest_model.pkl', 'rb') as model_file:
    model_rf = pickle.load(model_file)

# with open('api/model_weights/tfidf_vectorizer1.pkl', 'rb') as vectorizer_file:
#     vectorizer = pickle.load(vectorizer_file)

def analyze_url(url):
    try:
        print(hasattr(vectorizer, "idf_"))
        print(vectorizer)
        print(url)
        # Preprocess the URL
        url_transformed = vectorizer.transform([url])
        # Make a prediction
        prediction = model_rf.predict(url_transformed)
        
        # Determine if it's phishing and return confidence
        is_phishing = prediction[0] == 0  # Assuming 0 means phishing
        confidence = model_rf.predict_proba(url_transformed)[0][1] if is_phishing else model_rf.predict_proba(url_transformed)[0][0]
        print(confidence)
        return {"is_phishing": is_phishing, "confidence": confidence, "success":True, "error":""}
    except Exception as e:
        print(e)
        return{"is_phishing": "", "confidence": -1, "success":False, "error":str(e)}
