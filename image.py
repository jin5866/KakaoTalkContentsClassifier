import os
import binascii



def openandclassfy(root,file_name):
    out_dir = "./out/"
    jpg_head = bytes([0xff,0xd8])
    file_path = os.path.join(root,file_name)
    
    f = open(file_path,'rb')
    t = f.read(2)
    des_path
    if t == jpg_head:
        print("jpg")
        des_path = os.path.join(out_dir,file_name)

if __name__ == "__main__":
    root_dir = "./contents/"
    for (root, dirs, files) in os.walk(root_dir):
        if len(files) > 0:
            for file_name in files:
                openandclassfy(root,file_name)
                
