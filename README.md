# EfficientNet-B7 Flask Interface
This project is a simple image classifier that uses a pre-trained model to predict the contents of an image with Flask as the interface.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes using the Flask framework.

## Prerequisites
- Python 3.x (Used 3.9.0)
- Tensorflow 2.x 
- Keras 2.x 
- Matplotlib
- Numpy
- PIL

## Installing:
##### Without [Google Colab Notebook](https://colab.research.google.com/notebook):
- Clone the repository to your local machine.
- Create a virtual environment and activate it *(using virtualenv or conda)*.
#### Setup:
- Install the required packages using `pip install -r requirements.txt`
- Run the script using python app.py `python app.py`
- Post file via the local-page on port 5000 or Input the path of the image you want to classify

## Built With:
[Tensorflow](https://www.tensorflow.org/) - The deep learning framework used.<br>
[Keras](https://keras.io/) - The high-level neural networks API.

## Additional Resources
- [Keras documentation](https://keras.io/)
- [Tensorflow documentation](https://www.tensorflow.org/api_docs/python/tf/all_symbols)
- [Pillow documentation](https://pillow.readthedocs.io/en/stable/)
- [Matplotlib documentation](https://matplotlib.org/3.3.3/contents.html)


## Troubleshooting
- If you encounter the error Attribute `size` of `JpegImageFile` objects is not writable, make sure you have the latest version of PIL installed.
- If you have any other issues or questions, feel free to open an issue on the repository.

## Acknowledgments:
- The pre-trained model used in this project was trained on the [ImageNet](https://image-net.org/) dataset.
- The script is based on the [Keras documentation](https://keras.io/examples/vision/image_classification_from_scratch/) example.
