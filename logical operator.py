n=int(input("Enter the number:"))

if n>=80 and n<=100:
    print("A+")
elif n>=75 and n<=79:
    print("A")

elif n>=70 and n<=74:
    print("A-")
elif n>=65 and n<=69:
    print("B+")
elif n>=60 and n<=64:
    print("B")    
    
else:
    print("the result is poor or fail or invalid !")
    

c=input("Enter the character:")
if c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
    print("Vowel")
else:
    print("Consonent")