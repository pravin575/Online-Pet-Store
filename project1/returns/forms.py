from django import forms
from .models import Order, OrderReturn



class OrderReturnForm(forms.ModelForm):
    class Meta:
        model = OrderReturn
        fields = ['order', 'reason']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the logged-in user
        super().__init__(*args, **kwargs)
        if user:
            orders = Order.objects.filter(username=user)  # Use 'username' field
            print(f"Orders for user {user}: {orders}")  # Debugging print statement
            self.fields['order'].queryset = orders
