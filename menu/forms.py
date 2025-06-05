from django import forms
from .models import Item, Category

class BaseItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = Item
        fields = ('image', 'name', 'category', 'price', 'currency', 'detail')

class NewItemForm(BaseItemForm):
    class Meta(BaseItemForm.Meta):
        pass

class EditItemForm(BaseItemForm):
    class Meta(BaseItemForm.Meta):
        fields = BaseItemForm.Meta.fields + ('out_of_stock',)
