class MemoryNexus:
    def __init__(self):
        self.memory = {}

    def store_memory(self, user_id, key, value):
        """
        Stores a memory for a specific user.
        """
        if user_id not in self.memory:
            self.memory[user_id] = {}
        self.memory[user_id][key] = value

    def retrieve_memory(self, user_id, key):
        """
        Retrieves a memory for a specific user.
        """
        return self.memory.get(user_id, {}).get(key)

if __name__ == '__main__':
    nexus = MemoryNexus()
    nexus.store_memory("user123", "last_interaction", "Discussed the weather.")
    memory = nexus.retrieve_memory("user123", "last_interaction")
    print(f"Retrieved memory: {memory}")
