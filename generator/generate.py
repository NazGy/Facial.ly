import json

# Function to call to API and return image
def get_image(key):
    return NotImplemented

# Funtion to process and save image
def save_image(image):
    return NotImplemented

def use_mock():
    with open('./generator/mock.json') as f:
        data = json.load(f)
        return data

# Starts Generator
def generate():
    keys = ['vD-S_Wb8gXcuIgRgHypFdw'] # A list of keys
    print(use_mock())
    # for key in keys:
    #     for i in range(0, 500):
    #         image = get_image(key)
    #         save_image(image)

generate()
