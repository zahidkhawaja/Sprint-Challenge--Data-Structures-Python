class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest_index = 0

    def append(self, item):
        # There's enough room
        # Simply append
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            # Override oldest value (based on oldest_index)
            # After appending, shift the index over (to represent the new "oldest" value)
            self.storage[self.oldest_index] = item
            self.oldest_index += 1

        # Reset oldest_index since we have overwritten all the values now
        # Index 0 is the oldest value again
        if self.oldest_index == self.capacity:
            self.oldest_index = 0

    def get(self):
        return self.storage