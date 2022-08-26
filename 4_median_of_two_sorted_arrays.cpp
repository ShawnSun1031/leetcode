#include <bits\stdc++.h>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        int l = (m+n+1)/2;
        int r = (m+n+2)/2;
        int left,right;
        left = findkthnumber(nums1,0,nums2,0,l);
        right = findkthnumber(nums1,0,nums2,0,r);

        return (left+right)/2.0;
        
    }
    int findkthnumber(vector<int>& nums1,int i, vector<int>& nums2,int j, int k){
        if (i>=nums1.size()){
            return nums2[j+k-1];
        }
        if (j>=nums2.size()){
            return nums1[i+k-1];
        }
        if (k==1){
            return min(nums1[i],nums2[j]);
        }
        int midval1 = (i+k/2-1<nums1.size()) ? nums1[i+k/2-1] : INT_MAX;
        int midval2 = (j+k/2-1<nums2.size()) ? nums2[j+k/2-1] : INT_MAX;
        if (midval1 < midval2){
            return findkthnumber(nums1,i+k/2,nums2,j,k-k/2);
        }else{
            return findkthnumber(nums1,i,nums2,j+k/2,k-k/2);
        }

    }
};

int main(){
    vector<int> nums1 ={2,3,4,5,6};
    vector<int> nums2 ={1};

    cout << Solution().findMedianSortedArrays(nums1,nums2) << endl;

}