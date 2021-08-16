#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <tuple>
#include <map>

std::vector<std::string> parse_file(std::string fname)
{
    std::ifstream file;
    std::string temp;
    std::vector<std::string> rval;

    file.open(fname);
    while(getline(file, temp))
        rval.push_back(temp);
    file.close();

    return rval;
}

int main()
{
    char pos;
    std::vector<std::string> instructions = parse_file("data/day_02.dat");
    std::map<std::tuple<char, char>, char> geometry_p1 {
        {{'1', 'U'}, '1'}, {{'1', 'D'}, '4'}, {{'1', 'L'}, '1'}, {{'1', 'R'}, '2'},
        {{'2', 'U'}, '2'}, {{'2', 'D'}, '5'}, {{'2', 'L'}, '1'}, {{'2', 'R'}, '3'},
        {{'3', 'U'}, '3'}, {{'3', 'D'}, '6'}, {{'3', 'L'}, '2'}, {{'3', 'R'}, '3'},
        {{'4', 'U'}, '1'}, {{'4', 'D'}, '7'}, {{'4', 'L'}, '4'}, {{'4', 'R'}, '5'},
        {{'5', 'U'}, '2'}, {{'5', 'D'}, '8'}, {{'5', 'L'}, '4'}, {{'5', 'R'}, '6'},
        {{'6', 'U'}, '3'}, {{'6', 'D'}, '9'}, {{'6', 'L'}, '5'}, {{'6', 'R'}, '6'},
        {{'7', 'U'}, '4'}, {{'7', 'D'}, '7'}, {{'7', 'L'}, '7'}, {{'7', 'R'}, '8'},
        {{'8', 'U'}, '5'}, {{'8', 'D'}, '8'}, {{'8', 'L'}, '7'}, {{'8', 'R'}, '9'},
        {{'9', 'U'}, '6'}, {{'9', 'D'}, '9'}, {{'9', 'L'}, '8'}, {{'9', 'R'}, '9'},
    };
    std::map<std::tuple<char, char>, char> geometry_p2 {
        {{'1', 'U'}, '1'}, {{'1', 'D'}, '3'}, {{'1', 'L'}, '1'}, {{'1', 'R'}, '1'},
        {{'2', 'U'}, '2'}, {{'2', 'D'}, '6'}, {{'2', 'L'}, '2'}, {{'2', 'R'}, '3'},
        {{'3', 'U'}, '1'}, {{'3', 'D'}, '7'}, {{'3', 'L'}, '2'}, {{'3', 'R'}, '4'},
        {{'4', 'U'}, '4'}, {{'4', 'D'}, '8'}, {{'4', 'L'}, '3'}, {{'4', 'R'}, '4'},
        {{'5', 'U'}, '5'}, {{'5', 'D'}, '5'}, {{'5', 'L'}, '5'}, {{'5', 'R'}, '6'},
        {{'6', 'U'}, '2'}, {{'6', 'D'}, 'A'}, {{'6', 'L'}, '5'}, {{'6', 'R'}, '7'},
        {{'7', 'U'}, '3'}, {{'7', 'D'}, 'B'}, {{'7', 'L'}, '6'}, {{'7', 'R'}, '8'},
        {{'8', 'U'}, '4'}, {{'8', 'D'}, 'C'}, {{'8', 'L'}, '7'}, {{'8', 'R'}, '9'},
        {{'9', 'U'}, '9'}, {{'9', 'D'}, '9'}, {{'9', 'L'}, '8'}, {{'9', 'R'}, '9'},
        {{'A', 'U'}, '6'}, {{'A', 'D'}, 'A'}, {{'A', 'L'}, 'A'}, {{'A', 'R'}, 'B'},
        {{'B', 'U'}, '7'}, {{'B', 'D'}, 'D'}, {{'B', 'L'}, 'A'}, {{'B', 'R'}, 'C'},
        {{'C', 'U'}, '8'}, {{'C', 'D'}, 'C'}, {{'C', 'L'}, 'B'}, {{'C', 'R'}, 'C'},
        {{'D', 'U'}, 'B'}, {{'D', 'D'}, 'D'}, {{'D', 'L'}, 'D'}, {{'D', 'R'}, 'D'},
    };

    pos='5';
    for (auto const& path : instructions)
    {
        for (auto const& direc : path)
            pos = geometry_p1[std::make_tuple(pos, direc)];
        std::cout << pos;
    }
    std::cout << std::endl;

    pos='5';
    for (auto const& path : instructions)
    {
        for (auto const& direc : path)
            pos = geometry_p2[std::make_tuple(pos, direc)];
        std::cout << pos;
    }
    std::cout << std::endl;

    return 0;
}
