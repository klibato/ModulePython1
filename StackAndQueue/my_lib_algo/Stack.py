class Stack:
    """
    This is the Stack class. This is where you will be
    implementing your function.
    """

    def __init__(self):
        self.stack = []

    def is_empty(self) -> bool:
        if not self.stack: 
            return True  
        else : 
            return False
        """
        This function should return True is the stack is
        empty and False if the stack is not empty.
        :return: A boolean
        """
        

    def push(self, e) -> None:
        self.stack += [e]
        """
        This function should push an element to the stack.
        :param: e
        :return: None
        """
        

    def pop(self):

        tmp = self.stack[-1]

        self.stack.reverse()
        self.stack.remove(self.stack[0])
        self.stack.reverse()
        return tmp
        
        """
        This function should remove an element from the stack
        :return: The first element of the stack
        """
        
