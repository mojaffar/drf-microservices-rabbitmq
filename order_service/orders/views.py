from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from .tasks import notify_new_order

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        notify_new_order.delay(order.product_name, order.user_email)