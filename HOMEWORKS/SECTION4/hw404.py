print("""=================================================
 
   Please select your choice;

   Triangle or Quadangle ?
 
 ================================================="""
)

a = str(input("Which shape do you want? Triangle or Quadangle : "))

a = a.lower()

if a == "quadangle":
    a1 = int(input("1st Edge : "))
    a2 = int(input("2nd Edge : "))
    a3 = int(input("3rd Edge : "))
    a4 = int(input("4th Edge : "))

    if (a1 == a2 == a3 == a4):
        print("This is SQUARE")
    elif (a1 == a2 and a3 == a4) or (a1 == a3 and a2 == a4) or (a1 == a4 and a2 == a3):
        print("This is RECTANGLE")
    else:
        print("This is QUADANGLE")
        
elif a == "triangle":
    a1 = int(input("1st Edge : "))
    a2 = int(input("2nd Edge : "))
    a3 = int(input("3rd Edge : "))

    if (a1 == a2 == a3) : 
        print("This is Equilateral Triangle")
    elif (a1 == a2 != a3) or (a1 != a2 == a3) or (a1 == a3 != a2):
        print("This is Isosceles Triangle")
    else:
        print("This is simple Triangle")

else:
    print("You enterted invalid choice")

