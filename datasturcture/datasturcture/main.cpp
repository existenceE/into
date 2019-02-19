//
//  main.cpp
//  datasturcture
//
//  Created by 马晓宁 on 2018/7/7.
//  Copyright © 2018年 flowerao. All rights reserved.
//

#include <iostream>
#include "DFS.hpp"

using namespace std;
#define POW(c) (1 << (c))
#define MASK(c) (((unsigned long)-1) / (POW(POW(c)) + 1))

int countOnes(unsigned int n);
long long power2BF2 ( int n );
int test();
int test2();
int test3();
#include <iostream>
#include <iomanip>
#include <string>
#include <cstdio>
#include <cstring>
using namespace std;

class student
{
public:
    char name[20];
    char sex[10];
    float math;
    float english;
    float cprogram;
    void input_name();
    void input_sex();
    void input_math();
    void input_english();
    void input_cprogram();
    void input(class student *stu);
    void show_student_massage(class student *stu);
};

void student::input_name()
{
    cout << "输入学生姓名： " << endl;
    cin.getline(name,sizeof(name));
    cout << "学生姓名 ： "<< name << endl;
}

void student::input_sex()
{
    cout << "输入学生性别： " << endl;
    cin.getline(sex,sizeof(sex));
}

void student::input_math()
{
    cout << "输入学生数学： " << endl;
    cin >> math;
}

void student::input_english()
{
    cout << "输入学生英语： " << endl;
    cin >> english;
}

void student::input_cprogram()
{
    cout << "输入学生C语言： " << endl;
    cin >> cprogram;
}

void student::show_student_massage(class student *stu)
{
    cout << "学生姓名 ： "<< stu->name << endl;
    cout << "学生性别 ： "<< stu->sex << endl;
    cout << "学生数学 ： "<< stu->math << endl;
    cout << "学生英语 ： "<< stu->english << endl;
    cout << "学生C语言： "<< stu->cprogram << endl;
}

void student::input(class student *stu)
{
    stu->input_name();
    stu->input_sex();
    stu->input_math();
    stu->input_english();
    stu->input_cprogram();
}

int main(int argc, const char * argv[]) {
    // insert code here...
    /*
    std::cout << "Hello, World!\n";
    std::cout << (2 << 1) << "\n";
    std::cout << countOnes(5) << "\n";
    std::cout << MASK(1) << "\n";
    std::cout << power2BF2(3) << "\n";
    
    //std::cout << maxI([1,2,3,4], 4) << "\n";
     */
    //cout << test3() << "\n";
    student xiaoming;
    student *xiaoming_point = &xiaoming;
    xiaoming.input(xiaoming_point);
    xiaoming.show_student_massage(xiaoming_point);
     
     
    return 0;
     
}



int test ()
{
    // 带有 5 个元素的双精度浮点型数组
    double balance[5] = {1000.0, 2.0, 3.4, 17.0, 50.0};
    double *p;
    
    p = balance;
    
    // 输出数组中每个元素的值
    cout << "使用指针的数组值 " << endl;
    for ( int i = 0; i < 5; i++ )
    {
        cout << "*(p + " << i << ") : ";
        cout << *(p + i) << endl;
    }
    
    cout << "使用 balance 作为地址的数组值 " << endl;
    for ( int i = 0; i < 5; i++ )
    {
        cout << "*(balance + " << i << ") : ";
        cout << *(balance + i) << endl;
    }
    
    return 0;
}

const int MAX = 4;

int test2 ()
{
    const char *names[MAX] = {
        "Zara Ali",
        "Hina Ali",
        "Nuha Ali",
        "Sara Ali",
    };
    
    for (int i = 0; i < MAX; i++)
    {
        cout << "Value of names[" << i << "] = \n";
        cout << names[i] << "   111" << endl;
        cout << *names[i] << "   222" << endl;
        cout << (*names)[i] << "    000  " << endl;
        cout << *names[i+1] << "   333" << endl;
        cout << *names[i]+1 << "   444" << endl;
        cout << *(names[i]+1) << "   555" << endl;
    }
    const char *ps = "Clanguage";
    cout << ps << endl;
    cout << *ps << endl;
    cout << *(ps+1) << endl;
    cout << ps+1 << endl;
    cout << (*ps) + 1 << endl;
    cout << (*ps) + 2 << endl;
    cout << 'C' + 2 << endl;
    
    return 0;
}

void getSeconds(unsigned long *par)
{
    cout << "Value of *par = :" << *par << endl;
    cout << "Value of par = :" << par << endl;
    cout << "Value of &par = :" << &par << endl;
    cout << endl;
    // 获取当前的秒数
    *par = time(NULL);
    cout << "Value of *par = :" << *par << endl;
    cout << endl;
    return;
}
int test3()
{
    unsigned long sec = 0;
    
    cout << "Value of sec = :" << sec << endl;
    cout << "Value of &sec = :" << &sec << endl;
    cout << endl;
    getSeconds(&sec);
    
    // 输出实际值
    cout << "Number of seconds :" << sec << endl;
    
    return 0;
}





// find max
int maxI(int A[], int n){
    int m = INT_MIN;
    for ( int i = 0; i < n; i++){
        m = std::max(m, A[i]);
    }
    return m;
}

int maxR(int A[], int n){
    if( n < 2) //递归基
        return A[n-1];
    else
        return std::max(maxR(A, n-1), A[n-1]);
}

int maxR2(int A[], int lo, int hi){
    if( lo + 1 == hi)
        return A[lo];
    else{
        int mi = (lo + hi) >> 1;
        return std::max(maxR2(A, lo, mi), maxR2(A, mi, hi));
    }
}




// 2 ^ n
long long power2BF ( int n ){
    long long pow = 1;
    while (0 < n--)
        pow <<= 1;
    return pow;
}

long long power2BF2 ( int n ){
    return n > 0 ? 2 * power2BF2( --n ) : 1;
}
long long power2BF3 ( int n ){
    return ( 1 > n ) ? 1 : power2BF3( n - 1 ) << 1;
}



int countOnes(unsigned int n){
    int ones = 0;
    while (0 < n){
        ones += (1 & n);
        n >>= 1;
    }
    return ones;
}

int countOnes2(unsigned int n){
    int ones = 0;
    while (0 < n){
        ones ++;
        n &= n-1;
    }
    return ones;
}
