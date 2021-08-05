from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def textOnImg(text,color,tcolor,padding=20,font_name="Roboto-Light.ttf",font_size = 25,adjuster=.5,save_as="overlay.jpg",fk_img_dim=1080):
    """
    ...
    """
    #to calculate the what the width of the image should be based on the text
    fake_img = Image.new('RGB',(fk_img_dim,fk_img_dim),'white')
    fontObj = ImageFont.truetype("Roboto-Light.ttf",font_size)
    fake_draw = ImageDraw.Draw(fake_img)
    BG_W,BG_H = fake_draw.textsize(text,fontObj) #get the text dimensions to use on the real img

    #real image...
    add_to_w = padding
    add_to_h = padding #two vars incase i need to customize this on another occasion...
    real_img = Image.new('RGB',(BG_W+add_to_w,BG_H+add_to_h),color)
    real_draw = ImageDraw.Draw(real_img)
    fontObj = ImageFont.truetype(font_name,font_size)

    #add text + save
    adjust = adjuster #sometimes when the text is not vertically centered some adjustment is needed...(same happens on illustrator unless we make the text an outline)
    real_draw.text((add_to_w/2,add_to_h/2+adjust), text, tcolor, font=fontObj)
    real_img.save(save_as)



if __name__ == "__main__":

    text = input("Enter Text: ")
    color = input("Enter Image Color: ")
    tcolor = input("Enter Text Color: ")

    textOnImg(text,color,tcolor)