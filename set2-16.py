n1,m1=[int(x) for x in input().split()]
for num in range(n1,m1):
  fl=1
  if(num>1):
      for i in range(2,num):
          if(num%i==0):
              fl=0
              break;
      if(fl==1):
          print(num,end=' ')
