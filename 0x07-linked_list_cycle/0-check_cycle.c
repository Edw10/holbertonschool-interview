#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - prints all elements of a listint_t list
 * @list: pointer to head of list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *aux, *aux1;

	if (list == NULL)
		return (0);

	aux = list;
	aux1 = list;
	while (aux->next && aux->next->next)
	{
		aux = aux->next->next;
		aux1 = aux1->next;
		if (aux == aux1)
			return (1);
	}
	return (0);
}
