// Given the string, check if it is a palindrome.

string reverseString(string str) {  
    if (str.Length <= 1) {
        return str;
    }
    else {
        return reverseString(str.Substring(1)) + str[0];
    }
}  

bool checkPalindrome(string inputString) {
    if (inputString == reverseString(inputString)){
        return true;
    }
    else {
        return false;
    }
}
