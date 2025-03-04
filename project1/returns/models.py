from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="checkout_orders")
    order_id = models.CharField(max_length=20, unique=True)
    product_name = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.product_name}"


class OrderReturn(models.Model):
    ORDER_RETURN_STATUSES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=ORDER_RETURN_STATUSES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Return Request for {self.order.order_id}"
