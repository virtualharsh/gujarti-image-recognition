# 📝 Gujarati Handwriting Recognition 

This project was developed as the final year diploma project in Computer Engineering. It involves building a machine learning pipeline to recognize handwritten Gujarati digits or characters using Convolutional Neural Networks (CNN) and a basic Neural Network (NN). The project covers the full pipeline: data preprocessing, augmentation, model training, and evaluation.

## 🔍 Objective
To build a robust image classification model that can recognize Gujarati handwritten characters or digits with high accuracy using custom image preprocessing and CNN/NN architectures.

## ⚙️ Technologies Used

- `Python` - for model building and preprocessing
- `Pillow` (PIL) - image loading and manipulation
- `NumPy` - array operations
- `TensorFlow / Keras` - for building and training models (assumed)
- `Goggle Colab` - model training & analysis

## 🧹 Preprocessing Pipeline

1. Balancing Classes (get_no_of_imgs.py)
    - Counts the number of images in each class
    - Calculates how many more images are needed per class to balance the dataset

2. Resizing & Grayscale Conversion (resize_imgs.py)
    - Resizes all images to 50x70 pixels
    - Converts to grayscale
    - Organizes into class-wise directories

3. Thresholding & Binarization (absolute_0-1_filtering.py)
    - Converts images to grayscale
    - Applies a binary threshold (e.g., pixels > 130 → white, else black)
    - Saves cleaned images for further use

4. Augmentation (augment.py) 
    - Applies slight rotations to existing samples
    - Saves them as new images to increase data diversity

## 🔃 Preprocessing results

![Raw Image](/assets/image-1-raw.jpg) => ![Processed image](/assets/image-1-processed.jpg)


## 🧠 Model Architectures

1. `CNN` Model
    - Input shape: (50, 70, 1)
    - Multiple convolutional + max pooling layers
    - Dense layers for classification
    - Dropout regularization

2. Simple `Neural Network` (NN)
    - Input layer flattened from image
    - Dense layers with ReLU
    - Softmax output

## 📊 Results
- `Training Accuracy:` ~95% (CNN), ~80% (NN)
- `Test Accuracy:` ~90% (CNN), ~75% (NN)
- CNN outperformed NN significantly due to its capability to extract spatial features.