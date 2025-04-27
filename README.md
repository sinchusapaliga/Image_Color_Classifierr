# Image_Color_Classifierr

The Image Color Classifier is a web application built with Flask that classifies images based on their dominant color. It utilizes the Pillow library for image processing and provides a simple user interface for uploading images. The classifier currently uses a mock algorithm to demonstrate the functionality, which can be replaced with a real machine learning model.

# Features
Upload an image file for classification.
Classifies images as either "Dark Image" or "Light Image" based on the average color.
Displays classification results with confidence scores.
User-friendly interface for easy interaction.

# Installation
# Clone the repository:
bash
git clone https://github.com/yourusername/image-color-classifier.git
cd image-color-classifier

# Install the required packages:
bash
pip install Flask Pillow

# Run the application:
bash
python app.py
# Open a web browser and go to 
http://localhost:3000.

Upload an image using the provided form.
View the classification result displayed on the page.

# Code Structure
app.py: Main application file containing the Flask app and classifier logic.
templates/index.html: HTML template for the user interface.
images/: Directory for storing uploaded images (created automatically).
