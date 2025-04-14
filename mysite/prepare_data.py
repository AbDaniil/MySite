import json
import random

def get_word_data():
    words = []
    with open("./data/words.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        cnt=0
        for item in data["data"]:
            cnt+=1
            word = item["word"]
            translation = item["translation"]
            image =item["image"]
            if item["tags"]:
                tags = item["tags"][0]
                for i in range(1, len(item["tags"])):
                    tags +=", "
                    tags+=item["tags"][i]
            else:
                tags = ""
            words.append([cnt, word, translation, image, tags])
        file.close()
    return words

def get_rules_data():
    rules=[]
    with open("./data/rules.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        cnt=0
        for item in data["data"]:
            cnt+=1
            rule = item["rule"]
            if item["tags"]:
                tags = item["tags"][0]
                for i in range(1, len(item["tags"])):
                    tags +=", "
                    tags+=item["tags"][i]
            else:
                tags = ""
            rules.append([cnt, rule, tags])
        file.close()
    return rules

def write_rule(rule, *tags):
    with open("./data/rules.json", "r", encoding="utf-8") as file:
        data=json.load(file)
        new_tags = []
        for tag in tags[0]:
            if tag != "":
                new_tags.append(tag)
            if not (tag in data["tags"]):
                data["tags"].append(tag)
        new_rule = { 'rule' : rule, 'tags' : new_tags}
        data["data"].append(new_rule)
    with open("./data/rules.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def write_word(word, tr, img, *tags):
    with open("./data/words.json", "r", encoding="utf-8") as file:
        data=json.load(file)
        new_tags = []
        for tag in tags[0]:
            if tag != "":
                new_tags.append(tag)
            if not (tag in data["tags"]):
                data["tags"].append(tag)
        new_word = { 'word' : word, 'translation' : tr, 'image' : img, 'tags' : new_tags}
        data["data"].append(new_word)
    with open("./data/words.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def get_tags():
    with open("./data/words.json", "r", encoding="utf-8") as file:
        data=json.load(file)
        tags1 = data["tags"]
    with open("./data/words.json", "r", encoding="utf-8") as file:
        data=json.load(file)
        tags2 = data["tags"]
    tags3 = tags1+tags2
    tags = list(set(tags3))
    tags.sort()
    return tags


def get_data_for_test():
    with open("./data/words.json", "r", encoding="utf-8") as file:
        data=json.load(file)
        n = random.randint(0, len(data["data"])-1)
        word = data["data"][n]["word"]
        tr = data["data"][n]["translation"]
        img = data["data"][n]["image"]
    return word, tr, img


def get_words_with_tag(tag):
    words=[]
    with open("./data/words.json", "r", encoding="utf-8") as file:
        data=json.load(file)
        cnt=0
        for item in data["data"]:
            if tag in item["tags"]:
                cnt+=1
                word = item["word"]
                translation = item["translation"]
                image =item["image"]
                words.append([cnt, word, translation, image])
        file.close()
    return words