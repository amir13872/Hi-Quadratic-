import cmath
import matplotlib.pyplot as plt
import numpy as np
import os
import platform

class Calculator:
    def __init__(self):
        self.system_info()
        self.run()

    def system_info(self):
        # Detect the operating system and execute appropriate commands
        if platform.system() == "Windows":
            os.system('ipconfig')  # Display network information on Windows
            os.system('cls')       # Clear the console on Windows
        else:
            os.system('ifconfig')  # Display network information on Linux
            os.system('clear')     # Clear the console on Linux
        print(os.getcwd())          # Print the current working directory
        print("The name of God")    # Print a custom message

    def calculate_delta(self, a, b, c):
        # Calculate the discriminant (delta) of the quadratic equation
        return (b**2) - (4 * a * c)
    
    def calculate_x1(self, b, delta, a):
        # Calculate the first root of the quadratic equation
        return ((-b) + cmath.sqrt(delta)) / (2 * a)
    
    def calculate_x2(self, b, delta, a):
        # Calculate the second root of the quadratic equation
        return ((-b) - cmath.sqrt(delta)) / (2 * a)

    def plot_graph(self, a, b, c):
        # Create x values
        x = np.linspace(-10, 10, 400)
        # Calculate corresponding y values
        y = a * x**2 + b * x + c
        
        # Create the plot
        plt.figure()
        plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
        plt.title('Quadratic Function Graph')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()

    def run(self):
        while True:
            try:
                q = input('Hello, are you sure? Yes or NO ==>  ').lower()
                if q == 'no':
                    print('Goodbye')
                    break
                elif q == 'yes':
                    a = float(input('Enter a =  '))
                    b = float(input('Enter b =  '))
                    c = float(input('Enter c =  '))
                    if a == 0:
                        print("The coefficient 'a' cannot be zero. Please enter a valid number for 'a'.")
                        continue

                    delta = self.calculate_delta(a, b, c)
                    print(f'delta = {delta}')
                    if delta > 0:
                        x1 = self.calculate_x1(b, delta, a)
                        x2 = self.calculate_x2(b, delta, a)
                        print(f'x1 = {x1.real if x1.imag == 0 else x1}')
                        print(f'x2 = {x2.real if x2.imag == 0 else x2}')
                    elif delta == 0:
                        x = self.calculate_x1(b, delta, a)
                        print(f'x = {x.real if x.imag == 0 else x}')
                    else:
                        x1 = self.calculate_x1(b, delta, a)
                        x2 = self.calculate_x2(b, delta, a)
                        print(f'x1 = {x1}')
                        print(f'x2 = {x2}')

                    self.plot_graph(a, b, c)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
            except ZeroDivisionError:
                print("The coefficient 'a' cannot be zero. Please enter a valid number for 'a'.")

if __name__ == "__main__":
    calculator = Calculator()
