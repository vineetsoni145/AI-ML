from PIL import Image
import numpy as np

def imge():
    img = Image.open("static/gaming.jpg")
    return np.array(img)