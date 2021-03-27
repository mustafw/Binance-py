import BinanceAPI

### How much euros(€) affords to buy only one dollar($)
USD_EUR=BinanceAPI.Prices().get_currency("USD", "EUR")
EUR_USD=BinanceAPI.Prices().get_currency("EUR", "USD")
print(f"You can buy a Dollar($) for {USD_EUR['rate']} Euro(s)")
print(f"You can buy a Euro(€) for {EUR_USD['rate']} USD(s)")

XRP_USDT=BinanceAPI.Prices().get_coin("XRP", "USDT", pass_status=True)
DOGE_BTC=BinanceAPI.Prices().get_coin("DOGE", "BTC", pass_status=False) #### IT RETURNS TO TUPLE WHEN YOU SET "pass_status=True". SO YOU NEED TO SELECT RETURNED VALUE WITH "[0]". "[1]" STANDS FOR COIN'S STATUS
print(f"You can buy a XRP for {XRP_USDT['rate']} USDT(s)", f"XRP_USDT LAST 24HOUR INFORMATION: {XRP_USDT['24H']}")
print(f"You can buy a DOGE for {DOGE_BTC[0]['rate']} BTC(s)", f"DOGE_BTC LAST 24HOUR INFORMATION: {DOGE_BTC[0]['24H']}")
print(f"DOGE_BTC Status: {DOGE_BTC[1]}")






