import pprint
message1 = "hello my name is oogga I am very old and tall and big"
def character_counter(message):
    count={}
    for character in message:
        count.setdefault(character,0)
        count[character] += 1
    print(pprint.pprint(count))
character_counter(message1)
