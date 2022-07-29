import sys
import os

# In Anlehung an https://stackoverflow.com/questions/29518833/editing-yaml-file-by-python

if __name__ == '__main__':
    newImage=sys.argv[1]

    newfile=""

    with open("rr-deploy.yaml","r") as f:
        list_doc = f.readlines()
        for line in list_doc:
            wl=line
            if "image:" in wl:
                h=wl.split(":")
                wl=h[0]+ ": " +newImage + "\n"
            newfile=newfile+wl

    with open("rr-deploy.yaml","w") as f:
        f.write(newfile)

            
