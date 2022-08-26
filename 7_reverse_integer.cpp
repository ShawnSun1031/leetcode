#include <bits\stdc++.h>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        long res;
        res = x%10;
        x = x/10;
        while(x!=0){

            res = res*10 + x%10;
            x = x/10;
        }
        
        if (res>pow(2,31)-1){
            return 0;
        }
        if (res<-pow(2,31)){
            return 0;
        }
        
        return res;
    }
};

int main(){
    int x = 123;

    cout << Solution().reverse(x) << endl;

}