#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans;
        char c;
        for(int i=0; i<strs[0].size();i++)
        {
            c = strs[0][i];
            for(auto s:strs)
            {
                if( (i+1)>s.size() || c!=s[i] )
                    return ans;

            }
            ans.push_back(c);
        }
        return ans;
    }
};

int main()
{
    vector<string> strs = {"dog","racecar","car"};
    Solution s;
    string ans = s.longestCommonPrefix(strs);
    /*
    for(auto s : strs)
    {
        printf("%d\n",s.size());
    }
    */
    printf("%s",ans.c_str());

    return 0;    
}