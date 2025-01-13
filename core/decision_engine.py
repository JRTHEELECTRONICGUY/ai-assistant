from core.ethics_core import EthicsCore
from core.ai_agent import JRAgent

class DecisionEngine:
    def __init__(self):
        self.ethics_core = EthicsCore()
        self.agent = JRAgent()

    def process_command(self, user_input):
        if self.ethics_core.apply_rules(user_input):
            return self.agent.process_input(user_input)
        else:
            return "This action violates ethical guidelines."
    