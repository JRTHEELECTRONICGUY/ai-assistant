import datetime
import os
import openai  # Requires an OpenAI API key
import json

class JRAgent:
    def __init__(self, api_key=None):
        self.name = "JR the Electronic Guy"
        self.api_key = api_key
        self.memory = {}
        self.commands = {
            "hello": self.greet,
            "help": self.show_help,
            "date": self.get_date,
            "time": self.get_time,
            "create_file": self.create_file,
            "read_file": self.read_file,
            "write_file": self.write_file,
            "search_memory": self.search_memory,
            "add_memory": self.add_memory,
        }
        if self.api_key:
            openai.api_key = self.api_key

    def greet(self, _):
        return f"Hello! I'm {self.name}. How can I assist you today?"

    def show_help(self, _):
        return (
            "I can help you with the following commands:\n"
            "- 'hello': Greet me.\n"
            "- 'help': Show this help message.\n"
            "- 'date': Get the current date.\n"
            "- 'time': Get the current time.\n"
            "- 'create_file <filename>': Create a new file.\n"
            "- 'read_file <filename>': Read a file's content.\n"
            "- 'write_file <filename> <content>': Write content to a file.\n"
            "- 'add_memory <key> <value>': Save something in memory.\n"
            "- 'search_memory <key>': Search for something in memory."
        )

    def get_date(self, _):
        return f"Today's date is {datetime.date.today()}."

    def get_time(self, _):
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')}."

    def create_file(self, params):
        if not params:
            return "Usage: create_file <filename>"
        filename = params[0]
        try:
            with open(filename, "w") as f:
                f.write("")
            return f"File '{filename}' created successfully."
        except Exception as e:
            return f"Error creating file: {e}"

    def read_file(self, params):
        if not params:
            return "Usage: read_file <filename>"
        filename = params[0]
        if not os.path.exists(filename):
            return f"Error: File '{filename}' does not exist."
        try:
            with open(filename, "r") as f:
                content = f.read()
            return f"Content of '{filename}':\n{content}"
        except Exception as e:
            return f"Error reading file: {e}"

    def write_file(self, params):
        if len(params) < 2:
            return "Usage: write_file <filename> <content>"
        filename, content = params[0], " ".join(params[1:])
        try:
            with open(filename, "a") as f:
                f.write(content + "\n")
            return f"Content written to '{filename}'."
        except Exception as e:
            return f"Error writing to file: {e}"

    def add_memory(self, params):
        if len(params) < 2:
            return "Usage: add_memory <key> <value>"
        key, value = params[0], " ".join(params[1:])
        self.memory[key] = value
        return f"Memory added: {key} = {value}"

    def search_memory(self, params):
        if not params:
            return "Usage: search_memory <key>"
        key = params[0]
        if key in self.memory:
            return f"Memory found: {key} = {self.memory[key]}"
        else:
            return f"No memory found for key: {key}"

    def generate_response(self, user_input):
        """Use OpenAI GPT to generate a natural language response."""
        if not self.api_key:
            return "AI functionality requires an API key. Please provide one during initialization."
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"You are {self.name}. Respond to the following input naturally:\n\n{user_input}",
                max_tokens=150,
                temperature=0.7
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error generating response: {e}"

    def process_input(self, user_input):
        if not user_input:
            return "Please provide a command."
        
        tokens = user_input.split()
        command = tokens[0].lower()
        params = tokens[1:]

        if command in self.commands:
            return self.commands[command](params)
        else:
            return self.generate_response(user_input)


# Example usage:
if __name__ == "__main__":
    # Replace "your_openai_api_key" with your actual OpenAI API key
    agent = JRAgent(api_key="your_openai_api_key")
    print("Welcome to JR the Electronic Guy! Type 'help' to see what I can do.")
    while True:
        user_input = input("> ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = agent.process_input(user_input)
        print(response)
