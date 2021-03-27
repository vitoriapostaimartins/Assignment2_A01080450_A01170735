"""
Module that contains Menu class and its methods to display and act on the UI menu, as well as a main method.
"""

import os
from pathlib import Path
from store import Store, DailyTransactionReport


class Menu:
    """
    Class that represents a Menu for a storefront system.
    """

    def __init__(self):
        """
        Initialize a menu with an associated Store.
        """
        self._store = Store()

    @property
    def store(self):
        """
        Get the Store for this menu.
        :return:a Store
        """
        return self._store

    def _show_options(self):
        """
        Show the menu options.
        :return: an int
        """
        print("\nMenu")
        print("1 - Process Orders\n"
              "2 - Check Inventory\n"
              "3 - Exit\n")
        choice = input("Please choose an option from the above")
        return choice

    def _exit(self):
        """
        Exit the menu and print the daily transaction report.
        """
        orders = self.store.order_files
        file_name = DailyTransactionReport.create_report(orders)
        print(f"\nSuccessfully printed report to: {file_name}")
        print("-------------- Exited Program ---------------------")

    def show_menu(self):
        """
        Display the menu and carry out the operation chosen by the user.
        """
        print("""
        

 _  _     _ _ _    _             ___                     _           
| || |___| | (_)__| |__ _ _  _  | __|_ _____ _ _ _  _ __| |__ _ _  _ 
| __ / _ \ | | / _` / _` | || | | _|\ V / -_) '_| || / _` / _` | || |
|_||_\___/_|_|_\__,_\__,_|\_, | |___|\_/\___|_|  \_, \__,_\__,_|\_, |
                          |__/                   |__/           |__/ 
        """)
        print("\t\t\t The time to celebrate is today!\n"
              "-------------------------------------------------------------------")
        # Prompt the user to select a choice from the menu
        while True:

            try:
                choice = int(self._show_options())
            except ValueError:
                print("\nInvalid choice. Please try again.")
                continue

            if choice == 3:
                self._exit()
                return
            elif choice > 3 or choice < 0:
                print("\nInvalid choice. Please try again.")
                continue
            else:
                input_map = {
                    1: self._process_orders,
                    2: self._check_inventory,
                }

            operation = input_map[choice]

            operation()

    def _process_orders(self):
        """
        Process the orders in the excel file specified.
        """
        order_name = self._get_filename()
        self.store.process_orders(order_name)

    def _get_filename(self):
        """
        Prompt the user until they enter a valid file name.
        :return: a string
        """
        while True:
            filename = input("\nPlease enter a file name if you would like to enter it manually. Press d for default: ")
            if filename == "d":
                filename = "orders.xlsx"
                break
            extension = os.path.splitext(filename)[1]
            if self._check_filename(filename, extension):
                break
            print("\nPlease enter a valid and existent xlsx file or d.")
        return filename

    def _check_filename(self, path, file_extension):
        """
        Validate the file entered by a user.
        :param path: a string
        :param file_extension: a string
        :return: True if filename is valid, False otherwise
        """
        if Path(path).exists():
            if file_extension == ".xlsx":
                return True
        return False

    def _check_inventory(self):
        """
        Check the store inventory for that status of each item.
        """
        self.store.check_inventory()


def main():
    """
    Instantiate a Menu and show the menu options.
    """
    menu = Menu()
    menu.show_menu()


if __name__ == '__main__':
    main()
