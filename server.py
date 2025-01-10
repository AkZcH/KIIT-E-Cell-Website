from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    review = request.args.get('review', '') 
    response = {"message": "Received GET request", "review": review}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
