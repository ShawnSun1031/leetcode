#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // Init
        int index = 0;
        
        // Walk
        for (int i=0; i<nums.size(); ++i) {
            if (i == 0 || nums[i] != nums[i-1]) {
                nums[index] = nums[i];
                ++index;
            }
        }

        return index;
        
    }
};

int main(){
    vector<int> nums = {0,0,1,1,1,2,2,3,3,4};
    Solution s;
    int ans;
    ans = s.removeDuplicates(nums);

    printf("%d\n",ans);
    printf("*****\n");

    for (int i=0; i<nums.size(); ++i) {
        printf("%d\n", nums[i]);
    }
    

    return 0;
}