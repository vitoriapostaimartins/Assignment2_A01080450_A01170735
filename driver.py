from store import Store, DailyTransactionReport


class Menu:
    def __init__(self):
        self._store = Store()

    @property
    def store(self):
        return self._store

    def _show_options(self):
        print("Menu:\n"
              "1 - Process Orders\n "
              "2 - Check Inventory\n "
              "3 - Exit\n")
        choice = int(input("Please choose an option from the above"))
        return choice

    def _exit(self):
        orders = self.store.orders
        DailyTransactionReport.create_report(orders)

    def show_menu(self):
        print("Welcome the Store")

        while True:
            choice = self._show_options()

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

            # Catch any string values
            try:
                operation = input_map[choice]
            except ValueError:
                print("Invalid choice. Please try again.")
                continue

            operation()

    def _process_orders(self):
        order_name = "orders_blankvalues.xlsx"
        self._store.process_orders(order_name)

    def _check_inventory(self):
        self.store.check_inventory()


def main():
    menu = Menu()
    menu.show_menu()


if __name__ == '__main__':
    main()
