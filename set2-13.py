fl=1
num123=int(input())
if(num123>1):
    for i in range(2,num123//2):
        if(num123%i==0):
            print("no")
            fl=0
            break;
if fl==1:
    print('yes')
