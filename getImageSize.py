# coding:utf-8
import os
'''
filelist=[]
filename="F:\\picture\\draw\\3c.jpg"
with open(filename,"rb") as f:
    img=f.read()
    # print(img.encode('hex'))
    lst=str(img.encode('hex'))
    print lst
    mark_SOF0=lst.index('ffc0')
    # print mark_SOF0
    # img_height=int(lst[mark_SOF0+4:mark_SOF0+12])
    # print img_height
    # print int(str(img_height),16)
    img_height=int(str(lst[mark_SOF0+10:mark_SOF0+14]),16)
    print img_height
    img_width=int(str(lst[mark_SOF0+14:mark_SOF0+18]),16)
    print img_width
    if img_height<img_width:
        filelist.append(filename)

print filelist
'''
#-*- coding:utf-8-*-
import os
import shutil
def filter_ext(args,dirn,fln):
    for fls in fln:
        if fls.lower().endswith(args[1].lower()):
            args[0].append(os.path.join(dirn,fls))

def cp_ext(ext,src=".",dest="."):
    if not os.path.exists(dest):
        v=raw_input("The target path doesn't exist,want going?[y]")
        if v in ['y','Y']:
            os.mkdir(dest)
        else:
            return False
    assert os.path.isdir(src) or os.path.isdir(dest),TypeError("ALL path must be Dir")
    assert os.path.exists(src),ValueError("Source Path Must exists!")
    ll=[]
    os.path.walk(src,filter_ext,(ll,ext))
    for l in ll:
        print("Copying File:"+l)
        shutil.copy(l,dest)
