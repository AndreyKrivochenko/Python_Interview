from django import forms

from goodsapp.models import Good


class GoodCreateForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ('category', 'name', 'price', 'unit', 'provider_name')

    def __init__(self, *args, **kwargs):
        super(GoodCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
