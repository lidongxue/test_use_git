list1=['k91','k82','k72','s31','s51','s61','s52','s9',
       'a11','a21','e31','e62','ds70a','lx750a','lx755a',
       'lx850a','ud10a','lx960']
tmp=[]
for i in range(18):
    for j in range(18-i):
        tmp.append(list1[i:j+i+1])

with open("1111.txt",'w') as file:
    for i in tmp:
        ii=str(i)
        iii=ii.lstrip('[').rstrip(']')
        iiii=iii.replace("'","").replace(" ","")
        print >>file,iiii
