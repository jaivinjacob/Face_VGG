from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

def load_model():
    # Load the trained model
    model = load_model('./models/vgg16_face_expression_model.h5')
    return model

def predict(image_file, model):
    # Load and preprocess the image
    img = image.load_img(image_file, target_size=(img_width, img_height))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    
    # Make predictions
    predictions = model.predict(img_array)
    
    # Process predictions
    # (You may need to adapt this depending on your model's output format)
    class_names = ['class1', 'class2', 'class3', 'class4', 'class5', 'class6']
    predicted_class = class_names[np.argmax(predictions)]
    
    return {'prediction': predicted_class}
