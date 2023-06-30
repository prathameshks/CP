//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    struct Node* next;

    Node(int x) {
        data = x;
        next = NULL;
    }
};

// } Driver Code Ends
/*
// structure of the node is as follows

struct Node
{
        int data;
        struct Node* next;

        Node(int x){
            data = x;
            next = NULL;
        }

};

*/
class Solution {
   public:
    struct Node* merge(struct Node*& head1, struct Node*& head2) {
        // code here
        struct Node* temp1 = head1;
        struct Node* temp2 = head2;
        struct Node* ans = new struct Node(0);
        struct Node* temp3 = ans;

        while (temp1 != NULL && temp2 != NULL) {
            if (temp1->data > temp2->data) {
                temp3->next = temp2;
                temp3 = temp2;
                temp2 = temp2->next;
                temp3->next = NULL;
            } else if (temp1->data < temp2->data) {
                temp3->next = temp1;
                temp3 = temp1;
                temp1 = temp1->next;
                temp3->next = NULL;
            } else {
                temp3->next = temp2;
                temp3 = temp2;
                temp2 = temp2->next;
                temp1 = temp1->next;
                temp3->next = NULL;
            }
        }

        if (temp1) {
            temp3->next = temp1;
        }
        if (temp2) {
            temp3->next = temp2;
        }
        temp3 = ans;
        ans = ans->next;
        delete temp3;
        return ans;
    } 

    struct Node* mergeSort(struct Node*& head) {
        // code here
        if (head == NULL || head->next == NULL) {
            return head;
        }

        // cout << x++ << endl;
        // printList(head);

        struct Node* temp1 = head;
        struct Node* temp2 = head;
        temp2 = temp2->next;
        if (temp2 != NULL) temp2 = temp2->next;

        while (temp2 != NULL) {
            temp1 = temp1->next;
            temp2 = temp2->next;
            if (temp2 != NULL) temp2 = temp2->next;
        }

        if (temp1 != NULL) {
            temp2 = temp1->next;
            temp1->next = NULL;
        } else {
            temp2 = NULL;
        }
        temp1 = head;

        temp1 = mergeSort(temp1);
        temp2 = mergeSort(temp2);

        struct Node* ans = merge(temp1, temp2);
        return ans;
    }

    struct Node* makeUnion(struct Node* head1, struct Node* head2) {
        // code here
        struct Node* temp1 = head1;
        struct Node* temp2 = head2;

        temp1 = mergeSort(temp1);
        temp2 = mergeSort(temp2);
        struct Node* ans = merge(temp1, temp2);

        return ans;
    }
};

//{ Driver Code Starts.

struct Node* buildList(int size) {
    int val;
    cin >> val;

    Node* head = new Node(val);
    Node* tail = head;

    for (int i = 0; i < size - 1; i++) {
        cin >> val;
        tail->next = new Node(val);
        tail = tail->next;
    }

    return head;
}

void printList(Node* n) {
    while (n) {
        cout << n->data << " ";
        n = n->next;
    }
    cout << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m;

        cin >> n;
        Node* first = buildList(n);

        cin >> m;
        Node* second = buildList(m);
        Solution obj;
        Node* head = obj.makeUnion(first, second);
        printList(head);
    }
    return 0;
}

// } Driver Code Ends