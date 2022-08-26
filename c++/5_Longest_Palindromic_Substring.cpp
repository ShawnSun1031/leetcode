#include <bits\stdc++.h>

using namespace std;
/*
class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty())  return "";
        int n=s.size(), dp[n][n] = {0}, left = 0, len = 1;
        for (int i=0; i<n; i++){
            dp[i][i] = 1;
            for (int j=i; j<n; j++){
                if (s[i]==s[j] && (j-i<2 or dp[i+1][j-1])){
                    dp[i][j] = 1;
                }
                else{
                    dp[i][j] = 0;
                }
                if (dp[i][j] and len<j-i+1){
                    len = j-i+1;
                    left = i;
                }
            }
        }
        return s.substr(left,len);
        
    }
};
*/
class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty())  return "";
        int n=s.size(); 
        vector<vector<bool>> dp(s.size(), vector<bool>(s.size(), false));
     
        int left = 0, len = 1;

        for (int i=0; i<n; i++){
            dp[i][i] = true;
            for (int j=i; j<n; j++){
                if (s[i]==s[j] && (j-i<2 or dp[i+1][j-1])){
                    dp[i][j] = true;
                }
                else{
                    dp[i][j] = false;
                }
                if (dp[i][j] and len<j-i+1){
                    len = j-i+1;
                    left = i;
                }
            }
        }
        return s.substr(left,len);
        
    }
};

int main(){
    string s = "aacabdkacaa";

    cout << Solution().longestPalindrome(s) << endl;


}