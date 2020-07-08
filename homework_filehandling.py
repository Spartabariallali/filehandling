# 1.
# Accept from the user some text.Ensure user enters something else raise an
# exception.
# After that# write#that# text# to# a file and then read
# from this file to write# to another file simultaneously
# 2.
# Reading an image to writing to another file simultaneously

# class UserName:
#     while True:
#             try:
#                 firstvalue=input("please enter your name: ")
#                 if (len(firstvalue)) == 0:
#                     raise Exception
#             except Exception:
#                 print("please enter a valid name")
#                 self.raiseException() 
#             else:
#                 print(firstvalue + "thankyou for giving your name")
# user_one = UserName()

mike_tyson = 'mike_tyson.jpg'

class fileHandling:
    def __init__(self, text_storage=None):
        self.text_storage = text_storage

    def user_input(self):
        try:
            name = input("Enter your name: \n")
            if len(name) == 0:
                raise Exception
        except Exception:
            print("please enter a valid name(at least one letter)")
            self.user_input()
        else:
            print("thank you, your name has been registed {}".format(name))

    def readtext(self):

        try:
            user_input = input("please leave a message: \n")
            if len(user_input) == 0:
                raise Exception
        except Exception:
            print("please enter a message --> at least one character")
            self.readtext
        else:
            with open("message.txt","w+") as file:
                file.write(user_input)
                file.seek(0)
                self.text_storage = file.read()
            with open("message2.txt","w") as file:
                file.write(self.text_storage)
                return self.text_storage

    def readimage(seld):

        with open(mike_tyson,'rb') as image_file: # reading it as bytes rb = read_bytes
            image_string = image_file.read()
            with open("file location.png","wb") as dest_image:
                dest_image.write(image_string) # writing the top two lines into the bottom two lines 



obj1 = fileHandling()
 
# obj1.user_input()
# obj1.readtext()

obj1.readimage()