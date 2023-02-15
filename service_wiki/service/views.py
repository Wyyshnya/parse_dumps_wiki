from django.http import JsonResponse, HttpResponse
import json
import time
from django.shortcuts import render
from .models import Content, Category, CategoryContent
from .serializers import ContentSerializer, ContentSerializer1


def get_statistic_all(request):
    result = {}
    querry = Category.objects.all()
    for category in querry:
        count = CategoryContent.objects.filter(category=category).values().distinct().count()
        result[category.category_name] = count

    return render(request, 'base.html', {'hr': result})


def get_statistic(request, name):
    result = {}
    querry = Category.objects.get_by_natural_key(name)
    count = CategoryContent.objects.filter(category=querry).values().distinct().count()
    result[querry.category_name] = count

    return render(request, 'base.html', {'hr': result})


def get_article(request, name):
    obj = Content.objects.get_by_natural_key(name)
    obj.timestamp = obj.timestamp.timestamp()
    obj.create_timestamp = obj.create_timestamp.timestamp()
    return HttpResponse(json.dumps(ContentSerializer(obj).data, ensure_ascii=False), content_type="application/json")


def get_formatted_article(request, name):
    obj = Content.objects.get_by_natural_key(name)
    obj.timestamp = obj.timestamp.timestamp()
    obj.create_timestamp = obj.create_timestamp.timestamp()
    return render(request, 'base.html', {'hr': ContentSerializer1(obj).data})


def do_base(request):
    with open('static/ruwikiquote-20230213-cirrussearch-general.json', 'r') as file:
        stack = []
        result = []
        local_str = ""
        while True:
            try:
                symb = file.read(1)
                local_str += symb
                if symb == '{':
                    stack.append('{')
                elif symb == '}' and len(stack):
                    stack.pop()
                    if not len(stack):
                        try:
                            data = json.loads(local_str)
                            if len(data['template']) >= 0:
                                content = Content.objects.create_content(data)
                                if len(data['title']) > 1:
                                    for title in data['title']:
                                        category = Category.objects.create_category(name=data['title'])
                                        CategoryContent.objects.create_ship(category=category, content=content)
                                elif len(data['title']):
                                    category = Category.objects.create_category(name=data['title'])
                                    CategoryContent.objects.create_ship(category=category, content=content)
                        except KeyError:
                            local_str = ""
                        except json.decoder.JSONDecodeError as err:
                            local_str = ""

            except IOError:
                break
    return HttpResponse("Well Done!")
