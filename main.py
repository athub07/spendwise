from auth import signup, login
from expense_manager import *


# =========================
# 🔐 AUTH SYSTEM
# =========================

def start():
    print("\n====== 🚀 Welcome to SpendWise ======")
    print("1. Login")
    print("2. Signup")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        return login()
    elif choice == "2":
        return signup()
    else:
        print("❌ Invalid choice")
        return None


# =========================
# 🏠 MAIN APP
# =========================

def main():
    current_user = None

    # 🔐 Login loop
    while not current_user:
        current_user = start()

    # 🏠 Main menu loop
    while True:
        print(f"\n====== 💰 SpendWise ({current_user}) ======")
        print("1. ➕ Add Expense")
        print("2. 📄 View Expenses")
        print("3. 🗑️ Delete Expense")
        print("4. ✏️ Update Expense")
        print("5. 💰 Total Spending")
        print("6. 📊 Category Total")
        print("7. 🔍 Search Expense")
        print("8. 🎯 Set Budget")
        print("9. 🚪 Logout")
        print("10. 📊 Category Chart")
        print("11. 📈 Spending Trend")
        print("12. 🧠 AI Spending Analysis")
        print("13. ❌ Exit App")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(current_user)

        elif choice == "2":
            view_expenses(current_user)

        elif choice == "3":
            delete_expense(current_user)

        elif choice == "4":
            update_expense(current_user)

        elif choice == "5":
            total_spending(current_user)

        elif choice == "6":
            category_total(current_user)

        elif choice == "7":
            search_expense(current_user)

        elif choice == "8":
            set_budget()

        elif choice == "9":
            print("🔄 Logging out...")
            return   # restart app


        elif choice == "10":
            show_category_chart(current_user)

        elif choice == "11":
            show_spending_trend(current_user)

        elif choice == "12":
            analyze_spending(current_user)

        elif choice == "13":
            print("👋 Exiting SpendWise...")
            break

        else:
            print("❌ Invalid choice. Try again.")


# =========================
# ▶️ RUN APP
# =========================

if __name__ == "__main__":
    main()