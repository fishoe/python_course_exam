def parse_awesome_string(awesome_string):
    awesome_words = awesome_string.split(' ')
    really_awesome_word = None
    awesome_flag_count = 0
    is_previous_word_awesome = False
    for word in awesome_words:
        if awesome_flag_count > 2:
            really_awesome_word = word
            break
        if word in ["hey", "yo", "wow"] and not is_previous_word_awesome:
            awesome_flag_count += 1
            is_previous_word_awesome = True
        else:
            is_previous_word_awesome = False

    if really_awesome_word is None:
        raise Exception("Really Awesome Word Not Found!")
    
    if really_awesome_word in ["hey", "yo", "wow"]:
        raise Exception("Really Awesome Word Not Found!")
    
    if len(really_awesome_word) < 5:
        raise Exception("Really Awesome Word Not Found!")
    
    if really_awesome_word.islower():
        raise Exception("Really Awesome Word Not Found!")
    
    return really_awesome_word
