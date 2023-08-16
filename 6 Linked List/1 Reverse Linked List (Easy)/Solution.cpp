#include <algorithm>
#include <vector>
#include <iostream>
#include <iterator>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

void printList(ListNode* n) {
    while (n != nullptr) {
        cout << n->val << " ";
        n = n->next;
    }
}

class Solution {
public:
    static ListNode* reverseList(ListNode* head) {
        if (head == nullptr) return nullptr;

        ListNode* prev = nullptr;
        ListNode* curr = head;

        while (curr->next != nullptr) {
            ListNode* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }

        curr->next = prev;

        return curr;
    }
};

int main() {
    ListNode* head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));

    printList(Solution::reverseList(head));
}