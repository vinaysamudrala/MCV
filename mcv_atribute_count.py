from xml.dom import minidom
import os

cd = os.getcwd()
fn=[]
xlfil = open('atrcnt.csv', 'w')
xlfil.write('ID'+','+ 'Picking an item'+','+'Placing an item'+','+'Looking directly to a camera'+','+ 'Looking over shoulder'+','+ 'Customer is making a phone call' +','+'Customer is using the phone'+','+'Crouching'+","+"Total"+"labled Frames"+'\n')
for root, dirs, files in os.walk(cd):
    for name in files:
        vinay=os.path.join(root, name)
        if ".xml" in vinay[-4:]:
            fn.append(os.path.join(root, name))

file_names = []
for x in fn:
    frame_count=[]
    file_name = x
    doc = minidom.parse(file_name)
    name = doc.getElementsByTagName("id")[0]
    frame=doc.getElementsByTagName("box")
    for xx in frame:
        z=int(xx.getAttribute("frame"))
        zz=int(xx.getAttribute("outside"))
        if zz==0:
            frame_count.append(z)
    ln=len(set(frame_count))
    print(set(frame_count))
    Last_frame = int(name.firstChild.data)
    vs1= open(str(file_name), 'r')
    file_names.append(file_name)
    sk1= vs1.read()
    CoList1 = sk1.split("\n")
    a=-3
    b=-2
    c=-2
    d=-2
    e=-2
    f=-2
    g=-2
    h=Last_frame
    for pk in CoList1:
        if 'Picking an item' in pk:
            a=a+1
        if 'Placing an item' in pk:
            b=b+1
        if 'Looking directly to a camera' in pk:
            c=c+1
        if 'Looking over shoulder' in pk:
            d=d+1
        if 'Customer is making a phone call' in pk:
            e=e+1
        if 'Customer is using the phone' in pk:
            f=f+1
        if 'Crouching' in pk:
            g=g+1

    total=a+b+c+d+e+f+g
    xlfil.write(str(h)+","+str(a)+","+str(b)+","+str(c)+","+str(d)+","+str(e)+","+str(f)+","+str(g)+","+str(total)+','+str(ln)+'\n')
    print(total,a,b,c,d,e,f,g, "....", h)
    print("Filename:", file_names)
xlfil.close()