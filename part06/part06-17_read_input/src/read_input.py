# Write your solution here
def read_input(prompt: str, lower_limit: int, upper_limit: int):
    while True:
        try:
            input_str = input(prompt)
            number = int(input_str)
            if number > lower_limit and number < upper_limit:
                return number
        except ValueError:
            pass
        print(f"You must type in an integer between {lower_limit} and {upper_limit}")
