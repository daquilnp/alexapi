def convert_numbers(textnum, numwords={}):

    if not numwords:
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

        scales = ['hundred', 'thousand', 'million', 'billion',
                  'trillion']

        numwords['and'] = (1, 0)
        for (idx, word) in enumerate(units):
            numwords[word] = (1, idx)
        for (idx, word) in enumerate(tens):
            numwords[word] = (1, idx * 10)
        for (idx, word) in enumerate(scales):
            numwords[word] = (10 ** (idx * 3 or 2), 0)

    movie_splice = textnum.split()
    index = 0
    new_movie_splice = []
    while index <= len(movie_splice) - 1:
        if movie_splice[index] in units or movie_splice[index] in tens \
            or movie_splice[index] in scales:
            new_entity = movie_splice[index]
            if index < len(movie_splice) - 1:
                index += 1
            else:
                is_number_done = True
                new_movie_splice.append([new_entity, 1])
                break
            is_number_done = False
            while not is_number_done:
            	if ((movie_splice[index -1] in units) \
            		and (movie_splice[index] in units)):
					new_movie_splice.append([new_entity, 1])
					new_movie_splice.append([movie_splice[index], 1])

					is_number_done = True
					index += 1 
					break
            	elif ((movie_splice[index -1] in units or movie_splice[index -1] in tens) \
            		and (movie_splice[index] in tens)):
					new_movie_splice.append([new_entity, 1])
					new_movie_splice.append([movie_splice[index], 1])

					is_number_done = True
					index += 1 
					break
                                  		
                elif movie_splice[index] in units or movie_splice[index] \
                    in tens or movie_splice[index] in scales:
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
                        if movie_splice[temp_index] in units \
                            or movie_splice[temp_index] in tens \
                            or movie_splice[temp_index] in scales:
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
			current = result = 0
			for word in section[0].split():
			        if word not in numwords:
			          return ["Could not query movie properly.", 0]

			        scale, increment = numwords[word]
			        current = current * scale + increment
			        if scale > 100:
			            result += current
			            current = 0
			result_string = "{0}{1} ".format(result_string,str(result + current))
        else:
        	result_string = "{0}{1} ".format(result_string, section[0])
    return [result_string, 1]