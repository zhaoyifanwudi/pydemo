from PIL import Image
import math

def qipan(width,height,color1,color2,interval):
    im = Image.new('RGB',(width,height))#生成新的图
    hInterval = height/interval#每格的宽高
    wInterval = width/interval
    for h in range(width):#间隔填色
        for w in range(width):
            if (int(h/hInterval)+int(w/wInterval)) % 2 == 1:
                im.putpixel((w,h),color1)
            else:
                im.putpixel((w,h),color2)
    im.show()
if __name__ == '__main__':
    qipan(500,500,(50,50,50),(240,240,240),4)