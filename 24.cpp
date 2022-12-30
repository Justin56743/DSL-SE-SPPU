#include <iostream>

using namespace std;

struct Node {
  int data;
  Node *next;
  Node *prev;
};

Node *head = NULL;

// Insert an element into the set
void insert(int x) {
  Node *node = new Node;
  node->data = x;
  node->next = head;
  node->prev = NULL;
  if (head != NULL) {
    head->prev = node;
  }
  head = node;
}

// Remove an element from the set
void remove(int x) {
  Node *node = head;
  while (node != NULL && node->data != x) {
    node = node->next;
  }
  if (node == NULL) {
    return;
  }
  if (node->prev != NULL) {
    node->prev->next = node->next;
  }
  if (node->next != NULL) {
    node->next->prev = node->prev;
  }
  if (node == head) {
    head = node->next;
  }
  delete node;
}

// Check if an element is in the set
bool find(int x) {
  Node *node = head;
  while (node != NULL && node->data != x) {
    node = node->next;
  }
  return node != NULL;
}

int main() {
  // Insert some elements into the set
  insert(1);
  insert(2);
  insert(3);
  insert(4);

  // Check if the elements are in the set
  cout << find(1) << endl; // should print 1
  cout << find(2) << endl; // should print 1
  cout << find(3) << endl; // should print 1
  cout << find(4) << endl; // should print 1
  cout << find(5) << endl; // should print 0

  // Remove an element from the set
  remove(3);

  // Check if the element is still in the set
  cout << find(3) << endl; // should print 0

  return 0;
}
