# coding:utf-8
import os

pic_dir="F://picture//draw"
filelist=[]
# filename="F:\\NRG\\lab\\python\\TryPythonGame\\image\\3.jpg"  win8
# filename="F://NRG//lab//python//TryPyhtonGame//image//3.jpg"  win7

def get_jpg_size(jpg_file):
    img=jpg_file.read()
    # print(img.encode('hex'))
    print jpg_file
    lst=str(img.encode('hex'))
    # print lst
    if lst.find('ffc0')>=0:
        mark_SOF0=lst.index('ffc0')
        img_height=int(str(lst[mark_SOF0+10:mark_SOF0+14]),16)
        img_width=int(str(lst[mark_SOF0+14:mark_SOF0+18]),16)

        print img_width,"x",img_height
        # return [img_width,img_height]
        return img_width>=img_height



def get_png_size(png_file):
    img=png_file.read()
    # print(img.encode('hex'))
    lst=str(img.encode('hex'))
    print lst
    # mark_head=lst.index('0000004c')

    # print mark_head #32
    img_width=int(str(lst[32:40]),16)
    img_height=int(str(lst[40:48]),16)
    # img_info=
    print img_width,"x",img_height

    # return [img_width,img_height]
    return img_width>=img_height

'''
def choose_pic(width,height):
    # pic_inro=[width,height]
    # return pic_info[0]>=pic_info[1]
    return width>=height
'''

def test():

    for pic in os.listdir(pic_dir):
        mark_dot=pic.index('.')

        if pic[mark_dot+1:] in {'jpg','png','bmp'}:
            print pic
            pic_path=os.path.join(pic_dir,pic)
            with open(pic_path,'rb+') as f:
                if pic[mark_dot+1:]=='jpg':
                    if get_jpg_size(f):
                        filelist.append(pic)

                if pic[mark_dot+1:]=='png':
                    if get_png_size(f):
                    # if choose_pic(get_png_size(f)):
                        filelist.append(pic)
                        pic_path.replace('png','bmp')

                        
                f.close()
    print filelist


if __name__=="__main__":
    test()
