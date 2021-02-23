import random
import pyttsx3

# voice part
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Introduction part
reader= print("Hello listener, Hope you are doing great!!")
speak(" Hello listener, Hope you are doing great!! ")
print("welcome to Random story speaker")
speak("welcome to Random story speaker")
speak("what is your name?")
readername=input("what is your name? Type here  \n")
speak("Hello " + readername)
print("Hello " + readername)


#random story generation and selection
def story():
    speak(" Please enter the number of the story you want to listen from the following list ")
    print(" Please enter the number of the story you want to listen from the following list ")
    speak("1 Controlling Anger ")
    speak("2 The Farmer and the Well ")
    speak("3 Believe in Yourself ")
    speak("4 The Wolf")
    print('''
        1.Controlling Anger
        2.The Farmer and the Well
        3.Belive in Yourself
        4.The Wolf
        ''')
story()
choice = int(input("enter your choice: "))

while choice != 0:
    if choice == 1:
        names = ["Rohit", "Ben", "Rahul", "Andrew"]
        relation = ["Mother", "Father", "Grandmother", "Grandfather"]
        peroid = ["weeks", "days", "months"]
        randomname = random.choice(names)
        randomrelation = random.choice(relation)
        randomperiod = random.choice(peroid)
        story1 = "There was a young boy named " + randomname + " who had problem in controlling his temper. When he become angry he used to say anything which comes to his mind and make " + randomrelation + " hurt. One day his " + randomrelation + " gave him bag of nails and said 'every time you get angry hammer a nail on the wall. After few " + randomperiod + " the boy emptied half the bag of nails. Then,As " + randomperiod + " passed the bag became empty. His " + randomrelation + " asked him to remove nails from the wall. when the boy removed the last nail from the wall his " + randomrelation + " told him to observe the wall and said The wall is never going to be the same, even after repainting. Likewise, when you say mean things in anger, you will leave a scar in the " + randomrelation + " mind,as the nails did to the wall. Moral of the story: Anger is a dangerous weapon"
        print(story1)
        speak(story1)

        break

    elif choice == 2:
        animal = ["dog", "cat", "Rabbit", "Hamster"]
        thing = ["well", "tank full of water", ]

        randomanimal = random.choice(animal)
        randomthing = random.choice(thing)

        story2 = "A " + randomanimal + " and her babies lived on a farm, where there was a " + randomthing + " The mother told the babies , do not go near the " + randomthing + " or play around it. One of the babies wondered why they shouldn’t go to the " + randomthing + " and decided to explore it. He went to the " + randomthing + " . Climbed up the wall and peeked inside. In there, he saw his reflection and thought it was another " + randomanimal + " . The babies saw that the other " + randomanimal + " in the " + randomthing + " (his reflection) was doing whatever he was doing, and got angry for imitating him. He decided to fight with the " + randomanimal + " and jumped into the " + randomthing + ", only to find no " + randomanimal + " there. He made noise and swam until the farmer came and rescued him. The babies had learned his lesson. Moral of the story: Always listen to what the elders say. Question them, but do not defy them."
        print(story2)
        speak(story2)

        break


    elif choice == 3:
        girlname = ["Anita", "Geeta", "Riya", "Vaishnavi"]
        place = ["Gulmarg", "Manali", "Tawang", "Chopta"]
        work = ["sheppards", "Farmers"]

        randomgirlname = random.choice(girlname)
        randomplace = random.choice(place)
        randomwork = random.choice(work)

        story3 = " There was a girl named " + randomgirlname + " who grew up in " + randomplace + ". Her parents were " + randomwork + ". " + randomgirlname + " found a lot of tourists visit her village. Watching people from everywhere the planet visit her village made " + randomgirlname + " curious. 'What are these people doing here father?' asked " + randomgirlname + " . " + randomgirlname + " father laughed and said,' they have all come to climb those mountains. 'Amazed at their courage, " + randomgirlname + " said, 'Really father? Is it possible to climb to the top?' 'Of course dear,' replied her father. Many people do it. Someday, I will be able to climb to the highest of these majestic mountains said " + randomgirlname + " with a resounding streak of hope, a burning dream brewing in her eyes. But Life had other plans for her. " + randomgirlname + " lost one among her legs when she was thirteen. Clouds of despair overshadowed her happy world. 'l will never be ready to climb those mountains,' cried " + randomgirlname + ". Her father loved her dearly. He couldn't see his little girl in pain. He too was devastated. But he did not loose heart. One day " + randomgirlname + " father built her a peg, a wooden leg, which she could wear and walk. 'Never say 'never'. Start climbing the mountains,'said the determined father. " + randomgirlname + " was beside herself with joy. She wore the wooden limb and walked, and fell. Stood up, and tried to run, and fell again. The entire village laughed at the daddy and daughter's foolishness. But nothing pulled them down. Both the father and daughter were determined to win against all odds. They kept practicing. After five years Anita made it to the highest of the mountains. And she made her father very proud of her, along with her country. Moral: Never let words of discouragement pull you down. Always believe yourself."
        print(story3)
        speak(story3)
        break

    elif choice == 4:

        otheranimal = ["Sheep", "Dog", "cat", "Hen"]
        food = ["lamb", "chiken", "mutton"]
        expression = ["ahh", "wow"]
        randomotheranimal = random.choice(otheranimal)
        randomfood = random.choice(food)
        randomexpression = random.choice(expression)

        story4 = "One day a wolf was chased away from a farm for trying to steal some of the " + randomotheranimal + " for food. Later that week, the wolf came back to the farm hoping to find some food. He peeped inside the house and found the farmer and his family feasting on " + randomfood + " roast . "  + randomexpression + "! he thought. If I were to do the same thing that the farmer and his family are doing now, I would be shunted and chased, or even killed for killing a weak innocent " + randomfood + ". The moral of the story We are quick to judge and condemn others for what they do, but see nothing wrong in doing so ourselves. "
        print(story4)
        speak(story4)
        break

    else:
        print("Please choose a valid option")
        speak("Please choose a valid option")
    break
print()
speak("Hope you enjoyed the story")
print("Hope you enjoyed the story")
print("Thank you for choosing me. Have a great day")
speak("Thank you for choosing me. Have a great day")