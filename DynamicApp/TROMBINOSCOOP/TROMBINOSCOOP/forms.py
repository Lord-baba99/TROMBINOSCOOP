from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Courriel')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        # verifie que les deux champs sont valides
        if password and email:
            if password != 'alk' and email != 'mail@domain.com':
                raise forms.ValidationError("Adresse de couriel ou mot de passe erroné.")
        return cleaned_data
