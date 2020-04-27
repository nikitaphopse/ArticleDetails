from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

        labels = {
            'rfid': 'RFID',
            'storage_location': 'Storage Location',
            'article_num': 'Article Number',
            'price': 'Price(in EUR)',
            'article_name': 'Article Name'
        }


def __init__(self, *args, **kwargs):
    super(ArticleForm, self).__init__(*args, **kwargs)
    self.fields['storage_location'].required = False
