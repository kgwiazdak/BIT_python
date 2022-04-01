from collections import Counter
from operator import itemgetter
from pprint import pprint

def suggest_fanpages(data_file, user_string,k):
    d = {}

    with open(data_file) as file:
        for line in file:
            user, following = line.split(" -> ")
            d[user] = following.strip().split(", ")
    main_following = set(d[user_string])
    del d[user_string]
    curr_following = [value for key, value in d.items() if key in main_following]
    flat_curr_following = []
    for arr in curr_following:
        flat_curr_following.extend(arr)
    flat_curr_following = [following for following in flat_curr_following if following not in main_following]
    count = Counter(flat_curr_following)
    count = [(key, value) for key, value in count.items()]
    count.sort(key=itemgetter(1), reverse=True)
    suggestions = [el[0] for el in count[:k]]
    return suggestions



if __name__ == '__main__':
    suggestions =suggest_fanpages("text.txt", "Mark Twain", 3)
    print(suggestions)