var isPalindrome = function(x) {
    if ((x<0) || (x>0 && x%10==0)){ 
        return 0
    }
    // checking for if x is negative || x is greater than zero and last digit of x is not zero i.e. "01"
    result = 0
    while (result<x){               // check only till result is less than x
        result = result * 10 + x%10  // make result 1 digit extra by multiplying by 10 and then add last number of x by taking modulus
        x = x/10                     // reduce last number of x by dividing it by 10
    }   

    if((x==result) || (x==result/10)){ // check for even x==result and check for odd by dividing result by 10 i.e. x= 1 and result= 12 then x =result if we divide result by 10
        return true
    }else{
        return false
    }
};