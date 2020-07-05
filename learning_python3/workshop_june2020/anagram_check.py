words = ['Bag', 'State', 'Cat', 'Night', 'Bat', 'Apple', 'Listen', 'Dusty', 'Thing', 'Act', 'Inch', 'Nest', 'Funeral', 'dog', 'Bird', 'Silent', 'God', 'Chin', 'Study', 'Taste']

anagram_group = {}

for word in words:
    key = ''.join(sorted(word.lower()))
    value = anagram_group.get(key, [])
    value.append(word)
    anagram_group[key] = value

for key, value in anagram_group.items():
    if len(value)>1:
        print (value)
