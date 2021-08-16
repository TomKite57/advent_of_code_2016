#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <numeric>

std::vector<std::vector<int>> parse_file(std::string fname)
{
    std::ifstream file;
    std::string str, tmp;
    int val1, val2, val3;
    std::vector<std::vector<int>> rval;

    file.open(fname);
    while(getline(file, str))
    {
        std::stringstream sstream(str);
        sstream >> tmp;
        val1 = std::stoi(tmp);
        sstream >> tmp;
        val2 = std::stoi(tmp);
        sstream >> tmp;
        val3 = std::stoi(tmp);
        rval.push_back({val1, val2, val3});
    }
    file.close();

    return rval;
}


bool valid_triangle(std::vector<int> tri)
{
    int a=tri[0], b=tri[1], c=tri[2];
    return (a+b>c && a+c>b && b+c>a);
}


std::vector<std::vector<int>> rotate_list(std::vector<std::vector<int>> in)
{
    std::vector<std::vector<int>> rval;
    for (auto it=in.begin(); it<in.end(); it++)
    {
        std::vector<int> tmp1, tmp2, tmp3;
        tmp1.push_back((*it)[0]); tmp2.push_back((*it)[1]); tmp3.push_back((*it)[2]);
        it++;
        tmp1.push_back((*it)[0]); tmp2.push_back((*it)[1]); tmp3.push_back((*it)[2]);
        it++;
        tmp1.push_back((*it)[0]); tmp2.push_back((*it)[1]); tmp3.push_back((*it)[2]);

        rval.push_back(tmp1); rval.push_back(tmp2); rval.push_back(tmp3);
    }
    return rval;
}


int main()
{
    auto accumulator = [](int accum, std::vector<int> tri) {if (valid_triangle(tri)) return accum+1; return accum;};

    std::vector<std::vector<int>> triangles = parse_file("data/day_03.dat");
    std::cout << std::accumulate(triangles.begin(), triangles.end(), 0, accumulator) << std::endl;

    triangles = rotate_list(triangles);
    std::cout << std::accumulate(triangles.begin(), triangles.end(), 0, accumulator) << std::endl;

    return 0;
}
