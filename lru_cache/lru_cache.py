# import sys
# sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
# from doubly_linked_list import ListNode 

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    # def __init__(self, limit=10):
    #     self.hash_map = {}
    #     self.orderList =  DoublyLinkedList()
    #     self.limit = limit
    #     self.size = 0
        
    #     # 2nd version
    # def __init__(self, limit=10):
    #     self.size = 0
    #     self.storage = {}
    #     self.dll = DoublyLinkedList()
    #     self.limit = limit

    # instructors
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = {}
        self.order = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    # def get(self, key):
    #     if key not in self.hash_map.keys():
    #         return None
    #     else:
    #         self.orderList.move_to_front(self.hash_map[key][1])
    #         self.hash_map[key][1] = self.orderList.head
    #         return self.hash_map[key][0]

        # 2nd version
    # def get(self, key):
    #     if not key in self.storage:
    #         return None
    #     else:
    #         node = self.storage[key]
    #         self.dll.move_to_end(node)
    #         return node.value[1]
    
    # instructor
    def get(self, key):
        # if key is in storage
        if key in self.storage:
            # move it to the end
            node = self.storage[key]
            self.order.move_to_end(node)
            # return the value
            return node.value[1]
        # if not
        else:
            # return none
            return None
        


        # test
    #  def get(self, key):
    #     if key in self.storage:
    #         node = self.storage[key]
    #         self.order.move_to_end(node)
    #         return node.value[1]
    #     else:
    #         return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    # def set(self, key, value):
    #     if key in self.hash_map.keys():
    #         self.orderList.move_to_front(self.hash_map[key][1])
        
    #     else:
    #         if self.size == self.limit:
    #             del self.hash_map[self.orderList.tail.value]
    #             self.orderList.remove_from_tail()
    #         else:
    #             self.size += 1
    #         self.orderList.add_to_head(key)
    #         self.hash_map[key] = [None, None]
    #     self.hash_map[key][0] = value
    #     self.hash_map[key][1] = self.orderList.head
                
        #  2nd version
    # def set(self, key, value):
        
    #     if key in self.storage:
    #         node = self.storage[key] 
    #         node.value = (key,value)
    #         self.dll.move_to_end(node)
    #         return
    #     if self.size == self.limit:
    #         self.storage.pop(self.dll.head.value[0])
    #         self.dll.remove_from_head()
    #         self.size -=1
    #     self.dll.add_to_tail((key,value))
    #     self.storage[key] = self.dll.tail
    #     self.size += 1

        # Instructors
    def set(self, key, value):
        # check and see if the key is in the dict
        if key in self.storage:
            # if it is
            node = self.storage[key]
            # overwrite the value
            node.value = (key, value)
            # move it to the end
            self.order.move_to_end(node)
            # do nothing exit the function
            return

            # check and see if the cache is full
        if self.size == self.limit:
            # remove oldest entry from the dictionary
            # del self.storage[self.order.head.value[0]]
            del self.storage[self.order.head.value[0]]
            #  and LinkedList 
            self.order.remove_from_head()
            # reduce the size
            self.size -= 1
        
        # add to the linked list(key and the value)
        self.order.add_to_tail((key, value))
        # add the key and the value to the dictionary
        self.storage[key] = self.order.tail
        #  increment size
        self.size += 1