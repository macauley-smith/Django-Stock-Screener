from django.shortcuts import render
import requests
from .models import Stock

def get_stock_data(request):
    if request.method == 'POST':
        symbol = request.POST['symbol']
        api_key = 'API_KEY_GOES_HERE'
        base_url = 'https://www.alphavantage.co/query?'
        function = 'GLOBAL_QUOTE'
        datatype = 'json'
        final_url = f"{base_url}function={function}&symbol={symbol}&apikey={api_key}&datatype={datatype}"
        response = requests.get(final_url)
        raw_data = response.json()

        try:
            error_message = raw_data.get("Note")
            if error_message:
                data = {"error": error_message}
            else:
                symbol = raw_data["Global Quote"]["01. symbol"]
                open_price = raw_data["Global Quote"]["02. open"]
                high_price = raw_data["Global Quote"]["03. high"]
                low_price = raw_data["Global Quote"]["04. low"]
                price = raw_data["Global Quote"]["05. price"]
                volume = raw_data["Global Quote"]["06. volume"]
                latest_trading_day = raw_data["Global Quote"]["07. latest trading day"]
                previous_close = raw_data["Global Quote"]["08. previous close"]
                change = raw_data["Global Quote"]["09. change"]
                change_percent = raw_data["Global Quote"]["10. change percent"]

                data = {
                    "symbol": symbol,
                    "open": open_price,
                    "high": high_price,
                    "low": low_price,
                    "price": price,
                    "volume": volume,
                    "latest_trading_day": latest_trading_day,
                    "previous_close": previous_close,
                    "change": change,
                    "change_percent": change_percent,
                }
        except KeyError:
            error_message = "Incorrect symbol. Please try again."
            data = {"error": error_message}

    else:
        data = None

    return render(request, 'stocks/stock_data.html', {'data': data})








