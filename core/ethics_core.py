class EthicsCore:
    def __init__(self):
        self.rules = [
            "Always prioritize safety.",
            "Ensure data privacy and integrity.",
            "Provide unbiased information."
        ]

    def apply_rules(self, action):
        # Apply rules to the action and ensure it aligns with ethical standards
        if "harm" in action.lower():
            return False  # Reject harmful actions
        return True
    