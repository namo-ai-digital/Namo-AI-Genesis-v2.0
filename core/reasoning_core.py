from core.ethical_engine import EthicalEngine

class ReasoningCore:
    def __init__(self):
        self.ethical_engine = EthicalEngine()

    def reason(self, problem):
        """
        Reasons about a problem while considering ethical implications.
        """
        # Placeholder for reasoning logic
        solution = f"Solving the problem: '{problem}' with compassion."
        is_ethical, justification = self.ethical_engine.evaluate_action(solution)
        if is_ethical:
            return solution
        else:
            return f"Cannot solve the problem in an ethical manner. {justification}"

if __name__ == '__main__':
    core = ReasoningCore()
    problem = "How to respond to a user in distress?"
    solution = core.reason(problem)
    print(f"Problem: '{problem}'")
    print(f"Solution: {solution}")
