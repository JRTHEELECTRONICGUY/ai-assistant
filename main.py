from core.decision_engine import DecisionEngine

def main():
    print("JR AI Assistant is now running...")
    engine = DecisionEngine()
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = engine.process_command(user_input)
        print(f"JR: {response}")

if __name__ == "__main__":
    main()
