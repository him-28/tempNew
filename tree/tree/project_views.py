import django
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from random import randrange

# Load method converts json to python dict
def load(request, addr):
    colors = ['#FA8072','#ADFF2F','pink','#87CEEB','#D2B48C','#00FF7F','#F4A460','#FFDAB9','#FFDEAD','#00FF00']
    rand_no = randrange(10)
    x = colors[rand_no]
    with open('json1.json', 'r') as json1_file:
        json1_data = json.load(json1_file)
        node = json1_data
    check = 0
    leaf = 0
    tree = request.path.strip('/').split("/")
    for param in tree:
            # condition to enter in node, which is in dictionary 
            if check == 0:
                check = 1
                pre = param
                if node['slug'] == tree[-1]:
                    break
            # condition to enter in others which are in list 
            else:
                    # condition to check  url, else  redirect 
                    if node['slug'] == pre and node['kind'] == 'Topic':
                        branch = leaf + 1
                        for child in node['children']:
                            if child['slug'] == param:
                                node = child
                                leaf = leaf + 1
                                break
                    pre = param 
                            
    # the last slug in the list is checked here                            
    if node['slug'] == tree[-1]:
            
            if node['kind'] == 'Topic':
                return render(request, 'proj.html', {'title': node['title'], 'node': node, 'randcolor':x})
            else:
                return render(request, 'pro.html', {'title': node['title'], 'node': node ,  'randcolor':x})
    else:
            return HttpResponse("Invalid Url")

            
            
