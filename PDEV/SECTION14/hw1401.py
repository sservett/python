def extra(fonk):
    
    def extra_fetaure():
        print("---------------------------")
        print("PERFECT NUMBERS")
        print("---------------------------")
        for number in range(1,101):
            total = 0
            i = 1
            while (i < number):
                if (number % i == 0):
                    total += i
                i +=1
            if (total == number):
                print(number)
        fonk()
                
    return extra_fetaure
    
@extra
def prime_numbers():
    print("---------------------------")
    print("PRIME NUMBERS")
    print("---------------------------")
    
    for number in range(2,101):
        i = 2
        count = 0 
        while ( i < number ):
            if (number % i == 0):
                count +=1
            i += 1
        
        if (count == 0):
            print(number)

prime_numbers()