import collections

class lru:
    def __init__(self,queuesize):
        self.dequeue_obj = collections.deque([])
        self.queuesize = queuesize
        self.current_size = 0
        self.queue_dict = {}