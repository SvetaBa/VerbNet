from django import forms

class ContactForm(forms.Form):
    sender = forms.EmailField(
      required=True,
      label='',
      widget=forms.TextInput(
        attrs={'style': 'width:350px', 'placeholder': 'Введите email'}
        )
      )
    name = forms.CharField(
      label='',
      max_length=100,
      widget=forms.TextInput(
        attrs={'style': 'width:350px', 'placeholder': 'Введите имя'}
        )
      )
    message = forms.CharField(
      label='',
      widget=forms.Textarea(
        attrs={'style': 'width:350px','placeholder': 'Введите сообщение'}
        )
      )