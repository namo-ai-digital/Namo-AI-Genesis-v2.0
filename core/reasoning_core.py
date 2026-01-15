from core.ethical_engine import EthicalEngine

class ReasoningCore:
    def __init__(self):
        self.ethical_engine = EthicalEngine()

    def reason(self, user_input, context=None):
        """
        Reasons about a problem while considering ethical implications.

        Args:
            user_input (str): The input from the user or the problem statement.
            context (str, optional): Additional context, e.g., previous interaction.
        """
        # Determine Intent
        intent = self._determine_intent(user_input)

        # Generate Solution based on Intent
        solution = self._generate_solution(intent, user_input)

        # Ethical Check
        is_ethical, justification = self.ethical_engine.evaluate_action(solution)

        if is_ethical:
            return solution
        else:
            return f"Cannot solve the problem in an ethical manner. {justification}"

    def _determine_intent(self, text):
        text_lower = text.lower()
        if any(word in text_lower for word in ['help', 'assist', 'support']):
            return 'assist'
        elif any(word in text_lower for word in ['sad', 'happy', 'angry', 'feel', 'depressed']):
            return 'emotional'
        elif any(word in text_lower for word in ['how to', 'solve', 'fix']):
            return 'solve'
        elif any(word in text_lower for word in ['what', 'why', 'who', 'when', 'where', 'define']):
            return 'query'
        else:
            return 'general'

    def _generate_solution(self, intent, text):
        if intent == 'assist':
            return f"I am here to help. Based on your request '{text}', I can offer guidance and support."
        elif intent == 'emotional':
            return f"I understand this involves emotions. My response is to listen and provide a compassionate presence regarding '{text}'."
        elif intent == 'solve':
            return f"To address '{text}', I suggest breaking it down into smaller steps and analyzing each part logically."
        elif intent == 'query':
            return f"Regarding your question '{text}', I will analyze the available information to provide a clear answer."
        else:
            return f"I have processed '{text}' and am ready to engage in further dialogue."

if __name__ == '__main__':
    core = ReasoningCore()
    problem = "How to respond to a user in distress?"
    solution = core.reason(problem)
    print(f"Problem: '{problem}'")
    print(f"Solution: {solution}")
