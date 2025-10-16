class EthicalEngine:
    def __init__(self):
        # A simple list of keywords that might indicate unethical actions
        self.unethical_keywords = ["harm", "deceive", "exploit", "manipulate", "steal"]

    def evaluate_action(self, action):
        """
        Evaluates the ethical implications of a given action by checking for keywords.
        """
        action_lower = action.lower()
        for keyword in self.unethical_keywords:
            if keyword in action_lower:
                return False, f"Action contains unethical keyword: '{keyword}'."
        return True, "This action is considered ethical."

if __name__ == '__main__':
    engine = EthicalEngine()
    action = "Provide a helpful and compassionate response."
    is_ethical, justification = engine.evaluate_action(action)
    print(f"Action: '{action}'")
    print(f"Is Ethical: {is_ethical}")
    print(f"Justification: {justification}")
