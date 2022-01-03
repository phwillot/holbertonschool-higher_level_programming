#include "lists.h"

/**
 * is_palindrome - Check if the singly linked list is a palindrome
 * @head: pointer to pointer of first node of a listint_t list
 *
 * Return: 1 if palindrome, otherwise 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *copy = *head;
	int length = 0, i = 0, array[4096];

	if (*head)
	{
		while (copy)
		{
			array[length] = copy->n;
			copy = copy->next;
			length++;
		}
		while (i < (length / 2))
		{
			if (array[i] != array[length - 1 - i])
				return (0);
			i++;
		}
	}
	return (1);
}
