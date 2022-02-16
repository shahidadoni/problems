def rotate(n,k):
    # write your code here
    temp = n
    length = 0
    while temp > 0:
      temp = temp // 10
      length = length + 1

    k = k % length
    if k<0:
      k = k + length

    divisor = 1
    mult = 1
  
    for i in range(1,length+1):
      if i<=k:
        divisor *= 10
      else:
        mult *= 10
    
    quotient = n // divisor
    remainder = n % divisor

    rotated_number = remainder * mult + quotient

    print(rotated_number)

def main():
    n = int(input())
    k = int(input())
    rotate(n,k)

if __name__=="__main__":
    main()