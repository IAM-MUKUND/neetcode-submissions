/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
       ListNode* mid = head;
       ListNode* end = head;

       while (end && end -> next){
            end = end -> next -> next;
            mid = mid -> next;
       } 

       ListNode* second = mid -> next;
       mid -> next = nullptr;
       ListNode* prev = nullptr;
       while (second){
            ListNode* temp = second -> next;
            second -> next = prev;
            prev = second;
            second = temp;
       }
       ListNode* p1 = head;
       ListNode* p2 = prev;
       while (p1 && p2){
        ListNode* t1 = p1 -> next;
        ListNode* t2 = p2 -> next;
        p1 -> next = p2;
        p2 -> next = t1;
        p1 = t1;
        p2 = t2;
       }
    }
};
