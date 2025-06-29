def log_message(message):
    with open("assistant.log", "a") as log_file:
        log_file.write(f"{message}\n")

def handle_error(error):
    log_message(f"Error: {error}")

def validate_command(command):
    valid_commands = ["play music", "stop", "pause", "resume", "weather", "time"]
    return command in valid_commands

def format_response(response):
    return response.capitalize() + "."