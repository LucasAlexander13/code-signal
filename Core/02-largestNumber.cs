// Given an integer n, return the largest number that contains exactly n digits

int largestNumber(int n) {
    string largest = "";
    for (int i = 0; i < n; i++){
        largest = largest + "9";
    }
    return Convert.ToInt32(largest);
}
