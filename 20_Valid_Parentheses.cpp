#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> mystack;
        for(int i=0; i<s.size();i++)
        {
            switch(s[i])
            {
                case '(': mystack.push('(');break;
                case '[': mystack.push('[');break;
                case '{': mystack.push('{');break;
                case ')':
                {
                    if ((mystack.size()==0) || (mystack.top()!='('))
                        return false;
                    mystack.pop();
                    break;
                }
                case ']':
                {
                    if ((mystack.size()==0) || (mystack.top()!='['))
                        return false;
                    mystack.pop();
                    break;
                }
                case '}':
                {
                    if ((mystack.size()==0) || (mystack.top()!='{'))
                        return false;
                    mystack.pop();
                    break;
                }
            }
        }
        if (mystack.size() != 0)
            return false;
        return true;
       

        
    }
};

int main()
{
    string input = "([(())]]{}";
    Solution s;
    bool flag = s.isValid(input);
    printf("%d",flag);
    return 0;
}