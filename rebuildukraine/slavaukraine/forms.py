
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.core.validators import RegexValidator
from django.forms import DateInput, ModelForm, TextInput

from .models import Person, City, Proposal, Expertise


#from .models import Enterprise

class PersonRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address.")
    is_person = forms.BooleanField(initial=True,widget=forms.HiddenInput(), required=False,label="")
    is_enterprise = forms.BooleanField(initial=False, widget=forms.HiddenInput(), required=False,label="")
    profile_image = forms.ImageField(required=False)
    first_name = forms.CharField(label="Primeiro Nome",required=True)
    last_name = forms.CharField(label="Apelido",required=True)


    class Meta:
        model = Person
        fields= ("email","username","first_name","last_name","taxnumber","birth","taxnumber", "profile_image", "gender","birth", "address","password1","password2","is_person","is_enterprise")
        widgets= {'birth': forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={'class': 'form-control',
                   'placeholder': 'Select a date',
                   'type': 'date',
        }), }
        labels={
            'birth':"Data de nascimento",
            'username': "Nome de Utilizador",
            'first_name': "Primeiro Nome",
            'last_name': "Último Nome",
            'taxnumber':"Número de contribuinte",
            'profile_image':"Imagem de Perfil",
            'password2': "Confirmação de password",
            'address': "Morada"
        }

class PersonAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Person
        fields = ('email','password')


    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid credentials.");

class EnterpriseRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address.")
    is_person = forms.BooleanField(initial=False,widget=forms.HiddenInput(), required=False,label="")
    is_enterprise = forms.BooleanField(initial=True, widget=forms.HiddenInput(), required=False,label="")
    profile_image = forms.ImageField(required=False,label="Imagem de Perfil")
    first_name = forms.CharField(label="Nome da empresa",required=True)
    last_name = forms.CharField(label="Sigla",required=True)


    class Meta:
        model = Person
        fields= ("email","username","first_name","last_name","profile_image","taxnumber", "address","password1","password2","is_person","is_enterprise")
        labels={
            'username': "Nome da empresa",
            'taxnumber':"Número de contribuinte",
            'profile_image':"Imagem de Perfil",
            'password2': "Confirmação de password",
            'address': "Morada"
        }



class EnterpriseAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Person
        fields = ('email','password','is_person','is_enterprise')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid credentials.");


class ProposalForm(forms.ModelForm):
    #enterprise = forms.ChoiceField(widget=forms.HiddenInput(), required=False, label="")

    class Meta:
        model = Proposal
        fields = '__all__'
        widgets = {'enterprise': forms.HiddenInput}


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset= City.objects.none()
        self.fields['country'].required=True
        self.fields['country'].label = 'País'
        self.fields['city'].required = True
        self.fields['city'].label = 'Cidade'
        self.fields['expertiseNeeded'].required = True
        self.fields['expertiseNeeded'].label = 'Especialização'
        self.fields['description'].required = True
        self.fields['description'].label = 'Descrição'

        if 'country' in self.data:
            try:
                country_id= int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass #Invalid input from the cliente; Ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
