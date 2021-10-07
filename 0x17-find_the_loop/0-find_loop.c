#include "lists.h"

/**
 * find_listint_loop - Finds the loop in a linked list
 * @head: Pointer to the head of the linked list
 *
 * Return: The address of the loop node, NULL otherwise
 */
listint_t *find_listint_loop(listint_t *head)
{
listint_t *p = head;
listint_t *q = head;

if (!head)
return (NULL);
while (q && q->next)
{
p = p->next;
q = q->next->next;
if (p == q)
{
p = head;
while (p != q)
{
p = p->next;
q = q->next;
}
return (q);
}
}
return (NULL);
}
