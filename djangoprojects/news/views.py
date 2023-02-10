from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm


def news_main(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_main.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_main')
        else:
            error = 'Вы неверно ввели форму, повторите попытку.'
    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
