#include "pch.h"
#include "myDll.h"
#include <stdexcept>
#include <Windows.h>

using namespace std;

int Hour() {
    SYSTEMTIME st;
    GetLocalTime(&st);
    return st.wHour;
}

int Minute() {
    SYSTEMTIME st;
    GetLocalTime(&st);
    return st.wMinute;
}

int Second() {
    SYSTEMTIME st;
    GetLocalTime(&st);
    return st.wSecond;
}