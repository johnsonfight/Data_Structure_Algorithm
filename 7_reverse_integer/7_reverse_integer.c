// Runtime 0 ms Beats 100%
// Memory 5.4 MB Beats 100%

// #include <stdbool.h>
#include <math.h>
int reverse(int x){
    // Check input x is in range of signed 32-bit minus 1 integer
    if (x > pow(2,31)-1 || x < -(pow(2,31)-1)){
        return 0;
    }

    // Handle negative sign
    bool isNeg;
    if (x > 0){
        isNeg = false;
    } else if (x == 0){
        return 0;
    } else {
        isNeg = true;
        x = -x;
    }
    
    long out = 0;
    while (x != 0){
        out = out*10 + x%10;
        x = x/10;
    }

    // Handle negative sign
    if (isNeg == true){
        out = -out;
    }

    // Check output x is in range of signed 32-bit integer
    if (out > pow(2,31)-1 || out < -pow(2,31)){
        return 0;
    }

    return out;
}