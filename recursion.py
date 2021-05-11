

def fibonacci(i):
    past_values = {}

    if i in past_values:
        return past_values[i]

    if i == 1:
        number = 1
    elif i == 2:
        number = 1
    elif i > 2:
        number = fibonacci(i-1) + fibonacci(i-2)

    past_values[i] = number
    return number
    print("The sequence is" + number)


def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)




def compare_to(s1, s2, index=0):
    if s1[index] < s2[index]:
        return -1
    if s1[index] > s2[index]:
        return 1
    if s1[index] == s2[index]:
        if len(s1) and len(s2) == 1:
            return 0
        return compare_to(s1[1:], s2[1:])

if __name__ == "__main__":
    fib_no = int(input("What number would you like to Fibonacci sequence? "))
    print(fibonacci(fib_no))

    gcd_no = int(input("What is the first number of the numbers you want to find the common denominator between?"))
    gcd_no_two = int(input("What is the second number?"))
    print(gcd(gcd_no, gcd_no_two))

    no_compare_to_one = input("What is the first string in the comparison? ")
    no_compare_to_two = input("What is the second string in the comparison? ")
    print(compare_to(no_compare_to_one, no_compare_to_two))


