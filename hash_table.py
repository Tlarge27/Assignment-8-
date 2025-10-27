class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
       
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, number):
        index = self.hash_function(key)
        new_contact = Contact(key, number)
        new_node = Node(key, new_contact)
        
        if self.data[index] is None:
            self.data[index] = new_node
        else:
            current = self.data[index]
            while True:
                
                if current.key == key:
                    current.value.number = number
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self):
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            if self.data[i] is None:
                print("Empty")
            else:
                current = self.data[i]
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()  


# Test your hash table implementation here.  
if __name__ == "__main__":
    table = HashTable(10)
    table.print_table()
    print("\nInserting contacts...\n")
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")
    table.insert("Rebecca", "999-444-9999") 

    table.print_table()

    print("\nSearch results:")
    print("John ->", table.search("John"))
    print("Chris ->", table.search("Chris"))

#
#  A hash table is the right data structure for this project because it lets you find and store information very quickly. 
#  Instead of searching through every contact one by one like you would in a list, a hash table uses a hash function to 
#  turn each name into a specific index number. This lets the program jump straight to where the contact is stored, 
#  which makes searching, adding, and updating much faster, usually in constant time.

#  Collisions happen when two different names hash to the same index. To account for this the program uses a method called 
#  separate chaining.This means that each spot in the hash table can hold a small linked list. If two names land on the 
#  same index, the second one is simply added to the end of that list. When searching, the program just checks each node 
#  in that list until it finds the right contact. This strategy keeps the table functioning correctly even when multiple 
#  contacts share the same index.

# An engineer might choose a hash table over a list or tree when they need fast lookups by a unique key, like a name or 
# ID. A good example for this would be a phone contact list or a dictionary. Both need to find items quickly by a word or name. Hash tables 
# are ideal for this kind of task because they are fast and simple while still being able to handle collisions.
