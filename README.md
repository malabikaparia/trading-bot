# Trading Bot (Binance Futures Testnet)
- Modular design separating CLI, validation, and API layers for maintainability
## Features
- MARKET and LIMIT order support
- CLI input handling
- Input validation and error handling
- Logging to file
- Modular structure (client, orders, validators)

## Setup
pip install -r requirements.txt

## Run

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001

Limit Order:
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --qty 0.001 --price 30000

## Example Error
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --qty 0.001

Output:
ERROR ❌: Price required for LIMIT order

## Note
Uses mock response due to testnet access limitations.