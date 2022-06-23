from PIL import Image  
image = Image.open(r"tree.jpg")  
r, g, b = image.split()  
image.show()  
image = Image.merge("RGB", (b, g, r))  
image.show()  