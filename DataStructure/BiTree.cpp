#include <iostream>

typedef int DataType;

struct TreeNode{
    DataType data;
    TreeNode *leftTree;
    TreeNode *rightTree;


TreeNode(DataType value) : data(value), leftTree(nullptr), rightTree(nullptr) {}
};