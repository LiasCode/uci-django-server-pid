from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def getData(request):
  data = request.data
  result = process_orders(data.get('orders'), data.get('criterion'))
  if type(result) == str:
    return Response({"error": result})
  return Response({"total": result})

# orders: [
#   {
#     id: integer
#     item: string
#     quantity: integer
#     price: float
#     status: completed | pending | canceled
#   }
# ]

# type Criterion : completed | pending | canceled | all

def process_orders(orders, criterion):
    total = 0
    error = "Error: Invalid Price Format"

    for order in orders:
        if order["price"] < 0:
            return error
        if criterion == 'completed':
            if order['status'] == 'completed':
                total += order['price'] * order['quantity']
        elif criterion == 'pending':
            if order['status'] == 'pending':
                total += order['price'] * order['quantity']
        elif criterion == 'canceled':
            if order['status'] == 'canceled':
                total += order['price'] * order['quantity']
        elif criterion == 'all':
            total += order['price'] * order['quantity']
    return total
