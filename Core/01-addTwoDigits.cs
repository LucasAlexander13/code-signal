// You are given a two-digit integer n. Return the sum of its digits.

int addTwoDigits(int n) {
    int firstNumber = n / 10;
    int secndNumber = n - firstNumber * 10;
    return firstNumber + secndNumber;
}
