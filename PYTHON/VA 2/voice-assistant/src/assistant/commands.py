class CommandHandler:
    def __init__(self):
        self.commands = {
            "greet": self.greet,
            "exit": self.exit_assistant,
            # Add more commands as needed
        }

    def execute_command(self, command):
        if command in self.commands:
            return self.commands[command]()
        else:
            return "Command not recognized."

    def get_commands(self):
        return list(self.commands.keys())

    def greet(self):
        return "Hello! How can I assist you today?"

    def exit_assistant(self):
        return "Goodbye! Have a great day!"