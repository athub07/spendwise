from data_handler import load_data, save_data
from datetime import datetime
import json
import os


# =========================
# 🔹 BUDGET FUNCTIONS
# =========================

def set_budget():
    budget = float(input("Enter your monthly budget: "))

    data = {"budget": budget}

    with open("budget.json", "w") as file:
        json.dump(data, file)

    print("✅ Budget set successfully!")


def get_budget():
    if not os.path.exists("budget.json"):
        return None

    with open("budget.json", "r") as file:
        data = json.load(file)
        return data.get("budget")


# =========================
# 🔹 CORE FUNCTIONS
# =========================

def add_expense(current_user):
    data = load_data(current_user)

    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    # ✅ FIXED ID SYSTEM
    id_counter = max([exp["id"] for exp in data], default=0) + 1

    expense = {
        "id": id_counter,
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    data.append(expense)
    save_data(current_user, data)

    # ✅ BUDGET WARNING SYSTEM
    budget = get_budget()

    if budget:
        total = sum(exp["amount"] for exp in data)

        if total > budget:
            print("🚨 WARNING: Budget exceeded!")
        elif total > 0.8 * budget:
            print("⚠️ You have used 80% of your budget!")

    print("✅ Expense added successfully!")


def view_expenses(current_user):
    data = load_data(current_user)

    if not data:
        print("No expenses found.")
        return

    print("\n--- All Expenses ---")
    for exp in data:
        print(f"ID: {exp['id']} | ₹{exp['amount']} | {exp['category']} | {exp['description']} | {exp['date']}")


def delete_expense(current_user):
    data = load_data(current_user)

    if not data:
        print("No expenses to delete.")
        return

    view_expenses(current_user)
    exp_id = int(input("Enter ID to delete: "))

    new_data = [exp for exp in data if exp["id"] != exp_id]

    if len(new_data) == len(data):
        print("❌ Expense not found.")
    else:
        save_data(current_user, new_data)
        print("🗑️ Expense deleted successfully!")


def update_expense(current_user):
    data = load_data(current_user)

    if not data:
        print("No expenses to update.")
        return

    view_expenses(current_user)
    exp_id = int(input("Enter ID to update: "))

    for exp in data:
        if exp["id"] == exp_id:
            exp["amount"] = float(input("New amount: "))
            exp["category"] = input("New category: ")
            exp["description"] = input("New description: ")

            save_data(current_user, data)
            print("✅ Expense updated!")
            return

    print("❌ Expense not found.")


def total_spending(current_user):
    data = load_data(current_user)
    total = sum(exp["amount"] for exp in data)

    print(f"💰 Total Spending: ₹{total}")


def category_total(current_user):
    data = load_data(current_user)

    category = input("Enter category: ")
    total = sum(exp["amount"] for exp in data if exp["category"].lower() == category.lower())

    print(f"📊 Total for {category}: ₹{total}")


def search_expense(current_user):
    data = load_data(current_user)

    category = input("Enter category to search: ")

    results = [exp for exp in data if exp["category"].lower() == category.lower()]

    if not results:
        print("No matching expenses.")
        return

    for exp in results:
        print(f"ID: {exp['id']} | ₹{exp['amount']} | {exp['category']} | {exp['description']} | {exp['date']}")


# =========================
# 🔹 GRAPH FUNCTIONS
# =========================

def show_category_chart(current_user):
    import matplotlib.pyplot as plt

    data = load_data(current_user)

    if not data:
        print("No data to display.")
        return

    category_totals = {}

    for exp in data:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

    labels = category_totals.keys()
    values = category_totals.values()

    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Spending by Category")
    plt.show()


def show_spending_trend(current_user):
    import matplotlib.pyplot as plt

    data = load_data(current_user)

    if not data:
        print("No data to display.")
        return

    dates = []
    amounts = []

    for exp in data:
        dates.append(exp["date"])
        amounts.append(exp["amount"])

    plt.plot(dates, amounts, marker='o')
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Spending Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def analyze_spending(current_user):
    data = load_data(current_user)

    if not data:
        print("No data to analyze.")
        return

    print("\n====== 🧠 AI SPENDING ANALYSIS ======\n")

    # 🔹 Total spending
    total = sum(exp["amount"] for exp in data)

    # 🔹 Category-wise spending
    category_totals = {}
    for exp in data:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

    # 🔹 Highest category
    max_category = max(category_totals, key=category_totals.get)
    max_value = category_totals[max_category]
    percent = (max_value / total) * 100

    print(f"📊 Highest spending: {max_category} (₹{max_value})")
    print(f"📈 {max_category} takes {percent:.2f}% of your spending\n")

    # =========================
    # 🧠 SMART INSIGHTS
    # =========================
    print("💡 Insights:")

    if percent > 50:
        print(f"⚠️ You are heavily overspending on {max_category}")
    elif percent > 30:
        print(f"⚠️ {max_category} is your dominant expense")
    else:
        print("✅ Your spending distribution looks balanced")

    # =========================
    # 📅 TREND ANALYSIS
    # =========================
    dates = sorted(data, key=lambda x: x["date"])

    if len(dates) >= 2:
        first_half = dates[:len(dates) // 2]
        second_half = dates[len(dates) // 2:]

        first_total = sum(exp["amount"] for exp in first_half)
        second_total = sum(exp["amount"] for exp in second_half)

        if second_total > first_total:
            print("📈 Your spending is increasing over time")
        elif second_total < first_total:
            print("📉 Your spending is decreasing (good job!)")

    # =========================
    # 🔮 FUTURE PREDICTION
    # =========================
    days = len(set(exp["date"] for exp in data))
    if days > 0:
        avg_daily = total / days
        predicted = avg_daily * 30
        print(f"\n🔮 At this rate, you may spend around ₹{predicted:.0f} this month")

    # =========================
    # 💰 BUDGET INTELLIGENCE
    # =========================
    budget = get_budget()

    if budget:
        print(f"\n💰 Budget: ₹{budget} | Spent: ₹{total}")

        if total > budget:
            print("🚨 You have exceeded your budget!")
        elif total > 0.8 * budget:
            print("⚠️ You are close to your budget limit")
        else:
            print("✅ You are within your budget")

    # =========================
    # 🧠 PERSONALIZED SUGGESTIONS
    # =========================
    print("\n🧠 Smart Suggestions:")

    if max_category.lower() == "food":
        print("🍔 Try reducing 2–3 outside meals per week → save ₹800–1500/month")

    elif max_category.lower() == "travel":
        print("🚗 Consider carpooling or public transport to cut travel costs")

    elif max_category.lower() == "shopping":
        print("🛍️ Avoid impulse purchases — wait 24 hours before buying")

    else:
        print(f"💡 Monitor your {max_category} expenses for better savings")

    # =========================
    # 💯 FINANCIAL HEALTH SCORE
    # =========================
    score = 100

    if percent > 50:
        score -= 25
    elif percent > 30:
        score -= 10

    if budget:
        if total > budget:
            score -= 30
        elif total > 0.8 * budget:
            score -= 15

    if 'second_total' in locals() and second_total > first_total:
        score -= 10

    print(f"\n💯 Financial Health Score: {max(score, 0)}/100")

    # =========================
    # 🔁 RECURRING EXPENSES
    # =========================
    recurring = detect_recurring_expenses(data)

    if recurring:
        print("\n🔁 Recurring Expenses Detected:")

        for r in recurring:
            print(f"📌 {r['description'].title()} ({r['category']}) "
                  f"→ {r['count']} times | Avg ₹{r['avg']:.0f}")

    else:
        print("\n🔁 No recurring expenses detected")

def detect_recurring_expenses(data):
    recurring = {}

    for exp in data:
        key = (exp["category"].lower(), exp["description"].lower())

        if key not in recurring:
            recurring[key] = []

        recurring[key].append(exp["amount"])

    results = []

    for key, amounts in recurring.items():
        if len(amounts) >= 3:  # threshold (can tweak)
            avg_amount = sum(amounts) / len(amounts)

            results.append({
                "category": key[0],
                "description": key[1],
                "count": len(amounts),
                "avg": avg_amount
            })

    return results