struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){

    struct ListNode *init_node, *curr;
    int l1_val, l2_val, total, digit, carry;

    init_node = malloc(sizeof(struct ListNode));
    init_node->val = 0;
    init_node->next = NULL;
    curr = init_node;
    l1_val = 0;
    l2_val = 0;
    total = 0;
    digit = 0;
    carry = 0;

    while (l1 || l2 || carry){
        if (l1){
            l1_val = l1->val;
        } else {
            l1_val = 0;
        };

        if (l2){
            l2_val = l2->val;
        } else {
            l2_val = 0;
        };
 
        // process node
        total = l1_val + l2_val + carry;
        digit = total%10;
        carry = total/10;
        curr->val = digit;

        // move pointer
        if (l1) l1 = l1->next;
        if (l2) l2 = l2->next;

        if (l1 || l2 || carry){
            struct ListNode *next_node;
            next_node = malloc(sizeof(struct ListNode));
            next_node->val = 0;
            next_node->next = NULL;

            curr->next = next_node;
            curr = curr->next;
        }

    };
    
    return init_node;

}