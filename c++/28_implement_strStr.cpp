#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        size_t pos = haystack.find(needle);
        return pos==string::npos?-1:pos;
        
    }
};

/* Brute Force
class Solution {
public:
    int strStr(string haystack, string needle) {
        int i = 0, j = 0, n = haystack.size(), m = needle.size();
        while ( i < n && j < m){
            if (haystack[i] == needle[j]){
                i++;
                j++;

            }else{
                i = i-j+1;
                j = 0
            }
        }
        return j >= m ? i - j : -1;
    }
};
*/

int main(){
    string haystack = "hello";
    string needle = "ll";

    cout << Solution().strStr(haystack,needle) << endl;

}