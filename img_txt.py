import base64
  
def txtconvert():  
    with open(r"D:\image\aes_gui_trail.png", "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())  
    with open(r"D:\image\gui_trail.txt" ,"wb") as file:
        file.write(converted_string)