import logging

logging.basicConfig(
    level=logging.INFO,
    filename="data_input_log.txt",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",)

while True:
    user_input = input("Enter something (or 'end'): ")
    if user_input.lower() == "end":
        print("Goodbye!")
        break
        
    logging.info(f"User input: {user_input}")