from django import forms

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
    profile_picture = forms.FileField(label="Upload Profile Picture")
    favorite_drinks = forms.MultipleChoiceField(
    label="Favorite Drinks",
    choices=[
        ('coffee', 'Coffee'),
        ('tea', 'Tea'),
        ('juice', 'Juice'),
    ],
    widget=forms.CheckboxSelectMultiple)