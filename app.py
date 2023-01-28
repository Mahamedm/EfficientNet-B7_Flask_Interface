from keras.applications.efficientnet import preprocess_input, decode_predictions
from keras.applications.efficientnet import EfficientNetB7
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image
import numpy as np
import base64

app = Flask(__name__)

def predict(image_path):
    # EfficientNet-B7 model pre-trained on ImageNet
    model = EfficientNetB7(weights='imagenet')
    img = image_path.convert("RGB")

    # Resize the image to 600x600
    img = img.resize((600, 600))
    x = np.array(img)
    x = np.reshape(x, (1, 600, 600, 3))

    # Preprocess the image for the model
    x = preprocess_input(x)

    # Run the image through the model and decode the predictions
    preds = model.predict(x)
    
    # Top 3 predictions 
    pred_labels = decode_predictions(preds, top=3)[0]

    # list of the predictions
    return_list = []
    for pred in pred_labels:
        return_list.append(f"{pred[1]}, accuracy: {str(pred[2])}")
    return return_list

@app.route('/')
def index():
    # Main page with image upload
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    #  Get the file from post request
    file = request.files['image']
    img = Image.open(file.stream)  # PIL image

    width, height = img.size
    prediction = predict(img) # predict function

    # Plot the image and predictions using matplotlib
    plt.imshow(img,aspect='auto')
    
    # Set the background color to grey (there are better ways to do this)
    plt.gcf().set_facecolor("grey")
    plt.title('Analysed Image', color='white', bbox=dict(facecolor='Grey', alpha=0.0))
    for pred in prediction:
        plt.text(width, height, "", fontsize=10)
    
    # Save the plot to a buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Embed the result in the html output using base64 encoding for the image
    image_base64 = base64.b64encode(buf.getvalue()).decode()
    return render_template('index.html', predictions=prediction, image=image_base64)

if __name__ == '__main__':
    app.run(debug=True)