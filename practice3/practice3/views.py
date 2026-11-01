from django.shortcuts import render
import datetime

def home(request):
    d = {
        'name': 'Abdur-rahman',
        'age': 22,
        'city': 'Dhaka',
        'current_date': datetime.datetime.now(),
        'lst': [1, 2, 3],
        'slogan':['Speed thrills, but kills', 'Drive safe, arrive alive', 'Better late than never'],
        'courses':[
            {
                'id': 1,
                'name': 'Non-professional license course(bike)',
                'fee': 1000,
            },
            {
                'id': 2,
                'name': 'Professional license course(bile+car)',
                'fee': 2000,
            },
            {
                'id': 3,
                'name': 'Heavy license course(truck+bus)',
                'fee': 3000,
            }

        ]

    }
    return render(request, 'home.html', d)