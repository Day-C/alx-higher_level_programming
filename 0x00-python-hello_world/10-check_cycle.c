#include "lists.h"
/**
 * check_cycle - function check for infinile list
 * @list: first node of list
 *
 * Description: the idea of this code is to take node of the first node
 * and wile traversing the list if it appears many times then
 * its aninfinite list.
 *
 * Return: return 0 on success otherwise 1
 */
int check_cycle(listint_t *list)
{
	int number, repits = -1;
	listint_t *current;

	current = list;
	if (list == NULL)
		return (1);

	number = list->n;
	while (current)
	{
		if (current->n == number)
			repits++;
		if (repits >= 5)
			return (1);
		current = current->next;
	}
	return (0);
}

