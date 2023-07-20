from django import forms

from zed_hub.main_app.models import TemplateModel


class TemplateModelCreateForm(forms.ModelForm):
    class Meta:
        model = TemplateModel
        fields = '__all__'


class TemplateModelEditForm(forms.ModelForm):
    class Meta:
        model = TemplateModel
        fields = '__all__'


class TemplateModelDeleteForm(forms.ModelForm):
    class Meta:
        model = TemplateModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance


class TemplateModelShowForm(forms.ModelForm):
    class Meta:
        model = TemplateModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
