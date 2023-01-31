#ifndef LISTS_H
#define LISTS_H
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * struct listint_s - Singly liked list
 * @n: Integer
 * @next: Pointer to the next node
 *
 * Description: Singly linked list structure
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;

} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
listint_t *insert_node(listint_t **head, int number);


def islower(c) :
def uppercase(str) :
def print_last_digit(number) :
def add(a, b) :
def pow(a, b) :
def fizzbuzz(void) :
def remove_char_at(str, n):

#endif /* LISTS_H */
