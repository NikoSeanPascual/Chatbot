# 🧠 Simple Python Chatbot

A lightweight, interactive **terminal-based chatbot** written in Python.  
It supports conversation, jokes, facts, utilities, and simple games — all inside a loop that responds to user input.

---

## 🚀 Features

### 🗣️ Conversation (I encourage you to add more to make it feel more alive)
The chatbot responds to basic conversational prompts:
- `hi`
- `what's your name`
- `what's your objective`
- `how are you`
- `what do you like`
- `who made you`
- `how old are you`
- `what's your gender`
- `bye`

### 🕒 Utilities (I encourage you to add more to make it more useful)
Useful built-in tools:
- `time` → shows current time  
- `date` → shows today’s date  
- `coinflip` → flips a coin  
- `calculate` → evaluates math expressions  
- `weather` → random weather generator  


### 🎮 Mini Games (I encourage you to add more so there will be more games)
Fun games included:
- `guess the number` (1–10)
- `quiz game` (simple questions)
  
### 💬 Fun & Feelings (I encourage you to add more so it will be more fun) 
Extra interactive commands:
- `tell me a joke`
- `give me a fact`
- `motivate me`
- `compliment me`
- `i'm sad`
- `i'm happy`

---

## 📌 How It Works

- The program runs in a **while True** loop.
- User input is compared against:
  - a **conversation dictionary**
  - a **fun dictionary**
  - utility commands  
  - game commands
- If the command exists, the bot responds.
- If not, it prints:  
  `"I didn’t understand that. Type 'help' to see commands."`

The chatbot uses:
- `datetime` → time & date functions  
- `random` → jokes, facts, games, weather  
- `eval()` → simple math calculations  

---

## 📖 Help Menu

Typing `help` shows a full list of available commands:
