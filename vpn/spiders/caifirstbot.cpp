#include <iostream>
#include <string>

using namespace std;

int instruction1();
int select();
int Repeat_choice();
int non_vegetarian();

float sum = 0.0;

class vegetarian
{

private:
    char check;
    int choice;

public:
    int Repeat_choice()
    {
    item:
        char key;
        cout << "Step-2: Please press A for veg or B for non-veg" << endl;
        cout << " A -----> Vegetarian                   B -------> Non-vegetarian" << endl;
        cin >> key;
        if (key == 'A' || key == 'a')
        {
            veg();
        }
        else if (key == 'B' || key == 'b')
        {
            non_vegetarian();
        }
        else
        {
            cout << "You have enterd incorrect choice! Please enter correct character" << endl;
            goto item;
        }
        return 0;
    }

    int veg()
    {
    start1:

        cout << "---------------------------Press 1,2,3,4,5 for item, which you want to buy------------------------------" << endl;
        cout << "\n";
        cout << "# # # # # # # # # # # # Attention :: At a time you can press only one number # # # # # # # # # # # # # # " << endl;
        cout << "\n";
        cout << "1 --------> Paneer Makhani : 3 euro" << endl;
        cout << "2 --------> Pizza          : 4 euro" << endl;
        cout << "3 --------> veg. Burger    : 2.5 euro" << endl;
        cout << "4 --------> Daal-Rise      : 2 euro" << endl;
        cout << "5 --------> kaju Angara    : 3 euro" << endl;
        cin >> choice;

        if (choice == 1)
        {
            sum = sum + 3;
        }
        else if (choice == 2)
        {
            sum = sum + 4;
        }
        else if (choice == 3)
        {
            sum = sum + 2.5;
        }
        else if (choice == 4)
        {
            sum = sum + 2;
        }
        else if (choice == 5)
        {
            sum = sum + 3;
        }
        else
        {
            cout << "Invalid choice! please enter correct choice" << endl;
            goto start1;
        }
        cout << "\n";
        cout << "Do you want to buy more 'y' or 'n'" << endl;
        cin >> check;

        if (check == 'y' || check == 'Y')
        {
            Repeat_choice();
        }
        else
        {
            cout << "\n";
            cout << "Your total bill is " << sum;
        }
        return 0;
    }

    int non_vegetarian(void)
    {
    start2:
        char check;
        int choice;

        cout << "----------------------------Press 1,2,3,4,5 for item, which you want to buy-------------------------------" << endl;
        cout << "\n";
        cout << "# # # # # # # # # # # # # Attention :: At a time you can press only one number # # # # # # # # # # # # # #" << endl;
        cout << "\n";
        cout << "1 --------> Chicken Masala  : 4 euro" << endl;
        cout << "2 --------> chicken karry   : 4.5 euro" << endl;
        cout << "3 --------> non_veg. Burger : 3 euro" << endl;
        cout << "4 --------> Barbeque        : 6 euro" << endl;
        cout << "5 --------> chicken         : 2 euro" << endl;
        cin >> choice;

        if (choice == 1)
        {
            sum = sum + 4;
        }
        else if (choice == 2)
        {
            sum = sum + 4.5;
        }
        else if (choice == 3)
        {
            sum = sum + 3;
        }
        else if (choice == 4)
        {
            sum = sum + 6;
        }
        else if (choice == 5)
        {
            sum = sum + 2;
        }
        else
        {
            cout << "Invalid choice! please enter correct choice" << endl;
            goto start2;
        }

        cout << "\n";

        cout << "Do you want to buy more 'y' or 'n'" << endl;
        cin >> check;

        if (check == 'y' || check == 'Y')
        {
            Repeat_choice();
        }
        else
        {
            cout << "\n";
            cout << "Your total bill is " << sum;
        }

        return 0;
    }
    int select()
    {
        char Input;
        char key;
        cout << "Step-2: Please press A for veg or B for non-veg" << endl;
        cout << "Step-3: You will get the bill" << endl;
    item2:
        cin >> Input;

        if (Input == 'F' || Input == 'f')
        {
        item:
            cout << " A -----> Vegetarian                   B -------> Non-vegetarian" << endl;
            cin >> key;
            if (key == 'A' || key == 'a')
            {

                veg();
            }
            else if (key == 'B' || key == 'b')
            {

                non_vegetarian();
            }
            else
            {
                cout << "You have enterd incorrect choice! Please enter correct character" << endl;
                goto item;
            }
        }
        else
        {
            cout << "You have entered wrong key! please enter 'F' " << endl;
            goto item2;
        }
        return 0;
    }
    int instruction1()
    {

        cout << "------------------------------------Welcome to the online food order------------------------------------" << endl;
        cout << "------------------------------ Please follow below instruction for order--------------------------------" << endl;
        cout << "\n";
        cout << "# # # # # # # # # # # # Attention :: You can order both veg. and non-veg food # # # # # # # # # # # # # #" << endl;
        cout << "\n";
        cout << "Step-1: Please press F to order" << endl;
        return 0;
    }
};

int main()
{
    vegetarian order;
    order.instruction1();
    order.select();
    return 0;
}