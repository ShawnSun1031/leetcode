#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> c = {{'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}};
        int result = 0;
        for(int i=0;i<s.size();i++){
            if(c[s[i]]>=c[s[i+1]]) 
                result += c[s[i]];
            else
                result -= c[s[i]];
        }
        return result;
        
    }
};

int main()
{
    string input = "III";
    Solution s;
    int ans = s.romanToInt(input);
    printf("%d\n",input[1] <= input[0]);
    printf("%d",ans);

    return 0;
}