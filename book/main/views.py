from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def lection_1(request):
    return render(request, 'lections/lection_1.html')


def lection_2(request):
    return render(request, 'lections/lection_2.html')


def lection_3(request):
    return render(request, 'lections/lection_3.html')


def lection_4(request):
    return render(request, 'lections/lection_4.html')


def lection_5(request):
    return render(request, 'lections/lection_5.html')


def lection_6(request):
    return render(request, 'lections/lection_6.html')


def lection_7(request):
    return render(request, 'lections/lection_7.html')


def practice_1(request):
    return render(request, 'practice/practice_1.html')


def practice_2(request):
    return render(request, 'practice/practice_2.html')


def practice_3(request):
    return render(request, 'practice/practice_3.html')


def practice_4(request):
    return render(request, 'practice/practice_4.html')


def last_test(request):
    return render(request, 'last_test.html')
