import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer

def cache():
    sample_X = [
    # Compliments (EN + HI)
    "I admire your skills",
    "You are awesome",
    "Great job",
    "You're amazing",
    "Tu bahut accha hai",
    "Tu talented hai",
    "Badiya kaam kiya",
    "Mast hai tu",

    # Toxic / insults (EN + HI slang)
    "You suck",
    "You are dumb",
    "Nobody likes you",
    "You are useless",
    "bhosdi ka",
    "madarchod",
    "chutiya",
    "gandu",
    "tu bekaar hai",
    "tu pagal hai",
    "bakchod",
    "faltu aadmi",

    # Greetings
    "Hello",
    "Hi",
    "Hey",
    "Good morning",
    "Good evening",
    "Namaste",
    "Namaskar",
    "Hi bhai",
    "Hello dost",
    "Kya haal hai",

    # Questions / casual
    "How are you?",
    "What's up?",
    "How's your day?",
    "Kya kar raha hai",
    "Kaisa hai",
    "Sab theek?",
    "Kya chal raha hai",
    "Tu kya kar raha hai",

    # Farewell
    "Bye",
    "Goodbye",
    "See you later",
    "Phir milte hain",
    "Chalta hoon",
    "Bye bhai",
    "Milte hain"
]
    sample_y = [
    # Compliments
    "Thanks",
    "Thanks",
    "Thanks",
    "Thanks",
    "Thanks",
    "Thanks",
    "Thanks",
    "Thanks",

    # Toxic → controlled response
    "Same to you",
    "Same to you",
    "Same to you",
    "Same to you",
    "Same to you",
    "Same to you",
    "Same to you",
    "Same to you",
    "Same to you",
    "Same to you",
    "Same to you",
    "Same to you",

    # Greetings
    "Hello!",
    "Hello!",
    "Hello!",
    "Good morning!",
    "Good evening!",
    "Namaste!",
    "Namaste!",
    "Hello!",
    "Hello!",
    "I'm good, how are you?",

    # Questions
    "I’m good, thanks",
    "Not much, you?",
    "Pretty good!",
    "Bas theek hoon",
    "Main theek hoon",
    "Haan sab badhiya",
    "Kuch khaas nahi",
    "Bas timepass",

    # Farewell
    "Bye!",
    "Goodbye!",
    "See you!",
    "Phir milenge",
    "Theek hai, bye",
    "Bye bhai",
    "Milte hain"
]

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(sample_X)

    encoder = LabelEncoder()
    y = encoder.fit_transform(sample_y)

    model = DecisionTreeClassifier()
    model.fit(X, y)

    joblib.dump(model, "model-cache/chat_model.pkl")
    joblib.dump(vectorizer, "model-cache/vectorizer.pkl")
    joblib.dump(encoder, "model-cache/encoder.pkl")

    print("✅ Cached successfully!")

if __name__ == "__main__":
    cache()