import os
import binascii
import shutil


def openandclassfy(root,file_name):
    out_dir = os.path.join(os.getcwd(),"out")
    jpg_head = bytes([0xff,0xd8])
    png_head = bytes([0x89,0x50,0x4e,0x47])
    gif_head = bytes([0x47,0x49,0x46])
    file_path = os.path.join(root,file_name)
    
    f = open(file_path,'rb')
    t = f.read(8)
    des_path = ""
    if t[0:2] == jpg_head:
        #print("jpg")
        des_path = os.path.join(out_dir,file_name+".jpg")
    elif t[0:4]==png_head:
        #print("png")
        des_path = os.path.join(out_dir,file_name+".png")
    elif t[0:3] == gif_head:
        des_path = os.path.join(out_dir,file_name+".gif")
    else:
        #print("mp4")
        des_path = os.path.join(out_dir,file_name+".mp4")
    #print(des_path)
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    shutil.copyfile(file_path,des_path)
    
    
if __name__ == "__main__":
    print(os.getcwd())
    root_dir = "./contents/"
    for (root, dirs, files) in os.walk(root_dir):
        if len(files) > 0:
            for file_name in files:
                openandclassfy(root,file_name)
                
