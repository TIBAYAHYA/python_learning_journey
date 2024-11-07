import sys
emojies_dict = {
":)" : "smiley",
":()": "sad",
":D" : "BIG SMILEY"
}
print("please enter a text")
inputed_text = input()
inputed_list = inputed_text.split(" ")
def emojie_converter(possible_emote):
    for word in inputed_list:
        final_result = " "
        final_result += emojies_dict.get(word, word)
        return final_result
print(emojie_converter(inputed_list))
sys.exit