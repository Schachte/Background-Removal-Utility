import os
import requests

# Your PhotoRoom API key
# Grab from https://www.photoroom.com/api/docs
API_KEY = '<GRAB API KEY FROM PHOTOROOM>'
IMAGE_DIRECTORY = './photos'

def remove_background(image_path):
    """
    Function to remove the background of an image using the PhotoRoom API.
    """
    with open(image_path, 'rb') as img_file:
        image_bytes = img_file.read()
    response = requests.post(
        'https://sdk.photoroom.com/v1/segment',
        headers={'x-api-key': API_KEY},
        files={'image_file': image_bytes},
    )
    response.raise_for_status()
    return response.content

def process_images(directory):
    """
    Function to process all .jpeg images in a directory.
    """
    for filename in os.listdir(directory):
        if filename.endswith('.jpeg'):
            image_path = os.path.join(directory, filename)
            print(f'Processing {image_path}...')
            image_without_bg = remove_background(image_path)
            new_filename = filename.replace('.jpeg', '_no_bg.jpeg')
            new_image_path = os.path.join(directory, new_filename)
            with open(new_image_path, 'wb') as f:
                f.write(image_without_bg)
            print(f'Saved new image to {new_image_path}')

process_images(IMAGE_DIRECTORY)