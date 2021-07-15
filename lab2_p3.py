import random
import time
import math



test_sent = []
fin_time = []

count = 6
def random_sentence(count):
    intro_words = ["how can ", "when do ", "where can ", "how do "]
    middle_words = ["the ducks ", "your parents ", "the kids ", "your squids "]
    last_words = ["get to work?", "swim home?", "play guitar?", "throw lemons?"]
    i = 0
    while i < count:
        sample = (random.choice(intro_words) + random.choice(middle_words) + random.choice(last_words))
        print(sample)
        start = time.time()
        sentence = input()


        if sentence == sample:
            print ("found")
            time.sleep(2)
        else:
            print ("wrong")
        total = round(time.time() - start , 2)
        test_sent.append(sample)
        fin_time.append(total)
        i += 1
        print (round((total),2))


def write_results(count):
    writefile = open("times.txt", "a")

    #printing header for stats
    writefile.write(
    "\n                   Stats                \n" 
    "--------------------------------------------\n"
    "sentence:\t\t\t\t\t\t\t\t time:\n"
    "--------------------------------------------\n")

    j = 0
    while j < count:
        writefile.write(test_sent[j] + " :\t\t" + str(fin_time[j]) + "\n")

        j += 1

    writefile.write("average time" + str(sum(fin_time)/len(fin_time)))
    writefile.close()


random_sentence(count)
write_results(count)