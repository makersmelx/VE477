#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

void randperm(int Num)
{
    vector<int> temp;
    for (int i = 0; i < Num; ++i)
    {
        temp.push_back(i + 1);
    }

    random_shuffle(temp.begin(), temp.end());

    for (int i = 0; i < temp.size(); i++)
    {
        cout << temp[i] << " ";
    }
}

int main(int argc, char **argv)
{
    int num = stoi(argv[1]);
    cout << num * (num + 1) / 4 << endl;
    randperm(num);
}
