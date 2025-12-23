import time
import random
#Sentence for each difficulty level
easy_sentences=[
    "The sun rises in the east.",
    "I am Yasir Khan.",
    "Can you come with me,please?",
    "Hello, I love you",
    "I am going to my home."
]
medium_sentences=[
    "Programming needs focus and regular practice as well as patience while facing errors.",
    "Artificial Intelligence is changing the world.",
    "Time Management is valueable skill in life.",
    "Yasir Khan is a Multi Billionaire,a very famous person.",
    "Programming is not difficult for hard workers only."
]
hard_sentences=[
    "Precision and consistency are essential for mastering keyboard typing.",
    "Power is a famous book about various life changing hacks like consistency and discipline.",
    "Complex problems require critical and analytical thinking.",
    "Programm written in Low level language is callled a machine code and can be easily run without compiler."
]
def calculate_accuracy(original,typed):
    original_words=original.split()
    typed_words=typed.split()
    correct=0
    for o,t in zip(original_words,typed_words):#o,t=>for one word whether original or typed
        if o==t:
            correct+=1
    accuracy=(correct/len(original_words))*100
    return accuracy
def typing_test():
    print("===Typing Speed Test===")
    print("Choose Your level.")
    print("1.Easy")
    print("2.Medium")
    print("3.Hard")
    choice=int(input("Enter your level(1-3):"))
    if choice==1:
        sentence=random.choice(easy_sentences)
    elif choice==2:
        sentence=random.choice(medium_sentences)
    elif choice==3:
        sentence=random.choice(hard_sentences)
    else:
        print("Invalid choice!Try again")
        return
    print("Type the following sentence..")
    print("-------------------------------------------------")
    print(sentence)
    print("---------------------------------------------------")
    input("Press Enter when you are ready....")
    #Start timer
    start_time=time.time()
    typed=input("Start typing here:")
    end_time=time.time()
    #Time taken in seconds
    time_taken=end_time-start_time
    #Calculate words per minute
    word_count=len(typed.split())
    wpm=(word_count/time_taken)*60#wpm=>word per minute
    #Accuracy
    accuracy=calculate_accuracy(sentence,typed)
    print("===Results===")
    print(f"Time taken:{time_taken}seconds")
    print(f"Words typed:{word_count}")
    print(f"Words per minute:{wpm}")
    print(f"Accuracy:{accuracy}%")
typing_test()

    


