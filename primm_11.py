"""
PRIMM: 1+1 = 11
Faulty Addition Program
Emma Gustafsson - September 2024
"""
"""
This chunk of code asks the user for two numbers and then outputs the numbers beside each other.
"""
def main():
  
    num1: int = input("Enter a number: ")
    num2: int = input("Enter another number: ")
    total: int = num1+num2

    print(f"{num1} + {num2} = {total}")

if __name__ == "__main__":
  main()
