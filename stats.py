def get_num_words(text):
    words = text.split()
    return len(words)

def broj_karaktera(tekst):
    d = {}
    smanjeni_tekst = tekst.lower()
    for char in smanjeni_tekst:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return d

def sort_on(item):
    return item[1]

def sortirana_dict(d):
    return sorted(d.items(), key=sort_on, reverse=True)
