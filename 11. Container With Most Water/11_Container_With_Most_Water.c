#define MIN(i, j) ((i < j) ? i : j)
#define MAX(i, j) ((i > j) ? i : j)

int maxArea(int* height, int heightSize){
    int max_area = 0;
    int area = 0;
    int l = 0;
    int r = heightSize - 1;

    while(l < r){
        area = (r - l) * MIN(height[l], height[r]);
        max_area = MAX(max_area, area);

        if (height[l] < height[r]){
            l += 1;
        }
        else {
            r -= 1;
        }
    }
    return max_area;
}