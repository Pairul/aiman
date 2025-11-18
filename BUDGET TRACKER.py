# ---- Budget Tracker ----
def manage_budget():
    while True:
        print("\n--- Budget Tracker ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Back")
        choice = input("Choose: ")

        if choice == "1":
            item = input("Item: ")
            amount = float(input("Amount (RM): "))
            budget_items.append({"item": item, "amount": amount})
            print("Expense added.")
        elif choice == "2":
            print("\nBudget:")
            total = 0
            for b in budget_items:
                total += b["amount"]
                print(f"- {b['item']}: RM{b['amount']}")
            print(f"Total: RM{total}")
        elif choice == "3":
            break
        else:
            print("Invalid choice!")