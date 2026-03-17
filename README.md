# 📊 CGPA Calculator Telegram Bot

#Calculate your CGPA instantly using a simple Telegram bot
#Bot:https://t.me/diucoverBot

---

## 🚀 Overview

cgpa_calculator_bot is a lightweight Telegram bot that helps students quickly calculate their CGPA by entering credit and grade pairs.

The bot is designed for simplicity — no complicated steps, just type your data and get the result instantly.
It runs continuously using Railway deployment, making it accessible anytime.

---

## ✨ Features

### 🔢 CGPA Calculation

* Calculate CGPA in seconds
* Supports multiple courses input
* Accurate weighted calculation

### 💬 Simple Interaction

* Easy command-based usage
* Clean and minimal interface
* Beginner-friendly input format

### ⚠️ Error Handling

* Detects invalid input
* Prevents division by zero
* Guides user with correct format

### ⚡ Fast Response

* Instant calculation
* Lightweight and efficient

---

## 📥 How It Works

1. Start the bot
2. Type `/cgpa`
3. Enter credits and grades like this:

```
3 3.75 4 3.50 3 4.00 
```

4. Bot calculates and returns your CGPA

---

## 🛠 Tech Stack

* Python 3
* python-telegram-bot
* Railway (Deployment)
* asyncio

---

## 🌐 Deployment

* Hosted on Railway
* Runs 24/7
* Uses environment variables for security

Required variable:

```
TOKEN=your_telegram_bot_token
```

---

## 📁 Project Structure

```
cgpa_calculator_bot/
│
├── bot.py              # Main bot logic
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

---

## ⚙️ Run Locally

Clone the repository:

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

Install dependencies:

```
pip install -r requirements.txt
```

Set your token:

```
export TOKEN=your_telegram_bot_token
```

Run the bot:

```
python bot.py
```

---

## 📌 Example

Input:

```
3 3.75 4 3.50 3 4.00
```

Output:

```
Your CGPA = 3.73
```

---

## ⚠️ Notes

* Input must be in credit-grade pairs
* Keep your bot token private
* Check logs if bot stops responding

---

## 👤 Author

Developed by Najmul Hassan
