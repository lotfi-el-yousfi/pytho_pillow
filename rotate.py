from PIL import Image  
#Open image using Image module  
im = Image.open(r"tree.pg")  
#Show actual Image  
im.show()  
#Show rotated Image  
imim = im.rotate(45)  
im.show()  