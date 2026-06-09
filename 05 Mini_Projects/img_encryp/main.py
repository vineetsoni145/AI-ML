from task1 import imge
from PIL import Image
import numpy as np

data = imge()

modified = np.clip(data * 6,).astype(np.uint8)

output = Image.fromarray(modified)
output.save("modified_image.jpg")

print("Image saved successfully!")