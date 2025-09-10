from django.shortcuts import render

# Create your views here.
def item_list(request):
    context = {
        'title': 'My Brutal Item List',
        'items': ['Apple', 'Banana', 'Cherry', 'Durian'],
        'user_authenticated': True,
        'user_name': 'phantom0'
    }

    return render(request, 'item/item_list.html', context)