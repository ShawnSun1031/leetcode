#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int index=0;
        
        for (int i=0; i<nums.size() ; i++){
            
            if (nums[i] != val){
                nums[index++] = nums[i];
            }
        }
        return index;
    }
};

int main(){
    vector<int> nums = {3,2,2,3};
    int val = 3;
    
    cout << Solution().removeElement(nums,val) << endl;
    for (auto it=nums.begin(); it!=nums.end() ; it++){
        printf("%d\n",*it);
    }

}