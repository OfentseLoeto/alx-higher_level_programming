#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
#include <stdio.h>

/**
 * struct listint_s - Singly linked list
 * @n: interger
 * @next: pointer to the next node
 * Description: singly linked list node structure
 */

typedef struct listint_s

{
       	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint_t(listint_t *head);
int check_pal(listint_t **head, listint_t *last);
int is_palindrome(listint_t **head);
def replace_in_list(my_list, idx, element):
def element_at(my_list, idx):

#endif /*LISTS_H*/ 
