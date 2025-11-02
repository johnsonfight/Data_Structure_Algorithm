int numSubarrayProductLessThanK(int* nums, int numsSize, int k){
    if (k == 0 || numsSize <= 0){
        return 0;
    }
    int l = 0;
    int r = 0;
    int prod = 1;
    int count = 0;
    for (r = 0; r < numsSize; r++){
        prod *= nums[r];
        while (prod >= k && l <= r){
            prod /= nums[l];
            l += 1;
        }
        printf("r = %d, l = %d\n", r,l);
        count += r-l+1;
    }
    return count;
}