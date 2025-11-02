// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int binarySearch(int first, int last){
    int mid = first + (last - first)/2;
    if (isBadVersion(mid) && !isBadVersion(mid-1)){
        return mid;
    }
    if (!isBadVersion(mid)){
        return binarySearch(mid+1, last);
    } else {
        return binarySearch(first, mid-1);
    }
}

int firstBadVersion(int n) {
    //[1, 2, 3, 4, 5, ..., n]
    // G, G, G, B, B
    return binarySearch(1, n);
}