def reverse(n):
    # write your code here
    while n>0:
        result = n%10
        n = n//10
        print(result)

def main():
    n = int(input())
    reverse(n)

if __name__=="__main__":
    main()