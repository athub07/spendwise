# SpendWise 💰

SpendWise is a command line based expense manager made using Python. The main goal of this project was to build something that is actually useful in day to day life, not just a basic academic project.

It allows users to track their expenses, manage a monthly budget, and also get some basic analysis of their spending habits. Over time while building it, more features were added so it became a bit more complete than what was initially planned.

---

## 🚀 Features

* User signup and login system (with password hashing)
* Add, update and delete expenses
* View all recorded expenses
* Search expenses by category
* Calculates total spending
* Monthly budget setting with warnings if limit exceeds
* Category wise expense breakdown
* Graphs for better visualization (using matplotlib)
* Basic smart analysis (like spending trends and predictions)
* Detects some recurring expenses (not perfect but works in most cases)

---

## 🛠️ Tech Used

* Python
* JSON (for storing user data and expenses)
* Matplotlib
* Hashlib

Nothing too fancy was used, the focus was more on logic and implementation.

---

## 📂 Project Structure

```
SpendWise/
│
├── main.py
├── expense_manager.py
├── auth.py
├── data_handler.py
├── users.json
├── data_*.json
├── requirements.txt
└── report.pdf
```

main.py handles the flow of the program while expense_manager.py contains most of the core features.

---

## ⚙️ Setup Instructions

1. Download or clone the project

2. Open the folder in terminal

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the program:

```
python main.py
```

That’s it, it should start working.

---

## 🧪 How it Works

After starting the program, user can either login or signup. Once logged in, all the expenses are stored separately for each user in JSON files.

The program basically runs in a loop and shows options like adding expense, viewing data, analysis etc. Most operations directly read/write from files so its pretty straightforward.

---

## 🧠 Analysis Feature

There is also a small “smart analysis” part added in the project. It is not real AI but more like logic based insights.

It tries to:

* Find which category you spend the most on
* Check if spending is increasing or decreasing
* Estimate monthly spending
* Give some basic suggestions

It’s not 100% accurate always but gives a decent idea.

---

## ⚠️ Limitations

* It is CLI based, no graphical interface
* Data is stored locally only
* Analysis is basic, not using any real machine learning

Also the UI is very simple since its all terminal based.

---

## 🔮 Future Scope

* Add GUI (maybe using Tkinter or web based frontend)
* Use database instead of JSON
* Improve analysis with actual ML models
* Add export feature (PDF or CSV)
* Maybe make a mobile version in future

---

## 🙌 Final Note

This project started as a simple idea but became more detailed as features were added step by step. Some parts of the code could probably be written better, but overall it works fine and was a good learning experience.

There might be small bugs here and there but nothing major as far as tested.

---

## 👤 Author

Aviraj Singh Thakur   
25BCE10894   
VIT Bhopal University, Sehore, MP   
