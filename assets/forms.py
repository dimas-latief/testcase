from django import forms

class AssetRequestForm(forms.Form):
    quantity = forms.IntegerField(max_value=50, 
        widget=forms.NumberInput(
            attrs={
                'class' : 'validate',
                'placeholder' : 'Request Quantity',
                'min' : 1
            }
        )
    )


