from django import forms
from .models import Item

class BaseItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('image', 'name', 'category', 'price', 'currency', 'detail')

class NewItemForm(BaseItemForm):
    class Meta(BaseItemForm.Meta):
        pass

class EditItemForm(BaseItemForm):
    class Meta(BaseItemForm.Meta):
        fields = BaseItemForm.Meta.fields + ('out_of_stock',)
