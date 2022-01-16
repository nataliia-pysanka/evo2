from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Person
from pathlib import Path
from django.utils import timezone
import json
from datetime import timedelta


class NameForm(forms.Form):
    name = forms.CharField(label="Ім'я:")
    surname = forms.CharField(label="Прізвище:")


today = timezone.now().date()
day = timedelta(hours=24)


def index(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            name = f'{form.cleaned_data["name"]} {form.cleaned_data["surname"]}'
            try:
                p = Person.objects.get(name=name)
            except Person.DoesNotExist:
                p = Person(name=name)
                p.login_date = timezone.now()
                p.save()
                data = {'greetings': f'Вітаю, {name}', 'time': today}
                return render(request, 'main/greet.html', data)
            delta = p.login_date + day
            if delta > timezone.now():
                return render(request, 'main/greet.html', {'greetings': 'Вже бачились'})
            p.login_date = timezone.now()
            p.save()
            data = {'greetings': f'Вітаю, {name}', 'time': today}
            return render(request, 'main/greet.html', data)
        else:
            data = {'form': form, 'time': today}
            return render(request, 'main/index.html', data)
    data = {'form': NameForm(), 'time': today}
    return render(request, 'main/index.html', data)


def persons_list(request):
    data = {'persons_list': Person.objects.all(), 'time': today}
    return render(request, 'main/persons_list.html', data)


BASE_DIR = Path(__file__).resolve().parent / 'static'
path = [
    BASE_DIR / 'main/american-names-master/firstnames_f.json',
    BASE_DIR / 'main/american-names-master/surnames.json',
]


def read_file(file_name):
    with open(file_name, "r") as f:
        text = json.load(f)
    return text


def clear(request):
    persons = Person.objects.all()
    for p in persons:
        p.delete()
    return HttpResponseRedirect(reverse('main:persons_list'))


def config(request):
    names = read_file(path[0])
    surnames = read_file(path[1])
    counter = 0
    for name, surname in zip(names, surnames):
        p = Person(name=f'{name} {surname}', login_date=timezone.now())
        p.save()
        counter += 1
        if counter > 300:
            break
    return HttpResponseRedirect(reverse('main:persons_list'))
