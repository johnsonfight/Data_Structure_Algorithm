#define MAX_ASCII_COUNT 128

int lengthOfLongestSubstring(char * s){
    int left = 0;
    int output = 0;
    int len = strlen(s);
    int seen[MAX_ASCII_COUNT];
    memset(seen, -1, sizeof(seen));

    for (int right = 0; right < len; right++) {
        if (seen[s[right]] != -1) {
            left = (left > seen[s[right]] + 1) ? left : seen[s[right]] + 1;
        }
        output = (output > right - left + 1) ? output : right - left + 1;
        seen[s[right]] = right;
    }
    return output;
}