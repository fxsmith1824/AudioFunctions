# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 11:50:32 2022

Still a work in progress - currently does not find Unrelated options

@author: fxsmith
"""

### PARAMETERS FOR MATCHES

# Do all Target/Cohort/Rhyme options need to be the same orthographic length?
# Set to True/False
equal_lengths = False

# Minimum Target/Cohort overlap in characters - Set to None or desired number
cohort_overlap = None

# Minimum Target/Rhyme overlap in character - Set to None or desired number
rhyme_overlap = None

# Word list - any number of strings indicating which words to try to combine
# into target/cohort/rhyme combinations

wordlist = ['bale', 'bait', 'pail', 'roach', 
'bat', 'bag', 'mat', 'hand', 
'bath', 'bass', 'path', 'couch', 
'beak', 'beet', 'sneak', 'map', 
'bear', 'base', 'pear', 'jet', 
'beaver', 'lightbulb', 'mushroom', 'panther', 
'beef', 'bean', 'thief', 'gash', 
'beg', 'bet', 'leg', 'rink', 
'bell', 'bed', 'well', 'chalk', 
'berry', 'barrel', 'fairy', 'jacket', 
'bone', 'boat', 'phone', 'fox', 
'book', 'bush', 'hook', 'wave', 
'boot', 'boom', 'suit', 'badge', 
'bowl', 'bolt', 'pole', 'vine', 
'break', 'brain', 'steak', 'wolf', 
'broom', 'tomb', 'pen', 'vet', 
'bug', 'bud', 'jug', 'vein', 
'building', 'passport', 'honey', 'snowman', 
'butter', 'button', 'putter', 'whistle', 
'cage', 'cave', 'gauge', 'hip', 
'cape', 'kale', 'nun', 'red', 
'carrot', 'carriage', 'parrot', 'tadpole', 
'cash', 'cat', 'sash', 'dip', 
'cavern', 'cashew', 'tavern', 'banner', 
'children', 'marble', 'target', 'padlock', 
'chin', 'braid', 'home', 'wet', 
'clown', 'cloud', 'wine', 'yell', 
'coat', 'cone', 'vote', 'ram', 
'coffee', 'coffin', 'toffee', 'badger', 
'crown', 'crowd', 'drown', 'soup', 
'dash', 'rash', 'boar', 'crate', 
'dent', 'desk', 'tent', 'brush', 
'dice', 'cuff', 'plant', 'leash', 
'ditch', 'disk', 'witch', 'tube', 
'dollar', 'dolphin', 'collar', 'hammock', 
'drain', 'stain', 'coke', 'meal', 
'field', 'feet', 'shield', 'run', 
'fork', 'fort', 'cork', 'moose', 
'gear', 'geek', 'beer', 'judge', 
'ghoul', 'goose', 'fool', 'cow', 
'gnome', 'note', 'comb', 'doll', 
'god', 'pod', 'mutt', 'nerve', 
'grape', 'grate', 'drape', 'can', 
'gum', 'gut', 'drum', 'whale', 
'ham', 'hat', 'jam', 'cane', 
'hanger', 'handle', 'onion', 'pigeon', 
'heart', 'harp', 'cart', 'golf', 
'hole', 'hose', 'goal', 'cap', 
'horn', 'horse', 'corn', 'bib', 
'lab', 'lamb', 'crab', 'tire', 
'lace', 'lake', 'pup', 'job', 
'letter', 'lettuce', 'sweater', 'cannon', 
'light', 'line', 'kite', 'cheese', 
'lips', 'list', 'chips', 'tape', 
'log', 'van', 'nest', 'wash', 
'mad', 'mask', 'bench', 'car', 
'mail', 'maid', 'nail', 'bike', 
'match', 'catch', 'serve', 'hedge', 
'mess', 'chair', 'tank', 'peas', 
'mime', 'mice', 'dime', 'calf', 
'mob', 'mop', 'knob', 'hoof', 
'mountain', 'mousetrap', 'fountain', 'window', 
'mouse', 'mouth', 'house', 'chain', 
'mug', 'mud', 'pug', 'cool', 
'mustard', 'mustache', 'custard', 'penguin', 
'night', 'knife', 'bite', 'jar', 
'paddle', 'package', 'saddle', 'monkey', 
'pan', 'patch', 'fan', 'lime', 
'park', 'part', 'bark', 'den', 
'pat', 'pad', 'rat', 'king', 
'peach', 'peace', 'beach', 'hair', 
'pick', 'pit', 'kick', 'deer', 
'pin', 'pig', 'fin', 'hut', 
'plate', 'plane', 'gate', 'shack', 
'porch', 'port', 'torch', 'milk', 
'pumpkin', 'basket', 'nickel', 'radish', 
'race', 'rake', 'face', 'dome', 
'reach', 'reef', 'leech', 'joint', 
'read', 'bead', 'moon', 'salt', 
'rip', 'rib', 'ship', 'dog', 
'river', 'liver', 'kayak', 'bandage', 
'road', 'rope', 'toad', 'web', 
'robber', 'robin', 'perfume', 'ladder', 
'rocket', 'rocker', 'pocket', 'bubble', 
'root', 'roof', 'chute', 'man', 
'rose', 'robe', 'nose', 'pool', 
'scout', 'pout', 'hoop', 'pack', 
'shark', 'sharp', 'lark', 'gush', 
'sheep', 'sheet', 'leap', 'ball', 
'shell', 'shed', 'tail', 'week', 
'sick', 'sip', 'wick', 'door', 
'skunk', 'skull', 'trunk', 'peel', 
'snail', 'snake', 'moat', 'keg', 
'sock', 'sod', 'dock', 'lap', 
'socket', 'soccer', 'locket', 'filling', 
'sun', 'sub', 'bun', 'laugh', 
'swing', 'ring', 'jeep', 'leak', 
'sword', 'cord', 'heel', 'paint', 
'tack', 'tab', 'back', 'purse', 
'tag', 'tap', 'seam', 'crib', 
'tailor', 'table', 'sailor', 'muffin', 
'tart', 'tarp', 'dart', 'mash', 
'team', 'teen', 'flag', 'deck', 
'thorn', 'fence', 'grill', 'skate', 
'throne', 'throat', 'crone', 'dish', 
'thug', 'thumb', 'hug', 'rice', 
'tin', 'tick', 'win', 'same', 
'tool', 'tune', 'mule', 'vase', 
'trap', 'trash', 'nap', 'fist', 
'tug', 'tub', 'rug', 'mic', 
'turtle', 'turkey', 'hurdle', 'banjo', 
'twig', 'twin', 'dig', 'newt', 
'type', 'tile', 'pipe', 'coach', 
'vest', 'dam', 'cake', 'slug', 
'walk', 'wall', 'clock', 'raft', 
'wheat', 'wheel', 'seat', 'gem', 
'wig', 'wind', 'fig', 'buzz', 
'wizard', 'willow', 'lizard', 'bottle', 
'yarn', 'yard', 'barn', 'safe', 
'zit', 'zip', 'sit', 'coal',]

def split_word(word):
    '''
    
    This function will find the location of the character after the onset 
    consonant cluster + first vowel or vowel cluster and the location of 
    the the first vowel in a given word.
    
    Parameters
    ----------
    word : STR
        A string of any length that serves as the target word.

    Returns
    -------
    cohort_split : INT
        Index of the first character after the onset consonant cluster + 
        first vowel(s) - useful for [:cohohort_split] string indices to select
        only the "beginning" of a target word to find cohort matches.
    rhyme_split : INT
        Negative index of the first vowel - useful for [rhyme_split:] string
        indices to select all but the onset consonants of a target word to
        find rhyme matches.

    '''
    for index, char in enumerate(word):
        if char in 'aeiouy':
            cohort_split = index
            rhyme_split = index
            while True:
                if word[cohort_split+1] in 'aeiouy':
                    cohort_split += 1
                else:
                    break
            cohort_split += 1
            rhyme_split = rhyme_split - len(word)
            break
    return cohort_split, rhyme_split

item_sets = []

for word in wordlist:
    target = word
    cohort_split, rhyme_split = split_word(target)
    if cohort_overlap != None:
        cohort_split = cohort_overlap
    if rhyme_overlap != None:
        rhyme_split = -rhyme_overlap
    
    cohort_options = [cohort for cohort in wordlist 
                      if cohort[:cohort_split] == target[:cohort_split] 
                      and cohort != target]

    rhyme_options = [rhyme for rhyme in wordlist 
                     if rhyme[rhyme_split:] == target[rhyme_split:] 
                     and rhyme != target]
    
    if equal_lengths:
        cohort_options = [cohort for cohort in cohort_options
                          if len(cohort) == len(target)]
        rhyme_options = [rhyme for rhyme in rhyme_options
                         if len(rhyme) == len(target)]
    
    if len(cohort_options) == 0 or len(rhyme_options) == 0:
        continue
    
    for cohort in cohort_options:
        for rhyme in rhyme_options:
            item_set = [target, cohort, rhyme]
            item_sets.append(item_set)
  
'''
This was my attempt to ensure that there were no shared characters between
rhymes and cohorts but it was including the vowel clusters, which obviously
guaranteed overlap - might fix later and add back in at the beginning of the
nesteed loop on line 212

            if len(set(cohort[:cohort_split]) & set(rhyme[:cohort_split])) > 0:
                continue
            if len(set(cohort[rhyme_split:]) & set(rhyme[rhyme_split:])) > 0:
                continue
'''