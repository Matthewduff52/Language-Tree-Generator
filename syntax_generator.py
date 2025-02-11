import random

def split(string):
    List = string.split()
    return List

def restring(List):
    string = ' '.join(List)
    return string

def basic_word_order(word_order):
    word_orders = ['SOV','SVO','VSO','VOS','OVS','OSV']
    order_weights = [0.41, 0.354, 0.069, 0.018, 0.008, 0.003]
    order = random.choices(word_orders, order_weights)[0]
    order_list = list(order)
    word_order.append(order)
    return order_list, word_order

def nouns_order(new_sample,new_parts,word_order):
    art_include = ['y art','n art']
    art_weights = [0.5, 0.5]
    arts = random.choices(art_include, art_weights)[0]

    if arts == 'n art':
        new_sample = new_sample.replace("The ", "")
        new_sample = new_sample.replace("the ", "")
        new_parts = new_parts.replace("art.subj.sing ", "")
        new_parts = new_parts.replace("art.obj.sing ", "")
    else:
        pass

    word_order.append(arts)
    
    orders = ['n adj','adj n']
    order_weights = [0.5, 0.5]
    adj_order = random.choices(orders, order_weights)[0]

    if adj_order == 'n adj':
        new_sample = new_sample.replace("quick brown fox", "fox quick brown")
        new_sample = new_sample.replace("lazy dog", "dog lazy")
        new_parts = new_parts.replace("adj.subj.sing adj.subj.sing N.subj.sing", "N.subj.sing adj.subj.sing adj.subj.sing")
        new_parts = new_parts.replace("adj.obj.sing N.obj.sing", "N.obj.sing adj.obj.sing")
    else:
        pass

    word_order.append(adj_order)

    # is preposition: part of verb, after verb, before obj
    prep_orders = ['after verb','before obj']
    order_weights = [0.5, 0.5]
    prepositions = random.choices(prep_orders, order_weights)[0]

    if prepositions == 'after verb':
        # remove 'over ' and 'prep '
        # change 'jumps' to jumps over' and 'verb.3.sing.pres' to 'verb.3.sing.pres prep'
        new_sample = new_sample.replace("over ", "")
        new_parts = new_parts.replace("prep ", "")
        new_sample = new_sample.replace("jumps clearly", "jumps clearly over")
        new_sample = new_sample.replace("clearly jumps", "clearly jumps over")
        new_parts = new_parts.replace("adv.3.sing.pres verb.3.sing.pres", "adv.3.sing.pres verb.3.sing.pres prep")
        new_parts = new_parts.replace("verb.3.sing.pres adv.3.sing.pres", "verb.3.sing.pres adv.3.sing.pres prep")
    elif prepositions == 'before obj':
        pass

    word_order.append(prepositions)
    
    return new_sample, new_parts, word_order

def verbs_order(sample,parts,word_order):
    word_orders = ['clearly jumps','jumps clearly']
    order_weights = [0.5, 0.5]
    verb_order = random.choices(word_orders, order_weights)[0]

    word_order.append(verb_order)

    new_sample = sample.replace("clearly jumps", verb_order)
    new_parts = parts
    if verb_order == "jumps clearly":
        new_parts = parts.replace("adv.3.sing.pres verb.3.sing.pres", "verb.3.sing.pres adv.3.sing.pres")
        return new_sample, new_parts, word_order
    else:
        return new_sample, new_parts, word_order

def reorder(sample_list,parts_list,word_order):
    order, word_order = basic_word_order(word_order)
    new_sample = []
    new_parts = []
    # based on order: take from sample_list and put into new_sample
    combined_parts = [
        ' '.join(parts_list[0:4]),  # 'art adj adj subj'
        ' '.join(parts_list[4:6]),  # 'adv verb'
        ' '.join(parts_list[6:10])  # 'prep art adj obj'
        ]
    combined_sample = [
        ' '.join(sample_list[0:4]),  # 'art adj adj subj'
        ' '.join(sample_list[4:6]),  # 'adv verb'
        ' '.join(sample_list[6:10])  # 'prep art adj obj'
        ]
    for item in order:
        if item == 'S':
            new_sample.append(combined_sample[0])
            new_parts.append(combined_parts[0])
        elif item == 'O':
            new_sample.append(combined_sample[2])
            new_parts.append(combined_parts[2])
        elif item == 'V':
            new_sample.append(combined_sample[1])
            new_parts.append(combined_parts[1])
            
    new_sample = restring(new_sample)
    new_parts = restring(new_parts)
    
    return new_sample, new_parts, word_order

def generate_order():
    sample = 'The quick brown fox clearly jumps over the lazy dog'
    parts = 'art.subj.sing adj.subj.sing adj.subj.sing N.subj.sing adv.3.sing.pres verb.3.sing.pres prep art.obj.sing adj.obj.sing N.obj.sing'

    sample_list = split(sample)
    parts_list = split(parts)
    word_order = []

    new_sample, new_parts, word_order = reorder(sample_list,parts_list,word_order)
    new_sample, new_parts, word_order = verbs_order(new_sample,new_parts,word_order)
    new_sample, new_parts, word_order = nouns_order(new_sample,new_parts,word_order)

    print(new_sample)
    print(new_parts)
    print (word_order)

generate_order()
