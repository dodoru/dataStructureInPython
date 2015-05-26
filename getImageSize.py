# coding:utf-8
import os

pic_dir="F://NRG//lab//python//TryPyhtonGame//image"
filelist=[]
# filename="F:\\NRG\\lab\\python\\TryPythonGame\\image\\3.jpg"  win8
# filename="F://NRG//lab//python//TryPyhtonGame//image//3.jpg"  win7

def get_jpg_size(jpg_file):
    img=jpg_file.read()
    # print(img.encode('hex'))
    print jpg_file
    lst=str(img.encode('hex'))
    print lst
    mark_SOF0=lst.index('ffc0')
    img_height=int(str(lst[mark_SOF0+10:mark_SOF0+14]),16)
    img_width=int(str(lst[mark_SOF0+14:mark_SOF0+18]),16)

    print img_width,"x",img_height

    if img_height<=img_width:
        filelist.append(pic)
    jpg_file.close()

    return (img_width,img_height)

def get_png_size(png_file):
    img=f.read()
    # print(img.encode('hex'))
    lst=str(img.encode('hex'))
    print lst
    # mark_head=lst.index('0000004c')
    # print mark_head #32
    img_width=int(str(lst[32:40]),16)
    img_height=int(str(lst[40:48]),16)

    print img_width,"x",img_height

    if img_height<=img_width:
        filelist.append(pic)
    png_file.close()
    return (img_width,img_height)

for pic in os.listdir(pic_dir):
    # print pic
    mark_dot=pic.index('.')
    pic_path=os.path.join(pic_dir,pic)
    with open(pic_path,'rb') as f:
        if pic[mark_dot+1:]=='jpg':
            # print pic
            get_jpg_size(f)
        if pic[mark_dot+1:]=='png':
            # print pic
            get_png_size(f)
            pic[mark_dot+1:]='bmp'

print filelist

