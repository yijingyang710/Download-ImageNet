# Download-ImageNet
Download specific classes of images from ImageNet1K

Reference:

Thanks to the contribution of Sebastian Norena on Medium: https://medium.com/coinmonks/how-to-get-images-from-imagenet-with-python-in-google-colaboratory-aeef5c1c45e5 

Before you start, you need to create an account on http://image-net.org/download-images. After you get the permission, download the list of WordNet IDs for your task. Once you've get a .txt file containing the wordnet id, you are ready to run main.py. You can adjust the number of images per class based on your needs.

Note that the images are automatically resized into 224x224. To remove that resizing, or implement other types of preprocessing, simply adjust the code in LINE #40.
