import random

from django.http import Http404
from django.shortcuts import render

from .data import departures, description, subtitle, title, tours


def main_view(request):
    rand_tours = dict(random.sample(tours.items(), 6))
    context = {
        'title': title,
        'subtitle': subtitle,
        'description': description,
        'departures': departures,
        'rand_tours': rand_tours,
    }
    return render(request, 'tours/main.html', context=context)


def departure_view(request, departure):
    try:
        dep = departures[departure]
    except KeyError:
        raise Http404
    filtered_tours = {key: val for key, val in tours.items() if val['departure'] == departure}
    prices = [t['price'] for t in filtered_tours.values()]
    nights = [t['nights'] for t in filtered_tours.values()]
    amount_tours = len(filtered_tours)
    min_price = min(prices)
    max_price = max(prices)
    min_nights = min(nights)
    max_nights = max(nights)
    context = {
        'title': title,
        'departures': departures,
        'departure': dep,
        'min_price': min_price,
        'max_price': max_price,
        'min_nights': min_nights,
        'max_nights': max_nights,
        'filtered_tours': filtered_tours,
        'amount_tours': amount_tours,
    }
    return render(request, 'tours/departure.html', context=context)


def tour_view(request, id):
    try:
        tour = tours[id]
    except KeyError:
        raise Http404
    context = {
        'title': title,
        'subtitle': subtitle,
        'description': description,
        'departures': departures,
        'tour': tour,
    }
    return render(request, 'tours/tour.html', context=context)
