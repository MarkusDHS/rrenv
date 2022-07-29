import sys
import os
import yaml

# In Anlehung an https://stackoverflow.com/questions/29518833/editing-yaml-file-by-python

if __name__ == '__main__':
    newImage=sys.argv[1]

    with open("rr-deploy.yaml") as f:
        list_doc = yaml.load(f, Loader=yaml.FullLoader)

    for sense in list_doc:
        if sense["name"] == "image":
             sense["value"] = newImage

    with open("rr-deploy.yaml", "w") as f:
        yaml.dump(list_doc, f)
