#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <tuple>
#include <algorithm>

std::string remove_char(std::string input, char ch1)
{
    std::string output;
    std::copy_if(input.begin(), input.end(), std::back_inserter(output), [ch1](char ch2) { return ch2 != ch1; });
    return output;
}

int get_steps(std::string input)
{
    std::string output;
    std::copy(input.begin()+1, input.end(), std::back_inserter(output));
    return std::stoi(output);
}

std::vector<std::string> parse_file(std::string fname)
{
    std::ifstream file;
    //std::sstream content;
    std::string temp;
    std::vector<std::string> rval;

    file.open(fname);
    while(file >> temp)
    {
        rval.push_back(remove_char(temp, ','));
    }
    file.close();

    return rval;
}

void rotate(int &direc, std::string instruction)
{
    if (instruction[0] == 'R')
        direc = (direc + 1)%4;
    else
        direc = (direc - 1)%4;

    if (direc < 0)
        direc += 4;
}

void move(int &x, int &y, int &direc)
{
    if (direc == 0)
        y+=1;
    else if (direc == 1)
        x+=1;
    else if (direc == 2)
        y-=1;
    else if (direc == 3)
        x-=1;
}

bool repeated_location(std::vector<std::tuple<int, int>> positions, int x, int y)
{
    for (auto it=positions.begin(); it < positions.end(); it++)
    {
        if (std::get<0>(*it) == x && std::get<1>(*it) == y)
            return true;
    }

    return false;
}

int main()
{
    int x=0, y=0, direc=0;
    int fx=-1, fy=-1;
    std::vector<std::tuple<int, int>> positions;
    bool found = false;
    std::vector<std::string> directions = parse_file("data/day_01.dat");

    positions.push_back(std::make_tuple(0, 0));

    for (int i=0; i<directions.size(); i++)
    {
        rotate(direc, directions[i]);
        for (int j=0; j<get_steps(directions[i]); j++)
        {
            move(x, y, direc);
            if (!found && repeated_location(positions, x, y))
            {
                found = true;
                fx = x;
                fy = y;
            }
            positions.push_back(std::make_tuple(x, y));
        }
    }

    std::cout << "Total distance: " << abs(x) + abs(y) << std::endl;
    std::cout << "First repeat: " << abs(fx) + abs(fy) << std::endl;

    return 0;
}
