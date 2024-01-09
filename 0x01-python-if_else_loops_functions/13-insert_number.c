#include "lists.h"
/**
 * insert_node - function inserts number into sorted string
 * @head: double pointer to first node
 * @number: number to be inserted
 * Return: pointer to head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;
	listint_t *previous;

	current = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (*head)
	}

	if (current->n > number)
	{
		new_node->next = current;
		*head = new_node;
		return (*head);
	}
	while (current->next != NULL)
	{
		if (current->n < number)
		{
			previous = current;
			current = current->next;
			continue;
		}
		previous->next = new_node;
		new_node->next = current;
		break;

	}
	if (current->n < number)
		current->next = new_node;

	return (*head);
}

