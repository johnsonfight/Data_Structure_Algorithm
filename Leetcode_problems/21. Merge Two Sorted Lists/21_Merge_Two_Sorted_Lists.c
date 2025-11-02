/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode* head = (struct ListNode*)malloc(sizeof(struct ListNode));
    head->val = 0;
    head->next = NULL;

    struct ListNode* current = head;

    while (list1 && list2){
        if (list1->val < list2->val){
            current->next = list1;
            list1 = list1->next;
        }else{
            current->next = list2;
            list2 = list2->next;
        }
        current = current->next;
    }

    current->next = (list1 == NULL) ? list2 : list1;

    return head->next;
}