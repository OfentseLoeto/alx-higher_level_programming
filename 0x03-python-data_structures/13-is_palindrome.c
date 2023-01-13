#include "lists.h"

/**
 * is_palindrome - Check if a singly linked list is a palindrome
 * @head: pointer to the beggining of the list
 *
 * Return: 1 if is palindrome else 0
 */

int is_palindrome(listint_t **head);
{
	if (head == NULL || *head == NULL)
	return (1);

	return (check_pal(head, *head));
}

/**
 * check_pal - check if a list is a palindrome
 * @head: pointer to the beggining of the list
 * @last: pointe to the last of the list
 *
 * Return: 0 if is not palindrome else 1
 */

int check_pal(listint_t **head, listint_t *last)
{
	if (last == NULL)
	return (1);

	if (check_pal(head, last->next) && (*head)->n == last->n)

	{
	*head = (*head)->next;
	return (1);
	}
	return (0);
}
