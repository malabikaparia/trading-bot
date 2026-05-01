# Trading Bot (Binance Futures Testnet)

## Overview

This project implements a simplified trading bot for Binance Futures (USDT-M) with a focus on clean architecture, input validation, and structured logging. It supports placing MARKET and LIMIT orders through a command-line interface.

The design emphasizes modularity, separating concerns across client, order handling, validation, and CLI layers.
## Features
* Place MARKET and LIMIT orders
* Support for BUY and SELL operations
* CLI-based user input handling
* Input validation with clear error messages
* Logging of requests, responses, and errors
* Modular and reusable code structure

## Project Structure
trading-bot/
│
├── bot/
│   ├── clients.py          # Binance client wrapper
│   ├── orders.py           # Order placement logic
│   ├── validators.py       # Input validation
│   ├── logging_config.py   # Logging setup
│
├── cli.py                  # CLI entry point
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
├── .gitignore              # Ignored files
└── bot.log                 # Log output (generated)


## Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/trading-bot.git
cd trading-bot
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

### MARKET Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001
```

### LIMIT Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --qty 0.001 --price 30000
```


## Example Output

### Successful Order
```
SUCCESS ✅

Order Summary:
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Status: FILLED
Quantity: 0.001
```

### Validation Error
```
ERROR ❌: Price required for LIMIT order
```

## Logging
All API requests, responses, and errors are logged in:

```
bot.log
```


## Note on API Integration
The application is structured to interact with Binance Futures Testnet using a dedicated client layer.

Due to inconsistencies in testnet access during development, a mock response layer was used to validate order flow, CLI interaction, logging, and error handling.

The architecture ensures that replacing the mock with real API calls requires minimal changes.



## Future Improvements
* Enable full Binance Futures Testnet integration
* Add retry logic for API/network failures
* Support advanced order types (Stop-Limit, OCO)
* Extend to multiple trading pairs and strategies
* Improve logging with structured formats (JSON)



## Key Design Decisions
* Separation of concerns for maintainability
* CLI-driven interaction for flexibility
* Validation layer to prevent invalid API calls
* Logging for observability and debugging


## Author
Malabika
