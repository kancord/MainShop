from django import forms
from.models import Category
class SearchEngineForm(forms.Form):
    # Фильтр по категории товара
    filter_cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Все товары",
                                       widget=forms.Select(attrs={'fil': 'dropdown'}), label="Категория", required=False)

    class Meta:
        model = Category
        fields = ('name')
