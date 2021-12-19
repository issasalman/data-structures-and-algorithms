from linked_list import LinkedList

class HashTable:
    """
    HashTable Class to  initialize the array size
    """
    def __init__(self, size=1024):

        self.size = size
        self.map = [None] * self.size
        self.keys = []
        self.chain = LinkedList()


    def hash(self,key):
        """
        a function to get the hash value of the key in ascii code

        """
        ascii_sum=0
        if type(key) == int:
            ascii_sum=key
        else:
            for char in key:

                 ascii_sum+=ord(char)
        return ascii_sum*11 % self.size




    def add(self, key, value):

        # def __set_item__()
        hashed_key = self.hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] = [key,value]

            self.keys.append(key)
            return [key,value]
            # self.key = [key,value]
        else:

            diction={key:value}
            self.keys.append(diction)
            if isinstance(self.map[hashed_key], LinkedList):


                self.map[hashed_key].append([key,value])
                return [key,value]
            else:

                # chain = LinkedList()

                # existing_pair = self.key
                existing_pair= self.map[hashed_key]
                new_pair =[key,value]
                self.map[hashed_key]=self.chain
                self.chain.append((existing_pair))
                self.chain.append(new_pair)

                return new_pair
        # if type(  self.map[hashed_key])== list:
        #      self.map[hashed_key]= self.map[hashed_key][1]


    def get(self, key):
        hashed_key=self.hash(key)
        if  self.map[hashed_key]==None:
             return None
        else:

            if type(  self.map[hashed_key])== list:

                return self.map[hashed_key][1]
            else:
                current =  self.map[hashed_key].head
            if current!=None:
                while current.next != None:
                    if current.value[0] == key:
                        print (current.value[1])
                        return (current.value[1])
                    current = current.next


    def contains(self, key):
        hashed_key=self.hash(key)
        if  self.map[hashed_key]==None:
               return None
        else:

            if type(  self.map[hashed_key])== list:

                return  (True)
            else:
                current =  self.map[hashed_key].head
            if current!=None:
                while current.next != None:
                    if current.value[0] == key:
                        print (True)
                        return (True)
                    current = current.next
                print ("false")
                return None


if __name__ == '__main__':
    hashtable = HashTable()
    hashtable.add('ahmad', 30)
    hashtable.add('hamad', 29)
    hashtable.add('daham', 45)
    hashtable.add('load', 45)
    hashtable.add('doal', 49)
    hashtable.add('werw', 2549)
    hashtable.add('zaid', 24)
    hashtable.add('sultan', 24)
    # hashtable.get('issa')
    hashtable.contains("werw")

    print(hashtable.keys)

    for hashed_key, item in enumerate(hashtable.map):
        if item:
            print(hashed_key, item)




