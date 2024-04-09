from flask import Flask, request, jsonify
from model import load_model, predict

app = Flask(__name__)

# Load the model
model = load_model()

@app.route('/predict', methods=['POST'])
def prediction():
    if request.method == 'POST':
        # Get the image data from the request
        image = request.files['image']
        
        # Make predictions
        result = predict(image, model)
        
        # Return the prediction result
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
