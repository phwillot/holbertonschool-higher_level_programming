#include "lists.h"

/**
 * insert_node - Insert a number into a sorted singly linked list
 * @head: pointer of pointer of struct listint_t
 * @number: int
 *
 * Return: Adress of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *temp = *head, *temp2 = *head;

	if (head == NULL)
		return (NULL);
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);

	newnode->n = number;
	if (*head == NULL)
	{
		newnode->next = NULL;
		*head = newnode;
		return (newnode);
	}
	else
	{
		while (temp->next != NULL)
		{
			if (number < temp->n)
			{
				newnode->next = *head;
				*head = newnode;
				return (newnode);
			}
			if (number < temp->next->n && number > temp->n)
			{
				temp2 = temp, temp2 = temp2->next;
				temp->next = newnode;
				newnode->next = temp2;
			}
			else
				temp = temp->next;
		}
	}
	temp->next = newnode;
	newnode->next = NULL;
	return (newnode);
}
