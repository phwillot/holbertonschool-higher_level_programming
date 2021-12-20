#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr1, *ptr2;

	ptr1 = ptr2 = list;
	while (ptr2->next)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
		if (ptr1 == ptr2)
			return (1);
	}
	return (0);
}
