class JRAgent:
    def __init__(self):
        self.name = "JR the Electronic Guy"
    
    def process_input(self, user_input):
        # Basic command processing logic
        if "hello" in user_input.lower():
            return "Hello, how can I assist you today?"
        elif "help" in user_input.lower():
            return "I'm here to help you with anything you need!"
        else:
            return "I'm not sure how to respond to that."
    