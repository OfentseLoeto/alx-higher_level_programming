#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Check if a singly linked list conains a cycle
 * @list: Singly linked list
 * Return: If there's no cycle return 0, and return 1 if there is cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *theo, *n;

	if (list == NULL || list->next == NULL)
	return (0);

	theo = list->next;
	n = list->next->next;

	while (theo && n && n->next)
	{
	if (theo == n)
	return (1);

	theo = theo->next;
	n = n->next->next;
	}
	return (0);
}


