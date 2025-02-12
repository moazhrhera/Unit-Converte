A = float(input("Enter the space -> "))       #هنا يتم ادخال قيمه المساحه
B = str(input("Enter type of space (  mm , cm, m , km) -> "))      #هنا يتم تحديد نوع المساحه 
C = str(input("Enter new type of space (mm , cm , km) -> "))        #هنا يتم ادخال نوع المساحه الجديده 

if B == "mm" and C == "cm":
    result = A / 10
    print( A,B,"=",result,"C")
elif B == "mm" and C == "m":
    result = A / 1000
    print(A,B,"=",result,"C")
elif B == "mm" and C == "km":
    result = A / 1000000
    print(A,B,"=",result,"C")
elif B == "cm" and C == "mm":
    result = A* 10 
    print(A,B,"=",result,"C")
elif B == "cm" and C == "m":
    result = A / 100
    print(A,B,"=",result,"C")
elif B == "cm" and C == "km":
    result = A / 100000
    print(A,B,"=",result,"C")
elif B == "m" and C == "mm":
    result = A * 1000 
    print(A,B,"=",result,"C")
elif B == "m" and C == "cm":
    result = A * 100 
    print(A,B,"=",result,"C")
elif B == "m" and C == "km":
    result = A / 1000
    print(A,B,"=",result,"C")
elif B == "km" and c == "mm":
    result = A * 1000000
    print(A,B,"=",result,"C")
elif B == "km" and C == "cm":
    result = A * 100000
    print(A,B,"=",result,"C")
elif B == "km" and C == "m":
    result = A * 1000
    print(A,B,"=",result,"C")
elif (B == "mm" and C == "mm") or \
     (B == "cm" and C == "cm") or \
     (B == "m" and C == "m") or \
     (B == "km" and C == "km") :
    result = A
    print(A,B,"=",result,"B")
else:
    print("Invalid syntax, make sure to enter a valid input.")
