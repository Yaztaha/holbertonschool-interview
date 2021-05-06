#include "binary_trees.h"

/**
 * swap - swap nodes if it's bigger than the parent
 * @node: node's pointer.
 * Return: new node.
 */
heap_t *swap(heap_t *node)
{
while (node && node->parent)
{
while (node->n > node->parent->n)
{
node = node->parent;
node->n += node->parent->n;
node->parent->n -= node->n;
node->parent->n = node->n - node->parent->n;
}
}
return (node);
}


/**
 * heap_insert - insert value into binary tree with Max heap order.
 * @root: heap root node.
 * @value: node's value.
 * Return: binary tree ordered in a max heap.
 */
heap_t *heap_insert(heap_t **root, int value)
{
heap_t *node, *parent;
if (*root == NULL)
{
node = binary_tree_node(*root, value);
*root = node;
return (*root);
}
node = *root;
while (node != NULL)
{
parent = node;
if (node->n == value)
return (swap(node));
if (value > node->n)
node = parent->left;
else
node = node->right;
}
if (value > parent->n)
{
parent->left = binary_tree_node(parent, value);
return (parent->left);
}
else
{
parent->right = binary_tree_node(parent, value);
return (parent->right);
}
}
