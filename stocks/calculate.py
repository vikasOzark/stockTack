# from . import stock_search
from .stock_search import previous_date
from .models import MyPortfolio

def stock_value(request):
    try:
        # getting the data from the database
        portfolio_data = MyPortfolio.objects.filter(user=request.user)

        # getting the data from the API
        total_stock = 0
        total_stock_value = 0
        total_PL = 0
        current_value = 0

        for data in portfolio_data:
            quantity  = data.stock_quantity
            # adding quantity to the total stock
            total_stock += quantity

            price = data.purchased_price
            # adding total price to the total stock value
            total_stock_value += quantity * price

            # getting the current price of the stock
            try:
                current_price = previous_date(data.stock_name)['price']
                # adding the current price to the current value
                current_value += quantity * current_price
            except:
                current_price = 425
                current_value = 1500

            # calculating the profit/loss
            PL = (current_price - price) * quantity
            total_PL += PL
    except:
        total_stock = 0
        total_stock_value = 0
        total_PL = 0
        current_value = 0
    data = {
        'total_stock': total_stock,
        'total_stock_value': total_stock_value,
        'total_PL': round(total_PL, 2),
        'current_value' : round(current_value, 2)
        }
    return data