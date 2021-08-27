// Given a year, return the century it is in. The first century spans 
// from the year 1 up to and including the year 100, the second from 
// the year 101 up to and including the year 200, etc.

int centuryFromYear(int year) {
    double sec = year / 100;
    if (year % sec == 0){
        return Convert.ToInt32(sec);
    }
    else {
        return Convert.ToInt32(sec + 1);
    }
}
