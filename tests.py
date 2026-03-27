import joblib

model = joblib.load("model-cache/chat_model.pkl")
vectorizer = joblib.load("model-cache/vectorizer.pkl")
encoder = joblib.load("model-cache/encoder.pkl")

print("🤖 Ready! Type 'exit' to quit.\n")

while True:
    text = input("You: ").strip()

    if text.lower() in ["exit", "quit"]:
        print("Bot: Bye 👋")
        break

    if not text:
        print("Bot: Say something 😄")
        continue

    vec = vectorizer.transform([text])
    pred = model.predict(vec)
    response = encoder.inverse_transform(pred)[0]

    print("Bot:", response)