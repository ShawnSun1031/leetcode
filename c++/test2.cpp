#include <iostream>

struct Treenode
{
    int val;
    struct Treenode *leftnode;
    struct Treenode *rightnode;
};

int main()
{
    int a = 0;
    std::cout << a;
    struct Treenode *T;
    T->val = 5;
    std::cout << T->val;
    T->leftnode = new struct Treenode();
    std::cout << T->val;
}
