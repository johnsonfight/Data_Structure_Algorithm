int removeDuplicates(int* nums, int numsSize){
    int i = 0;
    int j = 0;
    while (i<=j && j<numsSize){
        if (nums[i] == nums[j]){
            j+=1;
        }else{
            nums[i+1] = nums[j];
            i+=1;
            j+=1;
        }
    }
    return i+1;
}