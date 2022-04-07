class Queue:
    """
    This is the Queue class. This is where you will be implementing
    your functions for queue
    """
    def __init__(self):
        self.queue = []

    def is_empty(self) -> bool:
        if not self.queue: 
            return True  
        else : 
            return False  
        """
        This function should return True is the queue is
        empty and False if the queue is not empty.
        :return: A boolean
        """
        

    def enqueue(self, e) -> None:
        self.queue+= [e]
 
        """
        This function add an element to the queue
        :param e: the element we want you to add
        :return: None
        """
        

    def dequeue(self):

        tmp = self.queue[0]
        self.queue.remove(self.queue[0])

        return tmp 

        """
        This function remove and return the first element
        of the list.
        :return: The first element of the list
        """
        
