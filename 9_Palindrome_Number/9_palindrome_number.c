bool isPalindrome(int x){
    if (x < 0){
        return false;
    };

    int origin = x;
    long reverse = 0;
    
    while (x > 0){
        reverse = x%10 + reverse*10;
        x = x/10;
    }
    return origin == reverse;
}