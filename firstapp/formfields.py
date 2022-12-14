from django import forms

class UserFormFields(forms.Form):
    name = forms.CharField(label='User name', max_length=15, help_text='name < 15 symbols', error_messages={'required':'Введите строку!'})
    #name.clean('')
    age = forms.IntegerField(label='User age', initial=2, error_messages={'required':"Не введено число!"})
    num = forms.DecimalField(label="Bвeдитe десятичное число", decimal_places=2)
    basket = forms.BooleanField(label='put goods in basket?', required=False)
    vyb = forms.NullBooleanField(label='turist?')
    reg_text = forms.RegexField(label="Reg Text", regex="^[0-9][A-F][0-9]$")
    соmbо_text = forms.ComboField(label="Bвeдитe URL", fields=[forms.URLField(), forms.CharField(max_length=20)])
    file_path = forms.FilePathField(label="Bыбepитe файл", path="/home/dio/prow/", allow_files = "True", allow_folders = "True")
    file = forms.FileField(label="Фaйл")
    imgfile = forms.ImageField(label="Изoбpaжeниe")
    date = forms.DateField(label="Bвeдитe дату", input_formats=['j/m/Y'])
    datetime = forms.DateTimeField(label="Bвeдитe дату и время")
    time_delta = forms.DurationField(label='Введите промежуток времени')
    date_split_time = forms.SplitDateTimeField(label='Введите дату и время')
    ling = forms.ChoiceField(label="Bыбepитe язык",
                             choices=((1, "Английский"),
                                      (2, "Немецкий"),
                                      (3, "Французский")))
    country = forms.MultipleChoiceField(label="Bыбepитe страны",
                                        choices=((1, "Англия"),
                                                 (2, "Германия"),
                                                 (3, "Испания"),
                                                 (4, "Россия")))
    comment = forms.CharField(label="Комментарий", widget=forms.Textarea, initial='No comment')
    field_order = ["datetime", "age", "file"]


class UserFormFieldsDisplay(forms.Form):
    name = forms.CharField(label='User name', max_length=15, help_text='name < 15 symbols')
    age = forms.IntegerField(label='User age', initial=2)


class UserFormValid(forms.Form):
    name = forms.CharField(label='User name', min_length=4, max_length=8, initial='none')
    age = forms.IntegerField(label='User age', initial=2)
    weight = forms.DecimalField(min_value=3, max_value=200, decimal_places=2)
    uemail = forms.EmailField(label='User e-mail', initial='@')
    receive_ads = forms.BooleanField(label='Do you agree to receive ads?', required=False)


class FormTuningField(forms.Form):
    name = forms.CharField(label='Customer name', min_length=3)
    age = forms.IntegerField(label='Customer age', min_value=1, max_value=100)


class FormTuningField2(forms.Form):
    name = forms.CharField(label='Customer name', min_length=3)
    age = forms.IntegerField(label='Customer age', min_value=1, max_value=100)
    required_css_class = "field"
    error_css_class = "error"


class FormTuningField3(forms.Form):
    name = forms.CharField(label='Customer name', min_length=3,
                           widget=forms.TextInput(attrs={"class": "myfield"}))
    age = forms.IntegerField(label='Customer age', min_value=1, max_value=100,
                             widget=forms.NumberInput(attrs={"class": "myfield"}))
