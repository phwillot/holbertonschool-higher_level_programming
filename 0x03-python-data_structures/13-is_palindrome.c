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
	int length = 0, i = 0, *array;

	if (*head)
	{
		while (copy)
		{
			copy = copy->next;
			length++;
		}
		array = malloc(sizeof(int) * length);
		if (array == NULL)
			return (0);
		while (copy)
		{
			array[i] = copy->n;
			copy = copy->next;
			i++;
		}
		i = 0;
		while (i < (length / 2))
		{
			if (array[i] != array[length - 1 - i])
			{
				free(array);
				return (0);
			}
			i++;
		}
	}
	free(array);
	return (1);
}
