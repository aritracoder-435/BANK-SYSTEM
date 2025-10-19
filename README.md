# BANK-SYSTEM
🪙 Banking System Project

A simple console-based banking system built in Python that allows users to sign up, sign in, and perform basic banking operations like balance enquiry, cash deposit, withdrawal, and fund transfer. The system emphasizes a clean terminal interface with smart screen clearing and secure password handling.

# ✨ Features

- ✅ User login & registration
-✅ Strong password validation
-✅ Balance enquiry, deposit, withdraw, fund transfer
-✅ Each banking operation shows confirmation
-✅ Instant feedback on actions
-✅ Menu remains visible while previous outputs clear
-✅ Smooth, professional terminal UI
-✅ Track account transactions (optional per user)
---

# ⚡ How It Works

1. Sign Up: Users create a new account. Strong password is enforced.
2. Sign In: Existing users login with their username and password.
3. Bank Services Menu:
        Users can choose any of the banking operations.
        After performing an action, the system clears only the previous output, keeping the menu visible.
4. Exit: Users can exit at any time; a thank-you message is displayed.

# 🔒 Password Requirements

    At least 8 characters
    At least one uppercase letter
    At least one lowercase letter
    At least one digit
    At least one special character (!@#$%^&* etc.)
    No spaces allowed

# 💻 Installation & Usage

1. Clone the repository:

    git clone https://github.com/aritracoder-435/Banking-System.git

2. Navigate into the project directory:

    cd Banking-System

3. Ensure you have Python installed (3.8+ recommended).

4. Install required packages (if any):

    pip install -r requirements.txt

5. Run the project:

    python main.py

6. Follow the on-screen instructions to SignUp, SignIn, and perform banking operations.


# 📂 Project Structure

Banking-System/
│
├── main.py           # Main program
├── register.py       # Handles signup & signin
├── Bank.py           # Bank class with banking services
├── customer.py       # Customer class
├── database.py       # Database connection & queries
└── README.md         # Project description

# 👨‍💻 Author

Aritra Mandal
Developed with ❤️
GitHub: https://github.com/aritracoder-435