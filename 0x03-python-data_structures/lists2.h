#ifndef "lists.h"
#define "lists.h"
#include <stdio.h>
#include <stdlib.h>


/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next nst_integer(my_list=[]):
 *
 * Description: singly linked list node structure
 */

typedef struct listint_s

{
	int n;
	struct listint_s *next
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_pal(listint_t **head, listint_t *last);
int is_palindrome(listint_t **head);
def print_list_integer(my_list=[]):
def element_at(my_list, idx):
def new_in_list(my_list, idx, element):
#endif /*LISTS_H */
