import json

import django
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


def load(request, addr):
    with open('json1.json', 'r') as json1_file:
        json1_data = json.load(json1_file)
        node = json1_data
        check = 0
        a = 0
        lis = request.path.strip('/').split("/")
        for tag in lis:
            if check == 0:
                check = 1
                if node['slug'] == lis[-1]:
                    break
            else:
                    if node['slug'] == lis[a] and node['kind'] == 'Topic':
                        b = a + 1
                        for child in node['children']:
                            if child['slug'] == lis[b]:
                                node = child
                                a = a + 1
                                break
                            else:
                                continue
       if node['slug'] == lis[-1]:
            link = settings.MEDIA_URL + "styles.css"
            if node['kind'] == 'Topic':
                return render(request, 'parent.html', {'node': node, 'link': link})
            else:
                return render(request, 'child.html', {'node': node, 'link': link})
        else:
            return HttpResponse("Invalid Url")
