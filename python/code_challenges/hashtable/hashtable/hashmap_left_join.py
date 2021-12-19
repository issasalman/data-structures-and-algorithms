from hashtable.hashtable import HashTable

def left_join(left_hash ,right_hash):
    """
    Leftjoin function to check every key Synonym with its Antonym
    """
    left_join_arr = HashTable()
    output = []
    for key in left_hash.keys:
        if right_hash.contains(key) :
            left_join_arr.add(key,[left_hash.get(key),right_hash.get(key)])
        else:
            left_join_arr.add(key,[left_hash.get(key),'None'])
    for key in left_join_arr.keys:
             output.append([key, left_join_arr.get(key)[0],left_join_arr.get(key)[1]])
    return output


left_hash = HashTable()

left_hash = HashTable()
left_hash.add('fond', 'enamored')
left_hash.add('wrath', 'anger')
left_hash.add('delight', 'employed')
left_hash.add('outifit', 'garp')
left_hash.add('guide', 'usher')


right_hash = HashTable()

right_hash.add('fond', 'averse')
right_hash.add('wrath', 'delight')
right_hash.add('delight', 'idle')
right_hash.add('guide', 'follow')
right_hash.add('flow', 'jam')


print(left_join(left_hash,right_hash))
