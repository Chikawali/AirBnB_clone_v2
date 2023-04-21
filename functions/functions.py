def to_dict(string = list):
    """this function help me convert a sting evaluation to a dict"""
    dic = []  
    for i in string:
        string_list = i.split("=")
        ids = ["city_id","place_id","state_id","amenity_id", "review_id","user_id","base_model_id","id"]
        string_list[1] = remove_quotes(string_list[1])
        string_list[1] = remove_under(string_list[1])
        if string_list[0] in ids:
            dic.append(tuple(string_list)) 
            continue
        try:
            try:
                if string_list[0] not in ids and "." in string_list[1] :
                    string_list[1] = float(string_list[1])
                    dic.append(tuple(string_list)) 
                    continue
            except:
                pass
            
            string_list[1] = int(string_list[1])
        except:
            pass
        dic.append(tuple(string_list))  
    return(dict(dic))
        
def remove_under(string):
    string_list = list(string)
    char_to_swap = "_"
    new_char = " "
    # Iterate over the list and swap the character
    for i in range(len(string_list)):
        if string_list[i] == char_to_swap:
            string_list[i] = new_char

    # Convert the list back to a string
    new_string = "".join(string_list)
    return new_string

def remove_quotes(string):
    string_list = list(string)
    char_to_swap = '\"'
    new_char = ""
    # Iterate over the list and swap the character
    for i in range(len(string_list)):
        if string_list[i] == char_to_swap:
            string_list[i] = new_char

    # Convert the list back to a string
    new_string = "".join(string_list)
    return new_string    

