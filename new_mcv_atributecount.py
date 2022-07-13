import xml.etree.ElementTree as ET
import os
import zipfile

cd = os.getcwd()
fn=[]
zip_files_list=[]
for root, dirs, files in os.walk(cd):
    for name in files:
        vinay=os.path.join(root, name)
        if ".zip" in vinay[-4:]:
            zp=os.path.join(root, name)
            zip_files_list.append(zp)
            with zipfile.ZipFile(zp, 'r') as zip_ref:
                try:
                    os.mkdir(vinay[:-4])
                    zip_ref.extractall(vinay[:-4])
                except:
                    continue

xlfil = open('atrcnt.csv', 'w')
xlfil.write('ID'+','+ 'Picking an item'+','+'Placing an item'+','+'Looking directly to a camera'+','+ 'Looking over shoulder'+','+ 'Customer is making a phone call' +','+'Customer is using the phone'+','+'Crouching'+","+"Total label count"+","+"Total labled Frames"+'\n')
for root, dirs, files in os.walk(cd):
    for name in files:
        vinay=os.path.join(root, name)
        if ".xml" in vinay[-4:]:
            fn.append(os.path.join(root, name))

for x in fn:
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    total=0
    tree = ET.parse(x)
    root = tree.getroot()
    id_list = []
    labled_frames=[]
    for x in root.iter('id'):
        id_list.append(x.text)

    for nei in root.iter('box'):
        ko=nei.attrib
        for neighbor in nei.iter('attribute'):
            k=neighbor.text
            if ko['outside'] == "0":
                if 'Picking an item' in k:
                    a=a+1
                if 'Placing an item' in k:
                    b=b+1
                if 'Looking directly to a camera' in k:
                    c=c+1
                if 'Looking over shoulder' in k:
                    d=d+1
                if 'Customer is making a phone call' in k:
                    e=e+1
                if 'Customer is using the phone' in k:
                    f=f+1
                if 'Crouching' in k:
                    g=g+1
                labled_frames.append(ko["frame"])

            total=a+b+c+d+e+f+g
            #print(total,">>>>>>>>>>>>>>",labled_frames)
    print(id_list[0]+","+str(a)+","+str(b)+","+str(c)+","+str(d)+","+str(e)+","+str(f)+","+str(g)+","+str(total)+','+str(len(set(labled_frames)))+'\n')
    xlfil.write(id_list[0]+","+str(a)+","+str(b)+","+str(c)+","+str(d)+","+str(e)+","+str(f)+","+str(g)+","+str(total)+','+str(len(set(labled_frames)))+'\n')
xlfil.close()
