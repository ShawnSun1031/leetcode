#include <bits\stdc++.h>

using namespace std;

int main(){
    int a = 96; // 1100
    int b;
    int sum = 0;
    bool sign = true;
    while (a>1){
        if (sign == true){
            sum = sum + a&1;

            // cout << sum << endl;
        }
        else{
            sum = sum - a&1;
            // cout << sum << endl;
        }
        a = a>>1;
        sign = !sign;
    }
    if (sign == true){
        sum = sum + a&1;

        // cout << sum << endl;
    }
    else{
        sum = sum - a&1;
        cout << sum << endl;
    }


    b = a >> 1 ; // 101

    cout << sum;



}