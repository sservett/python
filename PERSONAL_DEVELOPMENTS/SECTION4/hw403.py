print("""=================================================
 
   Please enter your MARKS.

   MARK Table;
   
    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF
 
 ================================================="""
)

a = float(input("1st term exams mark: "))
b = float(input("2nd term exams mark: "))
c = float(input("Final term exams mark : "))

mark = float((a * 0.3) + (b * 0.3) + (c * 0.4))
print("-->",mark)
if mark <= 100 and mark >=  90:
    print("Your Mark is AA")
elif mark >=  85:
    print("Your Mark is BA")
elif mark >=  80:
    print("Your Mark is BB")
elif mark >=  75:
    print("Your Mark is CB")
elif mark >=  70:
    print("Your Mark is CC")
elif mark >=  65:
    print("Your Mark is DC")
elif mark >=  60:
    print("Your Mark is DD")
elif mark >=  55:
    print("Your Mark is FD")
elif mark < 55:
    print("Your Mark is FF, you are FAILED!")
else:
    print("You entered incorrect mark(s)")