from core.emotional_mirror import EmotionalMirror
from core.memory_nexus import MemoryNexus
from core.ethical_engine import EthicalEngine
from core.reasoning_core import ReasoningCore

class NamoAI:
    def __init__(self):
        self.emotional_mirror = EmotionalMirror()
        self.memory_nexus = MemoryNexus()
        self.ethical_engine = EthicalEngine()
        self.reasoning_core = ReasoningCore()

    def interact(self, user_id, user_input):
        """
        Main interaction logic for Namo AI.
        """
        # 1. Analyze sentiment
        sentiment = self.emotional_mirror.analyze_sentiment(user_input)

        # 2. Retrieve relevant memories
        last_interaction = self.memory_nexus.retrieve_memory(user_id, "last_interaction")

        # 3. Reason about the user's input
        solution = self.reasoning_core.reason(user_input, context=last_interaction)

        # 4. Generate an empathetic and ethical response
        empathetic_response = self.emotional_mirror.generate_empathetic_response(sentiment)
        final_response = f"{empathetic_response} {solution}"

        # 5. Store the current interaction in memory
        self.memory_nexus.store_memory(user_id, "last_interaction", user_input)

        return final_response

if __name__ == '__main__':
    namo = NamoAI()
    user_id = "user456"
    user_input = "I'm feeling a bit lost and confused."
    response = namo.interact(user_id, user_input)
    print(f"User Input: '{user_input}'")
    print(f"Namo AI Response: {response}")
