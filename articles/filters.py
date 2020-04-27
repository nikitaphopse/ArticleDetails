import django_filters
from django_filters import CharFilter
from .models import Article


class ArticleFilter(django_filters.FilterSet):
    rfid = CharFilter(field_name='rfid', lookup_expr='icontains', label=u"RFID")

    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['storage_location', 'article_num', 'price']

