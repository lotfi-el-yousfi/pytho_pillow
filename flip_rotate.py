# import  image module  
from PIL import Image  
  
# Open an already existing image and create image object  
imageObject = Image.open(r'tree.jpg')  
  
# perform a flip of left and right  
hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)  
  
# display the original image  
imageObject.show()  
  
# display the horizontal flipped image  
hori_flippedImage.show()  