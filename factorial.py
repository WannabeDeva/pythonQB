def fact(number):
    i=1
    answer=1
    while (i<=number):
        answer=answer*i
        i=i+1
    
    return answer

num = int(input("Enter any number:"))

factorial = fact(num)

print("The factorial of {} is {}".format(num, factorial))