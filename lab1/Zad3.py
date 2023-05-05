
txt = input("IP to check: ") 
x = txt.split(".") 
flag = True 
if x.count(x) == 4: 
    for i in x: 
        if(int(i)<0 or int(i)>255): 
            flag = False 
if flag: 
    print("IP correct") 
else: 
    print("IP incorrect")