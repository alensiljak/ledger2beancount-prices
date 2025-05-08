# ledger2beancount-prices
ledger -> beancount price converter

Due to an issue in ledger2beancount converter, this script can be used to convert ledger prices to beancount price records.

The price records are recognized by the following regex:
```regex
P (\d{4}-\d{2}-\d{2})(?:\s+(\d{2}:\d{2}:\d{2}))?\s+([A-Z_]+)\s+([0-9.]+)\s+([A-Z]+)
```
