import re


# HERE REMOVE JUST THE @ SYMBOL AND PUT A SPACE IR YOUR PLACE..
def remove_at_sign(s):
    return re.sub('@', ' ', s)


# HERE REMOVE JUST THE leathers
def remove_letters(s):
    return re.sub('[a-zA-Z]', '', s)


# HERE REMOVE JUST THE SOME SPECIAL CHARACTERS
def remove_some_special_characters(s):
    return re.sub(r"[-()\"#;<>{}`+=~|.!?,]", "", s)
