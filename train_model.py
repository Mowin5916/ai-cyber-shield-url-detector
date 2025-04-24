# train_model.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

# Step 1: Sample training data
urls = ["http://bad.com", "https://safe.org", "http://phishing.co"]
labels = ["malicious", "safe", "malicious"]

# Step 2: Encode the labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(labels)

# Step 3: Vectorize the URLs
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(urls)  # ✅ This fits the TF-IDF!

# Step 4: Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Step 5: Save all components
with open('phishing_url_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('tfidf_vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

print("✅ Model, Vectorizer, and Label Encoder saved successfully!")
