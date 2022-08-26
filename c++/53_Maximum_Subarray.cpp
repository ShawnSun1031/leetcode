#include <bits\stdc++.h>

using namespace std;


/* method one DP */
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int curr = nums[0];
        int res = nums[0];
        if (nums.size()==1){
            return nums[0];
        }

        for (int i=1 ; i<nums.size() ; i++){
            curr += nums[i];
            if (curr<0 | nums[i] > curr){
                curr = nums[i];
            }
            if (res < curr){
                cout << res << endl;
                res = curr;
            }
        }
        return res;

    }
};


int main(){
    vector<int> nums = {-2,1};
    
    
    cout << Solution().maxSubArray(nums) << endl;

    
}