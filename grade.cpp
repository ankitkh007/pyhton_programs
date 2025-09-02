#include <iostream>

int main()
{
    int marks;
    std::cout << "Enter your marks:";
    std::cin >> marks;
    if (marks >= 90)
    {
        std::cout << "Grade O";
    }
    else if (marks >= 80)
    {
        std::cout << "Grade A";
    }
    else if (marks >= 70)
    {
        std::cout << "Grade B";
    }
    else if (marks >= 50)
    {
        std::cout << "Grade C";
    }
    else if (marks >= 30)
    {
        std::cout << "Grade D";
    }
    else
    {
        std::cout << "Grade F";
    }
    return 0;
}