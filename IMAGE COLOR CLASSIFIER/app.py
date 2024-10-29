from flask import Flask, render_template, request
from PIL import Image
import os

app = Flask(__name__)

# Ensure the images directory exists
os.makedirs('./images', exist_ok=True)

def simple_classifier(image):
    """
    A simple mock classifier that returns a fake prediction based on image content.
    This is a placeholder function. You can implement a real classifier logic here.
    """
    # Example: Let's say we classify images by their average color
    avg_color = image.resize((1, 1)).getpixel((0, 0))
    if sum(avg_color) / 3 < 128:
        return 'Dark Image', 0.85  # Fake confidence
    else:
        return 'Light Image', 0.90  # Fake confidence

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    if 'imagefile' not in request.files:
        return render_template('index.html', prediction='No file uploaded.')

    imagefile = request.files['imagefile']

    if imagefile.filename == '':
        return render_template('index.html', prediction='No selected file.')

    image_path = os.path.join('./images', imagefile.filename)
    imagefile.save(image_path)

    try:
        # Load the image and convert to RGB
        image = Image.open(image_path).convert('RGB')

        # Classify the image
        classification, confidence = simple_classifier(image)

        prediction = f'{classification} ({confidence * 100:.2f}%)'
    except Exception as e:
        prediction = f'Error processing image: {str(e)}'

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
