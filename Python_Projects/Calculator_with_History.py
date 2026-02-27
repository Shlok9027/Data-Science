HISTORY_FILE = "history.txt"


def show_history():
    file = open(HISTORY_FILE, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("OOPS! No History Found");
    else: 
        for line in reversed(lines):
            print(line.strip())
    file.close()



def clear_history():
    file = open(HISTORY_FILE,"w")
    file.write("")

    file.close()
    print("History Cleared Successfully");

def save_to_history(equation, result):
    file = open(HISTORY_FILE,"a")
    file.write(equation + "=" + str(result) + "\n")
    print("----------------------")
    file.close()


def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input format. Please use: number1 operator number2")
        return 
    
    num1 = float(parts[0])
    op =  parts[1]
    num2 = float(parts[2])


    if op == "+":
        result = num1 + num2

    elif op == "-":
        result = num1 - num2
    
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2    
    elif op == "%":
        result = num1 % num2    
    else:
        print("Invalid operator. Please use one of +, -, *, /, %")
        return
    

    if int(result) == result:
        result = int(result)
    print(f"Result: {result}")

    save_to_history(user_input, result)

def main():
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-SIMPLE CALCULATOR - TYPE HISTORY, CLEAR OR EXIT-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

    while True:
        user_input = input("Enter calculation (+, -, *, /) or command:(history, clear) ").strip().lower()

        if user_input == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)



main()