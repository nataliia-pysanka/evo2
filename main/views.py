from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# from .forms import EmailForm
from .models import Person
from pathlib import Path
import json


class NameForm(forms.Form):
    name = forms.CharField(label="Ім'я:")
    surname = forms.CharField(label="Прізвище:")


def index(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            name = f'{form.cleaned_data["name"]} {form.cleaned_data["surname"]}'
            try:
                p = Person.objects.get(name=name)
            except Person.DoesNotExist:
                p = Person(name=name)
                p.save()
                return render(request, 'main/greet.html', {'greetings': f'Вітаю, {name}'})
            return render(request, 'main/greet.html', {'greetings': 'Вже бачились'})
        else:
            return render(request, 'main/index.html', {'form': form})
    return render(request, 'main/index.html', {'form': NameForm()})


def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'main/persons_list.html', {'persons_list': persons})


BASE_DIR = Path(__file__).resolve().parent / 'static'
path = [
    BASE_DIR / 'main/american-names-master/firstnames_f.json',
    BASE_DIR / 'main/american-names-master/surnames.json',
]


def read_file(file_name):
    with open(file_name, "r") as f:
        text = json.load(f)
    return text


def config(request):
    names = read_file(path[0])
    surnames = read_file(path[1])
    for name, surname in zip(names, surnames):
        p = Person(name=f'{name} {surname}')
        p.save()
    return HttpResponseRedirect(reverse('main:persons_list'))
