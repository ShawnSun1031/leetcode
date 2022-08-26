#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        vector<int>::iterator it = find(nums.begin(),nums.end(),target);
        if (it!=nums.end()){
            return distance(nums.begin(),it);
        }else{
            for (auto it = nums.begin() ; it < nums.end() ; it++){
                if (*it > target){
                    return distance(nums.begin(),it);
                    
                }
            }
        }

        return nums.size();
    }
};

int main(){
    vector<int> nums = {1,3,5,6};
    int target = 7;
    cout << Solution().searchInsert(nums,target);
    
    return 0;
}