print("Welcome to the Pattern Generator and Number Analyzer!")
print()
while True:
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of numbers")
    print("3. Exit")
    choice = int(input("Enter your choice:"))
    match choice:
        case 1:
            n = int(input("Enter the number of rows for the pattern:"))
            print()
            print("Pattern:")
            for i in range(1,n+1):
                for j in range(i):
                    print("*",end = " ")
                print()
            print()
        case 2:
            print()
            while True:
                n1 = int(input("Enter the start of range:"))
                n2 = int(input("Enter the end of range:"))
                s = 0
                if n1|n2 < 0:
                    print ("Please Enter positive number")
                elif n1 > n2:
                    print("please enter valid range")
                else:
                    for i in range(n1,n2+1):
                        if i%2 ==0:
                            print(f"Number {i} is Even")
                        else:
                            print(f"Number {i} is Odd")
                        s +=i
                    print(f"Sum of all numbers from {n1} to {n2} is : {s}")
                    break
            print()
        case 3:
            print("Exiting the Program. Goodbye! ")
            break
