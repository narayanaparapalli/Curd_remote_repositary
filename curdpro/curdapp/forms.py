from django import forms
class ProductForm(forms.Form):
    p_id=forms.IntegerField(
        label='Enter product id',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'product id'
            }
        )
    )
    p_name = forms.CharField(
        label='Enter product name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product name'
            }
        )
    )
    p_cost = forms.IntegerField(
        label='Enter product cost',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product cost'
            }
        )
    )
    p_color = forms.CharField(
        label='Enter product color',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product color'
            }
        )
    )
    p_class = forms.CharField(
        label='Enter product class',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product class'
            }
        )
    )
    c_name = forms.CharField(
        label='Enter your name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your name'
            }
        )
    )
    c_mobile = forms.IntegerField(
        label='Enter your mobile',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your mobile'
            }
        )
    )
    c_email = forms.EmailField(
        label='Enter your email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your email'
            }
        )
    )
class UpdateForm(forms.Form):
    p_id = forms.IntegerField(
        label='Enter product id',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product id'
            }
        )
    )
    p_cost = forms.IntegerField(
        label='Enter product cost',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product cost'
            }
        )
    )
class DeleteForm(forms.Form):
        p_id = forms.IntegerField(
            label='Enter product id',
            widget=forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'product id'
                }
            )
        )