from django import forms


class AuthorForm(forms.Form):
    author_name = forms.CharField(label="Author name", max_length=50)
    author_surname = forms.CharField(label="Author surname", max_length=50)


class GenreForm(forms.Form):
    genre_name = forms.CharField(label="Genre Name", max_length=50)
    genre_description = forms.CharField(label="Description Name", max_length=50)
