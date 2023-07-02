void moveZeroes(int* nums, int numsSize){
    
    // Count zeros in nums
    int zero_counts = 0;
    for (int i = 0; i < numsSize; i++){
        if (nums[i] == 0){
            zero_counts += 1;
        }
    }

    // Remove all zeros in nums
    int non_zero_idx = 0;
    for (int i = 0; i < numsSize; i++){
        if (nums[i] != 0){
            nums[non_zero_idx] = nums[i];
            non_zero_idx++;
        }
    }

    // Add all zeros back to the end of nums
    for (int i = non_zero_idx; i < numsSize; i++){
        nums[i] = 0;
    }
}