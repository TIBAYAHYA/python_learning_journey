#random quiz generator
import random



capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#This code generates a quiz for 35 students
#the goal is to generate 50 quizs for each students, the quizs must be in random order to prevent the students from cheating

for quiz_number in range(35):
    
    quiz_file = open(f"quiz_file{quiz_number+1}.txt","w")  
    answer_file = open(f"answer_file{quiz_number+1}.txt","w")
    answer_file.write(f"quiz number{quiz_number+1}\n\nName:\n\nClass:\n\n")
    stats = random.sample(list(capitals.keys()),50)
    for questions_number in range(50):
        
        
        correct_answer = capitals[stats[questions_number]]
        wrong_answers = list(capitals.values())
        wrong_answers.remove(correct_answer)
        wrong_answers = random.sample(wrong_answers,3)
        answer_options = [correct_answer] + wrong_answers
        random.shuffle(answer_options)
        quiz_file.write(f"question {questions_number+1}:what is the capital of: {stats[questions_number]} ?\n")
        
        for x in range(4):
            quiz_file.write(f"{"ABCD"[x] }-{answer_options[x]}\n")
    quiz_file.close()
    answer_file.close()
            
            
            
    


