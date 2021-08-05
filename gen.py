from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def textOnImg(text,color,tcolor):
    #to calculate the what the width of the image should be based on the text
    fake_img = Image.new('RGB',(1080,1080),'white')
    fontObj = ImageFont.truetype("Roboto-Light.ttf",25)
    fake_draw = ImageDraw.Draw(fake_img)
    BG_W,BG_H = fake_draw.textsize(text,fontObj) #get the text dimensions to use on the real img

    #real image...
    real_img = Image.new('RGB',(BG_W+20,BG_H+20),color)
    real_draw = ImageDraw.Draw(real_img)
    fontObj = ImageFont.truetype("Roboto-Light.ttf",25)

    #add text + save
    real_draw.text((10,10), text, tcolor, font=fontObj)
    real_img.save('overlay.jpg')



if __name__ == "__main__":

    text = input("Enter Text: ")
    color = input("Enter Image Color: ")
    tcolor = input("Enter Text Color: ")

    textOnImg(text,color,tcolor)

    