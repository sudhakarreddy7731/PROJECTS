#include <iostream>
#include <string>
using namespace std;

class Node {
public:
    int roll;
    string name;
    string status;

    int totalClasses;
    int presentCount;
    float percentage;

    Node *left, *right;

    Node(int r, string n) {
        roll = r;
        name = n;
        status = "Not Taken";

        totalClasses = 0;
        presentCount = 0;
        percentage = 0.0;

        left = right = nullptr;
    }
};

class BST {
public:
    Node* root;

    BST() {
        root = nullptr;
    }

    Node* insert(Node* root, int roll, string name) {
        if (root == nullptr)
            return new Node(roll, name);

        if (roll < root->roll)
            root->left = insert(root->left, roll, name);
        else if (roll > root->roll)
            root->right = insert(root->right, roll, name);
        else
            cout << "Roll number already exists!\n";

        return root;
    }

    void addStudent(int roll, string name) {
        root = insert(root, roll, name);
        cout << "Student added!\n";
    }

    void inorderDisplay(Node* root) {
        if (root == nullptr) return;

        inorderDisplay(root->left);

        cout << "Roll: " << root->roll
             << " | Name: " << root->name
             << " | Attendance: " << root->status
             << " | Total Classes: " << root->totalClasses
             << " | Present: " << root->presentCount
             << " | %: " << root->percentage << endl;

        inorderDisplay(root->right);
    }

    void displayAll() {
        cout << "\n--- Student Report ---\n";
        inorderDisplay(root);
    }

    void takeAttendance(Node* root) {
        if (root == nullptr) return;

        takeAttendance(root->left);

        char a;
        cout << "Enter attendance for Roll " << root->roll 
             << " (" << root->name << ") [P/A]: ";
        cin >> a;

        root->totalClasses++;

        if (a == 'P' || a == 'p') {
            root->status = "Present";
            root->presentCount++;
        } 
        else {
            root->status = "Absent";
        }

        root->percentage = ( (float)root->presentCount / root->totalClasses ) * 100;

        takeAttendance(root->right);
    }

    void startAttendance() {
        if (root == nullptr) {
            cout << "No students added!\n";
            return;
        }

        cout << "\n--- Taking Attendance (New Class) ---\n";
        takeAttendance(root);
    }
};

int main() {
    BST obj;
    int choice;

    while (true) {
        cout << "\n--- College Attendance System (BST) ---\n";
        cout << "1. Add Student\n";
        cout << "2. Display Report\n";
        cout << "3. Take Attendance (New Class)\n";
        cout << "4. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        if (choice == 1) {
            int roll;
            string name;

            cout << "Enter Roll: ";
            cin >> roll;

            cout << "Enter Name: ";
            cin.ignore();
            getline(cin, name);

            obj.addStudent(roll, name);
        }
        else if (choice == 2) {
            obj.displayAll();
        }
        else if (choice == 3) {
            obj.startAttendance();
        }
        else if (choice == 4) {
            break;
        }
        else {
            cout << "Invalid choice!\n";
        }
    }

    return 0;
}