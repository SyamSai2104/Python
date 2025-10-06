import json
import random
import string
from pathlib import Path
from typing import List, Dict, Optional


class Bank:
    DATABASE_FILE = "Bank_Management.json"
    _accounts = []

    def __init__(self):
        self._load_data()

    @classmethod
    def _load_data(cls):

        try:
            if Path(cls.DATABASE_FILE).exists():
                with open(cls.DATABASE_FILE, 'r') as file:
                    cls._accounts = json.load(file)
            else:
                print("No database file found. Starting with empty accounts list.")
                cls._accounts = []
        except Exception as error:
            print(f"Error loading data: {error}")
            cls._accounts = []

    @classmethod
    def _save_data(cls):

        try:
            with open(cls.DATABASE_FILE, 'w') as file:
                json.dump(cls._accounts, file, indent=4)
        except Exception as error:
            print(f"Error saving data: {error}")

    @classmethod
    def _generate_account_number(cls):

        while True:
            prefix = ''.join(random.choices(string.ascii_uppercase, k=3))
            suffix = ''.join(random.choices(string.digits, k=3))
            account_number = f"{prefix}-{suffix}"
            
            if not any(account['account_number'] == account_number 
                      for account in cls._accounts):
                return account_number

    @staticmethod
    def _get_valid_input(prompt: str, input_type=str):
        """Safely get and validate user input"""
        while True:
            try:
                user_input = input(prompt).strip()
                if input_type == int:
                    return int(user_input)
                return user_input
            except ValueError:
                print("Invalid input. Please try again.")

    def _authenticate_user(self):

        account_number = input("Enter your account number: ").strip()
        try:
            pin = int(input("Enter your 4-digit PIN: "))
        except ValueError:
            print("PIN must be a number.")
            return None

        user_account = next(
            (account for account in self._accounts 
             if account['account_number'] == account_number 
             and account['pin'] == pin),
            None
        )
        
        return user_account

    def create_account(self):

        print("\n=== CREATE NEW ACCOUNT ===")
        
        name = self._get_valid_input("Enter your full name: ")
        age = self._get_valid_input("Enter your age: ", int)
        email = self._get_valid_input("Enter your email: ")
        pin = self._get_valid_input("Set your 4-digit PIN: ", int)

        if age < 18:
            print("Error: You must be at least 18 years old to create an account.")
            return

        if len(str(pin)) != 4:
            print("Error: PIN must be exactly 4 digits.")
            return

        if any(account['email'] == email for account in self._accounts):
            print("Error: An account with this email already exists.")
            return

        new_account = {
            'name': name,
            'age': age,
            'email': email,
            'pin': pin,
            'account_number': self._generate_account_number(),
            'balance': 0.0
        }

        self._accounts.append(new_account)
        self._save_data()

        print("\nAccount created successfully!")
        print("=== ACCOUNT DETAILS ===")
        for key, value in new_account.items():
            if key != 'pin':  # Don't display PIN for security
                print(f"{key.replace('_', ' ').title()}: {value}")
        
        print("\nPlease save your account number for future reference!")

    def deposit(self):
        print("\n=== DEPOSIT MONEY ===")
        
        user_account = self._authenticate_user()
        if not user_account:
            print("Error: Authentication failed. Please check your credentials.")
            return

        amount = self._get_valid_input("Enter deposit amount (1-10000): ", int)
        
        if not (1 <= amount <= 10000):
            print("Error: Amount must be between 1 and 10,000.")
            return

        user_account['balance'] += amount
        self._save_data()
        
        print(f"Rs.{amount:,} deposited successfully!")
        print(f"New balance: Rs.{user_account['balance']:,}")

    def withdraw(self):

        print("\n=== WITHDRAW MONEY ===")
        
        user_account = self._authenticate_user()
        if not user_account:
            print("Error: Authentication failed. Please check your credentials.")
            return

        amount = self._get_valid_input("Enter withdrawal amount: ", int)
        
        if amount <= 0:
            print("Error: Amount must be greater than zero.")
            return
        
        if amount > user_account['balance']:
            print(f"Error: Insufficient funds. Available balance: Rs.{user_account['balance']:,}")
            return

        user_account['balance'] -= amount
        self._save_data()
        
        print(f"Rs.{amount:,} withdrawn successfully!")
        print(f"Remaining balance: Rs.{user_account['balance']:,}")

    def view_account_details(self):
        print("\n=== ACCOUNT DETAILS ===")
        
        user_account = self._authenticate_user()
        if not user_account:
            print("Error: Authentication failed. Please check your credentials.")
            return

        print("\n=== YOUR ACCOUNT INFORMATION ===")
        for key, value in user_account.items():
            if key != 'pin':  
                display_key = key.replace('_', ' ').title()
                if key == 'balance':
                    print(f"{display_key}: Rs.{value:,}")
                else:
                    print(f"{display_key}: {value}")

    def update_account_details(self):

        print("\n=== UPDATE ACCOUNT DETAILS ===")
        
        user_account = self._authenticate_user()
        if not user_account:
            print("Error: Authentication failed. Please check your credentials.")
            return

        print("Enter new details (press Enter to keep current value):")
        
        new_name = input(f"New name [{user_account['name']}]: ").strip()
        new_email = input(f"New email [{user_account['email']}]: ").strip()
        new_pin_input = input("New 4-digit PIN (leave empty to keep current): ").strip()

        updates_made = False
        
        if new_name:
            user_account['name'] = new_name
            updates_made = True
        
        if new_email:
            if any(acc['email'] == new_email and acc != user_account 
                   for acc in self._accounts):
                print("Error: This email is already in use by another account.")
                return
            user_account['email'] = new_email
            updates_made = True
        
        if new_pin_input:
            if len(new_pin_input) != 4 or not new_pin_input.isdigit():
                print("Error: PIN must be exactly 4 digits.")
                return
            user_account['pin'] = int(new_pin_input)
            updates_made = True

        if updates_made:
            self._save_data()
            print("Account details updated successfully!")
        else:
            print("No changes were made.")

    def delete_account(self):

        print("\n=== DELETE ACCOUNT ===")
        
        user_account = self._authenticate_user()
        if not user_account:
            print("Error: Authentication failed. Please check your credentials.")
            return

        print(f"\nAccount: {user_account['account_number']}")
        print(f"Balance: Rs.{user_account['balance']:,}")
        
        if user_account['balance'] > 0:
            print("Error: Cannot delete account with positive balance.")
            print("Please withdraw all funds before deleting your account.")
            return

        confirmation = input("\n Are you sure you want to delete your account? (yes/no): ").strip().lower()
        
        if confirmation in ['yes', 'y']:
            self._accounts.remove(user_account)
            self._save_data()
            print("Account deleted successfully!")
        else:
            print("Account deletion cancelled.")

    def display_menu(self):

        print("\n" + "="*50)
        print("BANK MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Account Details")
        print("5. Update Account Details")
        print("6. Delete Account")
        print("7. Exit")
        print("="*50)

    def run(self):
        while True:
            self.display_menu()
            
            try:
                choice = int(input("\nSelect an option (1-7): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1-7.")
                continue

            actions = {
                1: self.create_account,
                2: self.deposit,
                3: self.withdraw,
                4: self.view_account_details,
                5: self.update_account_details,
                6: self.delete_account,
                7: lambda: (print("Bye!"), exit())
            }

            action = actions.get(choice)
            if action:
                action()
            else:
                print("Invalid choice. Please select 1-7.")
            
            input("\nPress Enter to continue...")


def main():
    """Initialize and run the banking system"""
    bank_system = Bank()
    bank_system.run()


if __name__ == "__main__":
    main()