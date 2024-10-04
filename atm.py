import time

# Simulate checking user details
print("Checking your details...")
time.sleep(1)  # Pause for 1 second to simulate processing

# Set a default password for demonstration purposes
password = "1234"

# Prompt the user for their PIN
pin = input("Enter your PIN: ")

# Initialize the balance and transaction history
balance = 5999
transaction_history = []

# Check if the entered PIN matches the password
if pin == password:
    # If the PIN is correct, enter the main loop
    while True:
        # Display the ATM menu options
        print("""
              1 == Check Balance 
              2 == Withdraw Amount
              3 == Deposit Amount
              4 == Change PIN
              5 == View Transaction History
              6 == Exit
              """)

        # Get the user's choice
        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid numeric value.")
            continue  # Continue to the next iteration of the loop

        # Process the user's choice
        if option == 1:
            # Display the current balance
            print(f"Your balance is: {balance}")
            time.sleep(2)  # Pause for 2 seconds to simulate processing

        elif option == 2:
            # Withdraw cash
            withdraw_amount = int(input("Please enter withdrawal amount: "))
            if withdraw_amount > balance:
                # Check if the withdrawal amount is greater than the balance
                print("Low balance")
            else:
                # Subtract the withdrawal amount from the balance
                balance -= withdraw_amount
                # Add the withdrawal to the transaction history
                transaction_history.append(f"Withdrawal: {withdraw_amount}")
                print(f"{withdraw_amount} has been debited from your account.")
                print(f"Your updated balance is: {balance}")
            time.sleep(2)  # Pause for 2 seconds to simulate processing

        elif option == 3:
            # Deposit cash
            deposit_amount = int(input("Please enter deposit amount: "))
            # Add the deposit amount to the balance
            balance += deposit_amount
            # Add the deposit to the transaction history
            transaction_history.append(f"Deposit: {deposit_amount}")
            print(f"{deposit_amount} has been credited to your account.")
            print(f"Your updated balance is: {balance}")
            time.sleep(2)  # Pause for 2 seconds to simulate processing

        elif option == 4:
            # Change the PIN
            new_pin = input("Enter your new PIN: ")
            password = new_pin
            print("PIN changed successfully!")
            time.sleep(2)  # Pause for 2 seconds to simulate processing

        elif option == 5:
            # View transaction history
            print("Transaction History:")
            for transaction in transaction_history:
                print(transaction)
            time.sleep(2)  # Pause for 2 seconds to simulate processing

        elif option == 6:
            # Exit the ATM
            print("Thank you for visiting!")
            time.sleep(2)  # Pause for 2 seconds to simulate processing
            break

        else:
            # Invalid option
            print("Invalid option, please try again.")

else:
    # Incorrect PIN
    print("Incorrect PIN, please try again.")