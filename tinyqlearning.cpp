#include<bits/stdc++.h>
#define ll long long
#define ld long double
using namespace std;
fstream f1;
ld epsilon=0.3,gamma=0.9,alpha=0.1;
vector<vector<ld>> vec(2, vector<ld>(3, 0));
vector<ll> reward = {1, 5, 2};
vector<vector<ld>> poss0 = {{0.1, 0.4, 0.5},{0.4, 0.2, 0.4},{0.3,0.7,0}};
vector<vector<ld>> poss1 = {{0.2, 0.6, 0.2},{0.5,0.25,0.25},{0.3,0.1,0.6}};
void fun1()
{
    f1.open("offlinedata.txt", ios::in);
    if(f1.is_open())
    {
        for (ll i = 0; i < 2;++i)
        {
            for (ll j = 0; j < 3;++j) f1 >> vec[i][j];
        }
        f1.close();
    }
}
void fun2()
{
    f1.open("offlinedata.txt", ios::out);
    for (ll i = 0; i < 2;++i)
    {
        for (ll j = 0; j < 3;++j) f1 << vec[i][j] <<" ";
        f1 << '\n';
    }
    f1.close();
}
int fun3(int state0,int action0)
{
    int state1;
    ld t = (rand()%100)/100.0;
    if(action0==0)
    {
        if(t<poss0[state0][0]) state1 = 0;
        else if(t<poss0[state0][0]+poss0[state0][1]) state1 = 1;
        else state1 = 2;
    }
    else
    {
        if(t<poss1[state0][0]) state1 = 0;
        else if(t<poss1[state0][0]+poss1[state0][1]) state1 = 1;
        else state1 = 2;
    }
    return state1;
}
int main()
{
    srand(time(NULL));
    fun1();
    int state0 = rand() % 3,state1=0;
    int action=0;
    cout << "begin state: " << state0 + 1 << '\n';
    cout << "        state1\tstate2\tstate3\n";
    cout << "action1 ";
    for (int j = 0; j < 2;++j) cout << vec[0][j] << '\t';
    cout <<vec[0][2]<< "\naction2 ";
    for (int j = 0; j < 2;++j) cout << vec[1][j] << '\t';
    cout <<vec[1][2]<< '\n';
    ld t=(rand()%100)/100.0;
    if(t>epsilon) action = vec[0][state0] > vec[1][state0] ? 0 : 1;
    else action = rand() % 2;
    state1 = fun3(state0,action);
    vec[action][state0] += alpha*(reward[state1] + gamma*max(vec[0][state1],vec[0][state1])-vec[action][state0]);
    state0 = state1;
    for (int i = 1; i < 100; ++i)
    {
        t=(rand()%100)/100.0;
        if(t>epsilon) action = vec[0][state1] > vec[1][state1] ? 0 : 1;
        else action = rand() % 2;
        state1 = fun3(state0,action);
        vec[action][state0] += alpha*(reward[state1] + gamma*max(vec[0][state1],vec[0][state1])-vec[action][state0]);
        state0 = state1;
    }
    fun2();
    cout<<"end state: "<<state1 + 1<<'\n';
    cout << "        state1\tstate2\tstate3\n";
    cout << "action1 ";
    for (int j = 0; j < 2;++j) cout << vec[0][j] << '\t';
    cout <<vec[0][2]<< "\naction2 ";
    for (int j = 0; j < 2;++j) cout << vec[1][j] << '\t';
    cout <<vec[1][2]<< '\n';
    return 0;
}