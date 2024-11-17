from django.shortcuts import render
from django.db import connections
from .models import Search1, Search2, Search3

def find_data(request):
    data_db1 = Search1.objects.using('default').values_list('item', flat=True)
    data_db2 = Search2.objects.using('db2').values_list('item', flat=True)
    data_db3 = Search3.objects.using('db3').values_list('item', flat=True)

    all_items = list(data_db1) + list(data_db2) + list(data_db3)

    if request.method == 'POST':
        selected_item = request.POST.get('selected_item')
        database_name = ''
        if selected_item in data_db1:
            database_name = 'db'
        elif selected_item in data_db2:
            database_name = 'db2'
        elif selected_item in data_db3:
            database_name = 'db3'

        return render(request, 'find_data.html', {
            'selected_item': selected_item,
            'database_name': database_name,
        })

    return render(request, 'find_data.html', {
        'items': all_items,
    })
