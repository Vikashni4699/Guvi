bb=input()
list=['a','e','i','o','u']
if(bb.isalpha()==True):
  if(bb in list):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("Invalid")
