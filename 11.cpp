/*
    要将10000日元兑换为1日元、5日元、10日元、50元、100元、500日元、1000元、2000元、5000元的零钱,请问有多少种兑换方法?

    动态规划问题,for use:g++ -o 11 11.cpp
*/
#include <iostream>
#include <ctime>
#include <map>

using namespace std;

int x[10]={0,5000,2000,1000,500,100,50,10,5,1};
map<int, map<int, int> > cache;//二维数组

long long solve( int y , int k )
{
    int &solves = cache[k][y];//对子结果进行缓存
    if(solves > 0){
        return solves;
    }
     
    if(y==0){
        return 1;
    }
    
    if(k==8){//减少一重for循环
        return y/5+1;
    }

    long long t=0;
    for(int i=0; i*x[k]<=y; i++){
        t+=solve(y-i*x[k] , k+1);
    }
    
    solves = t;//对子结果进行缓存
    return t;
}

int main()
{
    clock_t start,end;
    start = clock();
    cout<<"Count = "<<solve(10000,1)<<"\n";
    end = clock();
    cout <<"Time = "<<end-start<<" ms\n";
    return 0;
}
