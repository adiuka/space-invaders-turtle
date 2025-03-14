from PIL import Image

def image_resizer(image):
    """Used to resize transparent gif images"""
    img = Image.open(image)

    img = img.resize((25, 25))

    img.save(image)

    print("Image Resized Correctly")



#image_resizer("assets/invader2.gif")