from django import forms

from rss_reader_service import settings


class AddUrlForm(forms.Form):
    url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}),
                         label='Enter RSS feed URL here to track its news')


class NewsParametersForm(forms.Form):
    url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}),
                         label='Enter a feed URL to read, leave empty to read all cached feeds',
                         required=False
                         )
    limit = forms.IntegerField(label='Enter a number of news to read, leave empty to read all cached news',
                               required=False,
                               )
    date = forms.DateField(label='Enter date of news to read. Input format YYYY/MM/DD, e.g. 2022/06/01,\n'
                                 'leave empty to read news of all dates',
                           required=False,
                           )


class FreshNewsParametersForm(forms.Form):
    url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}),
                         label='Enter a valid feed URL to read',
                         required=True
                         )
    limit = forms.IntegerField(label='Enter a number of news to read, leave empty to read all found news',
                               required=False,
                               )
