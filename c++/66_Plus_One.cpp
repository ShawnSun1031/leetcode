#include <bits\stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        for (int i=n-1; i>=0; --i){
            if (digits[i] == 9){
                digits[i] = 0;
            }else{
                digits[i] = digits[i] + 1;
                return digits;
            }
        }
        if (digits.front() ==0){
            digits.insert(digits.begin(),1);
        }
        return digits;

        
    }
};


int main(){
    vector<int> digits = {1,2,3};
    cout << Solution().plusOne(digits)[0] << endl;

}