import os,shutil 
extenions=['.doc','.pdf','.docx','.txt']
from_dir='C:/Users/kapis/Downloads/C102_assets-main/C102_assets-main'
to_dir='C:/Users/kapis/OneDrive/Desktop'
files=os.listdir(from_dir)
for file in files:
    name,ext=os.path.splitext(file)
    if(ext in extenions):
        path1=from_dir+'/'+file
        path2=to_dir+"/documents"
        path3=path2+'/'+file
        if(os.path.exists(path2)):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)    