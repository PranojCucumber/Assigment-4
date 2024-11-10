# creation of the task class to store the task information
class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):

        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    # method to rturn a string for task debugging process
    def __repr__(self):
        
        return f"Task({self.task_id}, {self.priority}, {self.arrival_time}, {self.deadline})"

    # method to define compariosn based priorities for max-heap ordering
    def __lt__(self, other):

        return self.priority > other.priority 

# creation of the class for major operations
class PriorityQueue:

    # method to initialise an empty priority queue
    def __init__(self):

        self.heap = []

    # method to insert a new task to the priority queue, maintaining the heap property
    def insert(self, task):

        self.heap.append(task)  # Add the task at the end of the heap
        self._bubble_up(len(self.heap) - 1)  # Restore the heap property

    # method to bubble up the task index to maintain the heap property
    def _bubble_up(self, index):

        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:  # Max-heap: higher priority tasks at the top
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]  # Swap
                index = parent
            else:
                break

    # method to extract and return the task with the highest priority
    def extract_max(self):

        if len(self.heap) == 0:
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]  # Swapping of the roots
        max_task = self.heap.pop()  # highest priority task removal
        self._bubble_down(0)
        return max_task

    # method to restore or bubble down to maintain the heap property
    def _bubble_down(self, index):

        n = len(self.heap)
        while 2 * index + 1 < n:  
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index
            # finding out the largest among index, left child, and right child
            if left < n and self.heap[left] < self.heap[largest]:
                largest = left
            if right < n and self.heap[right] < self.heap[largest]:
                largest = right
            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    # method to increase the priority of a given task and adjusting the heap position
    def increase_key(self, task, new_priority):

        task.priority = new_priority 
        index = self.heap.index(task) 
        self._bubble_up(index)

    # method to decrease the priority of a given task and adjusting the heap position
    def decrease_key(self, task, new_priority):

        task.priority = new_priority 
        index = self.heap.index(task)
        self._bubble_down(index)

    # method to check if the priority queue is empty or not
    def is_empty(self):

        return len(self.heap) == 0


# creating an example usuage
def main():
    # example of tasks (task_id, priority, arrival_time, deadline)
    task1 = Task(1, 10, 0, 5)
    task2 = Task(2, 5, 1, 10)
    task3 = Task(3, 8, 2, 15)

    pq = PriorityQueue()

    # task insertion into the heap
    pq.insert(task1)
    pq.insert(task2)
    pq.insert(task3)

    # Extracting high priority task
    print(pq.extract_max())

    # Increasing priority of a task
    pq.increase_key(task2, 12)

    # extracton of the task with the highest priority after change of priority
    print(pq.extract_max())

# running the code
if __name__ == "__main__":
    main()
