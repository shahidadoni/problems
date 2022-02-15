def inverse(n):
    # write your code here
    inverse = 0
    index = 1
    while n != 0:
        last_digit = n % 10
        inverse_digit = index
        inverse_index = last_digit

        inverse = inverse + index * pow(10,last_digit-1)

        index += 1
        n = n//10

    print(inverse)



def main():
    n = int(input())
    inverse(n)

if __name__=="__main__":
    main()