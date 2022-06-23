from PIL import Image, ImageFilter  
#Open image  
Original_Image = Image.open(r"tree.jpg")  
Original_Image.show()  
  
# Applying simple blur function  
blur_Image = OriImage.filter(ImageFilter.BLUR)  
blur_Image.show()  