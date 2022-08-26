#include <bits\stdc++.h>

using namespace std;

/*
class Solution {
public:
    int lengthOfLastWord(string s) {
        vector<int> res;
        int temp = 0;
        for (int i=0; i<s.size() ; i++){
            if (s[i]==' ' | s[i]=='\n'){
                temp = 0;
            }else{
                
                temp++;
            }
            if (temp!=0){
                res.push_back(temp);
            }

        }

        return res.back();
        
    }
};
*/

class Solution{
    public:
        int lengthOfLastWord(string s) {
            int i = s.size() - 1;
            int res = 0;
            while (i>=0 && s[i]==' '){
                i--;
            }
            while (i>=0 && s[i]!=' '){
                i--;
                res++;
            }
            return res;

        }
};

int main(){
    string s = "luffy is still joyboy";

    cout << Solution().lengthOfLastWord(s) << endl;
    

}