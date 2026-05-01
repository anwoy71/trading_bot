# Trading Bot – Binance Futures Testnet

## Overview

This project is a simplified trading bot built using Python that interacts with the Binance Futures Testnet (USDT-M). It supports placing MARKET and LIMIT orders through both programmatic functions and a CLI interface.

---

## Features

* Place MARKET orders (BUY/SELL)
* Place LIMIT orders (BUY/SELL)
* CLI-based input using argparse
* Secure API key handling using `.env`
* Structured project design (client, orders, CLI, validators)
* Logging of API activity and errors

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py        # Binance client setup
│   ├── orders.py        # Order execution logic
│   ├── validators.py    # Input validation
│   ├── logging_config.py
│   └── __init__.py
│
├── cli.py               # CLI entry point
├── requirements.txt     # Dependencies
├── trading.log          # Logs
├── .env                 # API keys (not pushed to GitHub)
└── client.ipynb         # Testing notebook
```

---

## Setup Instructions

### 1. Clone repo

```
git clone https://github.com/anwoy71/trading_bot.git
cd trading_bot
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Setup API keys

Create `.env` file:

```
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

## Usage

### MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

---

## Output

* Order request summary
* Binance API response (orderId, status, executedQty, etc.)
* Success/failure message

---

## Notes

* Uses Binance Futures Testnet only (no real funds involved)
* `.env` file is excluded for security
* Logging is stored in `trading.log`

---

## Assumptions

* User has valid Binance Testnet API keys
* Futures account is enabled on testnet
* Python 3.x environment is set up

---

## Author

Anwoy
