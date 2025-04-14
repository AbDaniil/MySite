from django.shortcuts import render
from django.core.cache import cache
from . import prepare_data


def index(request):
    words = prepare_data.get_word_data()
    rules = prepare_data.get_rules_data()
    return render(request, "index.html", context ={"words" : words, "rules" : rules})

def add_rule(request):
    return render(request, "rule_add.html")

def send_rule(request):
    if request.method == "POST":
        cache.clear()
        new_rule = request.POST.get("new_rule", "")
        new_tags = request.POST.get("new_tags", "")
        context = {}
        if len(new_rule) == 0:
            context["success"] = False
            context["comment"] = "Вы забыли добавить правило"
        else:
            context["success"] = True
            context["comment"] = "Ваше правило принято"
            new_tags = new_tags.lower()
            tags_to_add = new_tags.split(";")
            prepare_data.write_rule(new_rule, tags_to_add)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "rule_request.html", context)
    else:
        add_term(request)

def add_word(request):
    return render(request, "word_add.html")

def send_word(request):
    if request.method == "POST":
        cache.clear()
        new_word = request.POST.get("new_word", "")
        new_tr = request.POST.get("new_tr", "")
        new_img = request.POST.get("new_img", "")
        new_tags = request.POST.get("new_tags", "")
        context = {}
        if len(new_word) == 0:
            context["success"] = False
            context["comment"] = "Вы забыли добавить слово"
        elif len(new_tr) ==0:
            context["success"] = False
            context["comment"] = "Вы забыли добавить перевод"
        else:
            context["success"] = True
            context["comment"] = "Ваше слово принято"
            new_tags = new_tags.lower()
            tags_to_add = new_tags.split(";")
            prepare_data.write_word(new_word, new_tr, new_img, tags_to_add)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "rule_request.html", context)
    else:
        add_term(request)

def tagged_list (request) :
    tags = prepare_data.get_tags()
    data = prepare_data.get_word_data()
    return render(request, "tagged_list.html", context = {"tags" : tags, "data" : data})

def test (request):
    word = ["some"]
    context = {}
    a,b,c= prepare_data.get_data_for_test()
    context["word"] = a
    context["tr"] = b
    context["img"] = c
    return render(request, "test_page.html", context)

def search_tag(request):
    if request.method == "POST":
        cache.clear()
        tag = request.POST.get("tag_for_search", "")
        words = prepare_data.get_words_with_tag(tag)
        return render(request, "search_tag.html", context = {"words" : words})
    else:
        tagged_list(request)