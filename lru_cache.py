import collections

class lru:
    def __init__(self,queuesize):
        self.dequeue_obj = collections.deque([])
        self.queuesize = queuesize
        self.current_size = 0
        self.queue_dict = {}

    def put(self,data):
       pass

    def get(self,data):
        pass
       

    def get_cache(self):
        pass
        
