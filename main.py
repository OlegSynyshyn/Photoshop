from PIL import Image, ImageFilter

# 
class ImageEditor:
    def __init__ (self, filename):
        self.filename = filename
        self.original = None
        self.changed = []
    
    def open(self):
        try:
            
            self.original = Image.open(self.filename)
            self.original.show()
        except:
            print('File is not found')

    def do_left(self):
        rotate = self.original.transpose(Image.ROTATE_90)


        self.changed.append(rotate)
        rotate.show()
        rotate.save("rotated_left.jpg")
    def do_right(self):
        rotate = self.original.transpose(Image.ROTATE_270)


        self.changed.append(rotate)
        rotate.show()
        rotate.save("rotated_right.jpg")

    def mirror(self):
        rotate = self.original.transpose(Image.FLIP_LEFT_RIGHT)


        self.changed.append(rotate)
        rotate.show()
        rotate.save("mirrored.jpg")
img1 = ImageEditor("sadowiy.jpg")
img1.open()
# img1.do_left()
# img1.do_right()
img1.mirror()