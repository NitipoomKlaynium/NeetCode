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
    static ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (list1 == nullptr && list2 == nullptr) return nullptr;
        if (list1 == nullptr) return list2;
        if (list2 == nullptr) return list1;
    
        ListNode* head;
        ListNode* p1 = list1;
        ListNode* p2 = list2;

        if (p1->val < p2->val) {
            head = new ListNode(p1->val);
            p1 = p1->next;
        }
        else {
            head = new ListNode(p2->val);
            p2 = p2->next;
        }

        ListNode* curr = head;

        while(p1 != nullptr && p2 != nullptr) {
            if (p1->val < p2->val) {
                curr->next = new ListNode(p1->val);
                curr = curr->next;
                p1 = p1->next;
            }
            else {
                curr->next = new ListNode(p2->val);
                curr = curr->next;
                p2 = p2->next;
            }
        }

        while(p1 != nullptr) {
            curr->next = new ListNode(p1->val);
            curr = curr->next;
            p1 = p1->next;
        }

        while(p2 != nullptr) {
            curr->next = new ListNode(p2->val);
            curr = curr->next;
            p2 = p2 ->next;
        }

        return head;
    }
};

int main() {
    ListNode* list1 = new ListNode(1);
    ListNode* list2 = new ListNode(2);

    printList(Solution::mergeTwoLists(list1, list2));
}