# from . import stock_search
from stock_search import previous_date
from .models import MyPortfolio

def stock_value(request):
    # getting the data from the database
    portfolio_data = MyPortfolio.objects.filter(user=request.user)
    # getting the data from the API
    total_stock = 0
    total_stock_value = 0
    total_PL = 0

    for data in portfolio_data:
        quantity  = data.stock_quantity
        # adding quantity to the total stock
        total_stock += quantity

        price = data.purchased_price
        # adding total price to the total stock value
        total_stock_value += quantity * price