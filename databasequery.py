import json
import jaro
from os import path

filename = "data_storage.json"

def main():

    with open(filename) as fp:
        objects = json.load(fp)

    recipeNames = []
    for currDict in objects:
        recipeNames.append(list(currDict.keys())[0])


    exactString = "Cacio E Pepe"
    nonCaseString = "cacio e pepe"
    substringMatchVal = "Cacio"

    print(exact_string_comparison(exactString, recipeNames))
    print(exact_string_ignore_case(nonCaseString, recipeNames))
    print(similar_substring(substringMatchVal, recipeNames))



 #given a string and list, returns the index of the string. If not, returns -1
def exact_string_comparison(inputVal, lst):
    if(inputVal in lst):
        return lst.index(inputVal)
    else:
        return -1

#same as exact string comparison, but not case sensitive
def exact_string_ignore_case(inputVal, lst):
    lowerList = lst
    lowerList = [item.lower() for item in lowerList]

    if (inputVal in lowerList):
        return lowerList.index(inputVal)
    else:
        return -1

def similar_substring(inputVal, lst):

    # if there is not an exact match already in there
    jaro_dict = {}
    jaro_lst = []
    if (inputVal not in lst):
        for ind, val in enumerate(lst):
            curr_jaro = jaro.jaro_winkler_metric(inputVal, val)
            jaro_dict[ind] = curr_jaro
            jaro_lst.append(curr_jaro)

    for value, key in enumerate(jaro_dict):
        if(jaro_dict[value] == max(jaro_lst) and max(jaro_lst) > 0.70):
            return key

    return -1

main()