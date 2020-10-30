# Capcha module is used to convert our text to image
from captcha.image import ImageCaptcha

# PIL module is used to show our captcha image
from PIL import Image

# Captcha variable is used to take input text 
Captcha=input("Enter captcha : ")

# Form variable is used to take name of image
Form=input("Enter name of Image : ")

# image variable is used to give dimentions to image and creating object of captcha.image
image = ImageCaptcha(width = 280, height = 90)

# Here write function is used to assemble our text into image
image.write(Captcha, Form )

# im is a object of PIL module used to open image
im=Image.open(Form)

# we use show image to view captcha
im.show()