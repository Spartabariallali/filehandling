class TextFileHandling:

    def __init__(self,file_path,text_storage=None):
        self.file_path = file_path
        self.text_storage = text_storage

    # read in two ways and write in two ways

    # def readTextFile(self):
    #     #open file
    #     try:
    #         file=open(self.file_path,"r")
    #     except Exception as e:
    #         print(e)
    #     else:
    #         #read the file 
    #         self.text_storage=file.read()
    #         self.text_storage=file.readline()
    #         self.text_storage=file.readlines()
    #         print(file.tell())
    #         print(file.read(1))
    #         print(file.tell())
    #         file.seek(0)
    #         # self.text_storage=file.read(3)
    #         #close the file 
    #        return self.text_storage
    #     finally: 
    #             file.close()
    #             print("always run")
       
        

    def writeTextfile(self):
        # open, write, close
        file=open("writer.txt", "w") # "w" write two arguments - one is the file and other is made
        file.write("My first python created")
        file.close()
        file = open("writer.txt", "a+") # "a" append, "a+" appends and read
        file.write("\n I am overriding the file") # append mode
        file.seek(0)
        self.text_storage = file.read() # storing what I read from the file to the instance variable
        file.close() # gives status of closure
        print(file.name) # gives you the name of the current file 
        print(file.mode)
        return self.text_storage
       

    def readTextFileUsingWith(self):
        # to reduce the overhead of closing files 
        with open("order.txt","r") as file:
            self.text_storage = file.read()
            return self.text_storage



    def writeTextFileUsingWith(self):
        with open("write.txt","w+") as file:
            file.write("using writer with functionality")
            print(file.tell())
            file.seek(0)
            self.text_storage=file.read()
            return self.text_storage
    
    
    def playingwihtPythonsOnMondule(self):
        import os 
        print(os.getcwd()) # prints current working directory 
        # os.remove("write.txt")
        print(os.listdir())
        # os.rename("order.txt","modified.txt")
        # os.open("modified.txt","r")
        os.mkdir("bari")


    def playingWithException(self):
        try:
            file=open(self.file_path, 'r')
        except FileNotFoundError as fnf:
            print(fnf)
            print("file unvailable")
        except Exception as e:
            print(e)
        else:
            self.text_storage.read()
            file_close()
        finally:
            print("will run for sure")
            return self.text_storage
        
    def raiseException(self):
        while True:
            try:
                firstvalue=input("please enter your name: ")
                if (len(firstvalue)) == 0:
                    raise Exception
            except Exception:
                print("please enter a valid name")
                self.raiseException()
        else:
            print(firstvalue + " thankyou for giving your name")
        
