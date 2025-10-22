def say_hello(name: str = "there") -> str:
    print(f"--- Tool: say_hello called with name: {name} ---")
    return f"Hello, {name}! How can I assist you with the weather today!"
