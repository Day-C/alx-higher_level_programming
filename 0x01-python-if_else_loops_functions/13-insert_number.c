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
	previous = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return NULL;
	new_node->n = number;
	new_node->next = NULL;

	while (current)
	{
		if (current->n > number)
			new_node->next = current

		if (current->n < number)
		{
			current = current->next;
			continue;
		}
