# idea is to use a list of large number e.g. 10000
# key will be our index so (k,v) pair will be stored at index key i.e. list[key % 10000]
# create a object Bucket for each element of list and have methods, get, update and remove to those objects
# now, adding a key val pair, will check if the object at index key has already values i.e. collision
# if yes, check if the key is already in that bucket, if yes update if no append at the end of the bucket (list of that object)
# removing a key, check if the bucket has key already if yes, remove the pair else return
# get a val, check if the bucket already has a key, if yes, return value of the key else return -1
class Bucket(object):
    def __init__(self):
        self.bucket = []
    
    def update(self, key :int, val : int) -> None:
        found = False
        for i, (k, v) in enumerate(self.bucket):
            if k== key:
                self.bucket[i] = (key, val)
                found = True
                break
        if not found:
            self.bucket.append((key, val))
        return
    
    def get(self, key: int) -> int:
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1
    
    def remove(self, key: int) -> None:
        for i, (k, v) in enumerate(self.bucket):
            if k == key:
                del self.bucket[i]
                return
        return


class MyHashMap(object):
    def __init__(self):
        self.keySpace = 100000
        self.space = [Bucket() for _ in range(self.keySpace)]
     
    def put(self, key:int, value: int) -> None:
        self.space[key % self.keySpace].update(key, value)
        return
    
    def get(self, key: int)-> int:
        return self.space[key % self.keySpace].get(key)
    
    def remove(self, key: int)-> None:
        self.space[key % self.keySpace].remove(key)
        return

# time : O(1) - all the operations happen in O(1) as we know the index (key) of the (k, v) pair in our keySpace
# space : O(N) - to store the (key, value) pairs