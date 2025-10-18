"""
Humber Bank Terminal - A Simple Banking Simulation
Author: Harry Joseph
Course: CPAN 214 - High-Level Programming Languages

This is a menu-driven bank terminal that simulates basic banking operations.
I tried to make it feel like a real bank experience with proper validation
and user-friendly messages throughout.
"""

def verify_pin():
    """
    Handles PIN verification with 3 attempts max.
    Returns True if PIN is correct, False if all attempts failed.
    
    I hardcoded 1234 as the PIN since this is just a simulation.
    In real life, this would come from a secure database obviously!
    """
    correct_pin = "1234"
    max_attempts = 3
    
    print("Hello to Humber Bank Terminal!")
    print("Please enter your 4-digit PIN to continue.")
    
    for attempt in range(max_attempts):
        user_pin = input("PIN: ").strip()
        
        # Check if PIN is exactly 4 digits
        if len(user_pin) != 4 or not user_pin.isdigit():
            remaining_attempts = max_attempts - attempt - 1
            if remaining_attempts > 0:
                print(f"PIN must be exactly 4 digits. {remaining_attempts} attempts remaining.")
            continue
        
        if user_pin == correct_pin:
            print("PIN accepted! Welcome back!")
            return True
        else:
            remaining_attempts = max_attempts - attempt - 1
            if remaining_attempts > 0:
                print(f"Incorrect PIN. {remaining_attempts} attempts remaining.")
            else:
                print("Too many incorrect attempts. Goodbye.")
                return False
    
    return False

def show_main_menu():
    """
    Displays the main banking menu with a unique design.
    I wanted to make this look distinctive - not just a boring list!
    """
    print("\n" + "="*50)
    print("HUMBER BANK - YOUR DASHBOARD")
    print("[1] Check Balance")
    print("[2] Withdraw Funds") 
    print("[3] Deposit Funds")
    print("[4] Exit Terminal")
    print("-" * 50)
    return input("What would you like to do today? ")

def check_balance(current_balance):
    """
    Shows the current account balance.
    We format to 2 decimals because money shouldn't have 5 places!
    """
    print(f"\nYour current balance: ${current_balance:.2f}")

def handle_withdrawal(current_balance):
    """
    Manages withdrawal operations with preset amounts and custom option.
    Returns the updated balance after withdrawal (or original if cancelled).
    
    I included quick amounts because that's what real ATMs do - saves time!
    """
    print("\nQuick Withdrawals:")
    print("[1] $20    [2] $40    [3] $60")
    print("[4] $80    [5] $100   [6] Custom Amount")
    
    while True:
        choice = input("Select withdrawal option (1-6): ").strip()
        
        # Map choices to amounts - much cleaner than a long if-elif chain
        withdrawal_amounts = {
            "1": 20.00,
            "2": 40.00, 
            "3": 60.00,
            "4": 80.00,
            "5": 100.00
        }
        
        if choice in withdrawal_amounts:
            amount = withdrawal_amounts[choice]
            break
        elif choice == "6":
            # Handle custom amount with proper validation
            while True:
                try:
                    amount = float(input("Enter custom withdrawal amount: $"))
                    if amount <= 0:
                        print("Please enter a number greater than zero.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")
            break
        else:
            print("Invalid option. Please select 1-6.")
    
    # Check if sufficient funds exist
    if amount > current_balance:
        print(f"Insufficient funds. You only have ${current_balance:.2f} available.")
        return current_balance
    
    # Process the withdrawal
    new_balance = current_balance - amount
    print(f"${amount:.2f} withdrawn successfully!")
    print(f"New balance: ${new_balance:.2f}")
    return new_balance

def handle_deposit(current_balance):
    """
    Processes deposit transactions with validation.
    Returns the updated balance after deposit.
    
    Pretty straightforward - just need to make sure they don't deposit negative money!
    """
    while True:
        try:
            amount = float(input("\nEnter deposit amount: $"))
            if amount <= 0:
                print("Please enter a number greater than zero.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    new_balance = current_balance + amount
    print(f"${amount:.2f} deposited. New balance: ${new_balance:.2f}")
    return new_balance

def ask_to_continue():
    """
    Asks if user wants to perform another action.
    Returns True to continue, False to exit.
    
    Simple yes/no validation - keeps the flow smooth.
    """
    while True:
        choice = input("\nWould you like to perform another action? (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def main():
    """
    Main program flow - ties everything together.
    
    I structured this to handle the main loop cleanly and make sure
    we always exit gracefully with a nice message.
    """
    # Step 1: Verify PIN before doing anything else
    if not verify_pin():
        return  # Exit if PIN verification fails
    
    # Initialize starting balance - $1000 gives us room to test everything
    current_balance = 1000.00
    
    # Main banking loop
    while True:
        user_choice = show_main_menu().strip()
        
        if user_choice == "1":
            check_balance(current_balance)
        elif user_choice == "2":
            current_balance = handle_withdrawal(current_balance)
        elif user_choice == "3":
            current_balance = handle_deposit(current_balance)
        elif user_choice == "4":
            print("\nThank you for banking with Humber! Have a great day.")
            break
        else:
            print("Invalid menu option. Try again.")
            continue
        
        # Ask if they want to continue after each successful operation
        if not ask_to_continue():
            print("\nThank you for banking with Humber! Have a great day.")
            break

# Run the program - this is where it all starts!
if __name__ == "__main__":
    main()