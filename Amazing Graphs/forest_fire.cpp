/*
    C++
    forest_fire.cpp
    2019.08
    https://oeis.org/A229037
Sequence of positive integers where each is chosen 
to be as small as possible subject to the condition that 
no three terms a(j), a(j+k), a(j+2k) (for any j and k) 
form an arithmetic progression.
*/


#include <iostream>
#include <fstream>
#include <array>


const int NO_POINTS = 100;


bool three_points_same_distance(std::array<int, NO_POINTS> nums, int X) {
    for (int x=X-1; x>=X/2; --x) {
        if ((2*nums[x] - nums[X]) == nums[2*x - X]) {
            return true;
        }
    }
    return false;
}


std::array<int, NO_POINTS> forest_fire() {
    std::array<int, NO_POINTS> nums = {1,1};
    int attempt;
    for (int X=2; X<NO_POINTS; ++X) {
        std::cout << X << "\n";
        attempt = 1;
        while(1) {
            nums[X] = attempt;
            if (three_points_same_distance(nums, X)) {
                attempt += 1;
            } else {
                break;
            }
        }
    }
    return nums;
}


int main() {
    std::array<int, NO_POINTS> nums;
    nums = forest_fire();

    std::cout << "Writing to file \'test.txt\'" << "\n";
    std::ofstream my_file;

    my_file.open("test.txt");
    my_file << "[";
    for (int i=0; i<NO_POINTS-1; i++) {
        my_file << nums[i] << ", ";
    }
    my_file << nums[NO_POINTS-1] << "]" << "\n";
    my_file.close();
    
    return 0;
}
