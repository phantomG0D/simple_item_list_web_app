from django.shortcuts import render

# Create your views here.
def item_list(request):
    context = {
        'title': 'My Brutal Item List',
        'items':
        ["Exploit Weakness",     # Find every vulnerability (in systems, people, yourself) and use it.
    "Dominate Time",        # Own the clock. Schedule, execute, repeat without mercy.
    "Hoard Knowledge",      # Accumulate skills, intel, and secrets no one else bothers to get.
    "Crush Resistance" 
    ],

        'user_authenticated': True,
        'user_name': 'phantom0'
    }

    return render(request, 'item/item_list.html', context)