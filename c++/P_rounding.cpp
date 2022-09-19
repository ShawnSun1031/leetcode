/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/

// Online IDE - Code Editor, Compiler, Interpreter

#include<iostream>
#include<vector>
using namespace std;

int round(float val);
int main()
{
    vector<float> inputs = {10.4, 10.5};
    vector<int> answers = {10, 11};
    
    for(int i = 0; i < inputs.size(); i++)
    {
        int output = round(inputs[i]);
        
        if(output != answers[i])
            cout << "[Fail] Your answer = " << output << "  Expected answer = " << answers[i] <<endl;
        else
            cout <<"[Pass] Your answer = " << output << endl;
    }
    return 0;
}

int round(float val)
{
    //========== Coding here
    // int d = int(val);
    // if ((val-d)>=0.5)
    // {
    //     return d+1;
    // }else{
    //     return d;
    // }
    
    // 10.4 -> 104 --> 104%100 = 4 --> 104-4 = 100 100/10 = 10
    int m = val*10;
    int p=1;
    while (p<m){
        p *= 10; 
    }
    p = p/10;
    
    int dem = m-p;
    int roundoff = 0;
    if (dem>=5)
    {
        roundoff = 1;
    }
    int ans = m/10+roundoff;
    
    return ans;
    
}