/********************************************************************************
 * @file test02.cc
 * @author lxy (2305195328@qq.com)
 * @brief 斐波那契数列(递归)
 * @version 1.0.0
 * @date 2022-11-24
 ********************************************************************************/
#include <iostream>
using namespace std;

/********************************************************************************
 * @brief 给定一值当作位置，求斐波那契数列那个位置的值 
 *  
 * @param  _arg
 * @return int
 ********************************************************************************/
//斐波那契指的是这样一个数列：1、1、2、3、5、8、13、21、34、……
int func(int _arg)
{
    //递归尾
    if(_arg == 1 || _arg == 2)
        return 1;
    //? 只要知道_arg-2和_arg-1位置的值就能算出_arg的值
    return func(_arg-2) + func(_arg-1);
}

int main(int argc, char **argv)
{
    
    cout << func(9) << endl;
    return 0;
}