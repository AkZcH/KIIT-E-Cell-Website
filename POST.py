from flask import Flask, request, jsonify
import joblib

model = joblib.load('C:\\Users\\KIIT0001\\Desktop\\Personal Vault\\Projects\\ML models\\IMDb Movie Reviews\\IMDb_movie_reviews\\movie_review_model.pkl')
vectorizer = joblib.load('C:\\Users\\KIIT0001\\Desktop\\Personal Vault\\Projects\\ML models\\IMDb Movie Reviews\\IMDb_movie_reviews\\vectorizer.pkl')
scaler = joblib.load('C:\\Users\\KIIT0001\\Desktop\\Personal Vault\\Projects\\ML models\\IMDb Movie Reviews\\IMDb_movie_reviews\\scaler.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    # Preprocess the text
    text = data['text']
    features = vectorizer.transform([text]).toarray()
    features = scaler.transform(features)
    
    # Predict
    prediction = model.predict(features)
    label = 'Positive' if prediction[0] == 1 else 'Negative'
    
    return jsonify({'prediction': label})

if __name__ == '__main__':
    app.run(debug=True)



