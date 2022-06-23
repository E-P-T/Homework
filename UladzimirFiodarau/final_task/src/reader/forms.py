from django import forms


class AddUrlForm(forms.Form):
    url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}),
                         label='Enter RSS feed URL here to track its news')
