from PIL import Image,ImageEnhance
import os

#loop se sabhi jpg wali pics ko .pdf mai convert krke change kr lunga

'''for item in os.listdir(r'C:\prabhakar\images'):                                 #listdir se folder ke chije leli
    if item.endswith('.jpg'):                                                   #loop lgaya us listdir mai fir us path ko join kia loop wale item se
        pic=Image.open(os.path.join(r'C:\prabhakar\images',item))               #path ko loop ke item se join kr dia or fir open kr lia
        i_name,extension=os.path.splitext(item)                                 #file name or  or extension alg alg kr liye jrurt ke hisab se
        path=(os.path.join(r'C:\prabhakar\images',f'{i_name}'))                 #nya path bnaya h jha se save krana h wha ke liye
        photo=Image.open(path+".jpg")                                           #sabhi photos ko open krega or next step mai show krega
        # photo.show()                                                          #ise comment se bhr nikalna h show krane ke liye pics
        pic.save(f'{path}.pdf')'''

'''
#-------------resize all pics at once-------------
for item in os.listdir(r'C:\prabhakar\images'):
    if item.endswith('.jpg'):
        pic1=Image.open(os.path.join(r'C:\prabhakar\images',item))
        size=(3000,3000)
        pic1.resize(size)
        pic1.save(item)                                                         #ye jo for loop se item iterate hora h vo string mai ara h to agr use use krna h to bina string
'''

'''
#-------------ImageEnchancer-------------------------
from PIL import ImageEnhance
for item in os.listdir(r'C:\prabhakar\images'):

    pic2=Image.open(os.path.join(r'C:\prabhakar\images',item))

    sharp_img=ImageEnhance.Sharpness(pic2)
    sharp_img.enhance(5.9).save("sharpen"+item)

    colored_img=ImageEnhance.Color(pic2)
    colored_img.enhance(2.8).save("coloued "+item)

    bright_img=ImageEnhance.Brightness(pic2)                                    #floats mai bi pass kr skte h value
    bright_img.enhance(2).save("bright"+item)

    contrast_img=ImageEnhance.Contrast(pic2)
    contrast_img.enhance(1.5).save("contrast"+item)
'''

#-----------------filter---------------------------
























# # print(Image.open(os.path.join(r'C:\prabhakar\images',)))
# path=os.path.join(r'C:\prabhakar\images','image10.jpg')
# pic=Image.open(path)
# pic.show()