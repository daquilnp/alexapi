import logging
from word2number import w2n
logging.basicConfig()


logger = logging.getLogger()
logger.setLevel(logging.INFO)
def is_valid_number(word):
    try:
        if compare_word_in_units(word):
            return True
        elif compare_word_in_tens(word):
            return True
        elif compare_word_in_scales(word):
            return True
        else:
            return False
    except:
        return False
def word2number(word):
    return w2n.word_to_num(word)
def compare_word_in_units(word):
    units = [
            'zero',
            'one',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine',
            'ten',
            'eleven',
            'twelve',
            'thirteen',
            'fourteen',
            'fifteen',
            'sixteen',
            'seventeen',
            'eighteen',
            'nineteen',
            ]
    try:
        return word in units
    except:
        return False
def compare_word_in_tens(word):
    try:
        tens = [
            '',
            '',
            'twenty',
            'thirty',
            'forty',
            'fifty',
            'sixty',
            'seventy',
            'eighty',
            'ninety',
            ]
        return word in tens
    except:
        return False
def compare_word_in_scales(word):
    try:
        scales = ['hundred', 'thousand', 'million', 'billion',
                  'trillion']
        return word in scales
    except:
        return False
def convert_numbers(textnum, numwords={}):
    
    movie_splice = textnum.split()
    index = 0
    new_movie_splice = []
 
    while index <= len(movie_splice) - 1:

        if is_valid_number(movie_splice[index]):
            new_entity = movie_splice[index]

            if index < len(movie_splice) - 1:
                index += 1

            else:
                is_number_done = True
                new_movie_splice.append([new_entity, 1])
                break
            is_number_done = False
            while not is_number_done:
            
                if (compare_word_in_units(movie_splice[index -1])) \
                    and (compare_word_in_units(movie_splice[index])):
                    new_movie_splice.append([new_entity, 1])
                    new_movie_splice.append([movie_splice[index], 1])

                    is_number_done = True
                    index += 1 
                    break
                elif ((compare_word_in_units(movie_splice[index -1]) or compare_word_in_tens(movie_splice[index -1])) \
                    and (compare_word_in_tens(movie_splice[index]))):
                    new_movie_splice.append([new_entity, 1])
                    new_movie_splice.append([movie_splice[index], 1])

                    is_number_done = True
                    index += 1 
                    break
                                        
                elif compare_word_in_units(movie_splice[index]) or compare_word_in_tens(movie_splice[index]) \
                     or compare_word_in_scales(movie_splice[index]):
                    new_entity = new_entity + ' ' + movie_splice[index]
                    index += 1
                    if index >= len(movie_splice) - 1:
                        new_movie_splice.append([new_entity, 1])
                        is_number_done = True
                        break
                else:

                    if movie_splice[index] == 'and':
                
                        temp_index = index + 1
                        if index >= len(movie_splice) - 1:
                            new_movie_splice.append([new_entity, 1])
                            is_number_done = True
                            break
                        if is_valid_number(movie_splice[temp_index]):

                            new_entity = new_entity + ' ' \
                                + movie_splice[index] + ' ' \
                                + movie_splice[temp_index]
                            index = temp_index + 1
                            
                            if index > len(movie_splice) - 1:
                                new_movie_splice.append([new_entity, 1])
                                is_number_done = True
                                break
                        else:
                            new_movie_splice.append([new_entity, 1])
                            is_number_done = True
                    else:
                        new_movie_splice.append([new_entity, 1])
                        is_number_done = True
        else:
            new_movie_splice.append([movie_splice[index], 0])
            index += 1

   
    result_string = ""
    for section in new_movie_splice:
        if section[1] == 1:
            result_string = "{0}{1} ".format(result_string,word2number(section[0]))
        else:
            result_string = "{0}{1} ".format(result_string, section[0])
    return [result_string, 1]