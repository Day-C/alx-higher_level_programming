#include "lists.h"
/**
 * node_count - function counts the number of nodes in  singly linked list
 * @head: pointer to first node
 * Return: number of nodes
 */
int node_count(listint_t *head)
{
	int count = 0;

	while (head)
	{
		count++;
		head = head->next;
	}
	return (count);
}
/**
 * is_palindrome - fnction checks if linked list is a palindrome
 * @head: pointer to a pointer to head(first node)
 * Return: return 1 on success otherwise -1
 *
 * Description: i sold this problem by allocating a block of memory
 * to contain every item of the linked list.
 * Then filled the memory block from the last index to the first
 * wile looping throught the linked list
 * Note: the items the memory block are in reverse compared to the liked list
 * finally i compared them with and retur -1 if there are differeced
 * and 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	int a, i,  count = 0;
	listint_t *current, *temp;
	int *ptr;

	if (head == NULL)
		return (0);

	count = node_count(*head);
	current = *head;
	ptr = malloc(sizeof(int) * count);
	a = count;
	while (current)
	{
		ptr[a] = current->n;
		temp = current->next;
		current = temp;
		a--;
	}
	temp = NULL;
	i = 0;
	while (current)
	{
		if (current->n != ptr[i])
		{
			free_listint(*head);
			free(ptr);
			return (-1);
		}
		temp = current->next;
		current = temp;
		i++;
	}
	return (1);
}
