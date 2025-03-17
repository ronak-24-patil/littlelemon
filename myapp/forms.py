from django import forms
from .models import Logger

class CustomerForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100, initial ="enter a name")
    email = forms.EmailField(label="Your Email", help_text="Enter a valid email address.")
    reservation_date = forms.DateField(
        label="Reservation Date",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    favorite_dish = forms.ChoiceField(
        label="Favorite Dish",
        choices=[
            ('pizza', 'Pizza'),
            ('salad', 'Salad'),
            ('kebab', 'Kebab'),
        ],
        widget=forms.RadioSelect
    )
    
    favorite_drinks = forms.MultipleChoiceField(
    label="Favorite Drinks",
    choices=[
        ('coffee', 'Coffee'),
        ('tea', 'Tea'),
        ('juice', 'Juice'),
    ],
    widget=forms.CheckboxSelectMultiple)


# Define shift choices
SHIFT_CHOICES = [
    ('morning', 'Morning Shift'),
    ('afternoon', 'Afternoon Shift'),
    ('evening', 'Evening Shift'),
]

class InputForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=200)
    last_name = forms.CharField(label="Last Name", max_length=200)
    shift = forms.ChoiceField(label="Shift", choices=SHIFT_CHOICES)
    time_log = forms.TimeField(
        label="Time Log",
        help_text="Enter the exact time.",
        required=False
    )

class LogForm(forms.ModelForm):
    class Meta:
        model = Logger  # Bind the form to the Logger model
        fields = '__all__'  # Include all fields in the form
