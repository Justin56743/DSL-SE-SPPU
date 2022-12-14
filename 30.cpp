#include <iostream>
#include <list>

template <typename T>
class PriorityQueue {
public:
  PriorityQueue() {}

  void push(const T& item, int priority) {
    // Create a new queue item with the given data and priority
    QueueItem queue_item = {item, priority};

    // Find the position in the list where the new item should be inserted
    // in order to maintain the list in ascending order of priorities
    auto it = items_.begin();
    while (it != items_.end() && it->priority <= priority) {
      ++it;
    }

    // Insert the new item at the appropriate position
    items_.insert(it, queue_item);
  }

  T pop() {
    if (items_.empty()) {
      throw std::out_of_range("The queue is empty");
    }

    // Remove the item with the highest priority from the list
    // and return its data
    T item = items_.front().item;
    items_.pop_front();
    return item;
  }

  bool empty() const {
    return items_.empty();
  }

private:
  // This inner class represents an item in the queue,
  // with its data and priority
  struct QueueItem {
    T item;
    int priority;
  };

  // The list that will store the queue items,
  // in ascending order of priorities
  std::list<QueueItem> items_;
};

int main() 
  // Create a priority queue
  PriorityQueue<std::string> queue;

  // Push some items with different priorities
  queue.push("apple", 5);
  queue.push("banana", 3);
  queue.push("orange", 2);
  queue.push("grapefruit", 1);
  queue
