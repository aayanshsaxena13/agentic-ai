# Import necessary modules here...
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib as jlb
import os
import json

# Clearly define app...
app = FastAPI()

origins = [
    "*" # as a dev resort...
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define all global dependancies here...
if os.path.exists("model-cache/mini-slm.pkl"):
    model = jlb.load("model-cache/mini-slm.pkl")
if os.path.exists("model-cache/vectorizer.pkl"):
    vectorizer = jlb.load("model-cache/vectorizer.pkl")
if os.path.exists("model-cache/encoder.pkl"):
    encoder = jlb.load("model-cache/encoder.pkl")

# Define the training and caching mechanism...
def cache() -> str:
    global model, vectorizer, encoder
    try:
        # Define raw mini-dataset clearly before preprocessing...
        with open("input/dataset.json", "r") as f:
            dataset = json.load(f)
            X_text = dataset["X_text"]
            y_text = dataset["y_text"]

        # Preprocess data before modelling takes place...
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(X_text).toarray()
        jlb.dump(vectorizer, "model-cache/vectorizer.pkl")

        encoder = LabelEncoder()
        y = encoder.fit_transform(y_text)
        jlb.dump(encoder, "model-cache/encoder.pkl")

        # Define and Train the model with the preprocessed data...
        model = GaussianNB()
        model.fit(X=X, y=y)
        jlb.dump(model, "model-cache/mini-slm.pkl")
        return "✅ Successfully trained Apple Intelligence Demo..."
    
    except Exception as e:
        print(f"❌ Something went wrong and needs fixing...{e}")

# Handle requests here...
@app.get("/")
def response():
    try:
        if not os.path.exists("model-cache/mini-slm.pkl") and not os.path.exists("model-cache/vectorizer.pkl") and not os.path.exists("model-cache/encoder.pkl"):
            cache()
            return {
                "msg": "✅ Successfully cached Apple Intelligence Demo SLM."
            }
        else:
            return {
                "msg": "💡 Already cached Apple Intelligence Demo SLM."
            }
    except Exception as e:
        return {
            "msg": f"Something went wrong...Reason: {str(e)}"
        }

@app.post("/predict")
def predict(text: str):
    try:
        # Translate input text for the model to understand...
        input_text = vectorizer.transform([text]).toarray()

        # Predict using the model here...
        prediction = model.predict(input_text)

        # Convert into natural language...
        response_text = encoder.inverse_transform(prediction.ravel())[0]

        return { 
            "input": text,
            "response": response_text
        }
    except Exception as e:
        return { 
            "msg": f"Model or vectorizer not loaded: {str(e)}"
        }

# Run using py -m fastapi dev app.py