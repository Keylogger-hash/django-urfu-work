from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(label="Full name", max_length=40)
    email = forms.EmailField(label="Email", max_length=50)
    username = forms.CharField(label="Username", max_length=20)
    password = forms.CharField(
        label="Password",
        min_length=10,
        max_length=20,
        widget=forms.PasswordInput,
    )
