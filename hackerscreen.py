"""
Algorithm
"""
"""
max_category -  int - 20
min_category -  int - 0
change -  int - 10
wait - int - 2
word_time - int - 2
word_interval - int - 0.25

while true:
    fake = sleep(wait)
    os.system('cls')
    loop through and
        if change > max || change < min: change *= -1
        add change to category of hacker type
    end
    print three lines
        one list of hacked items
        one of something suggesting censorship
        one last line of jargon
    while true:
        print new word
        break at new line
    print last message
    display gone

Written by MKH to display what it might look like to write over ISIS or IRL hackers. #DISCLAIMER: I DO NOT CONDONE HACKING OR VIOLENCE; THE PURPOSE OF THIS PIECE OF CODE IS TO SHARE MY HOMEWORK WITH FUTURE PROFESSOR AND FUTURE EMPLOYER.
"""

from time import sleep # <--- added from time import sleep
import os, random # <----- added os, random (for use further down the script or for clear)
max_category = 10 # <----- amount of words in each category
min_category = 0 # <----- to keep changing length of words *10
change = 0 # <----- to change the length of how often words change
wait = 0.66 # <----- length of wait it takes before compileing a new line (MS)
word_time = 0.50 # <----- length of wait it takes before the words flash both after each other (MS)
word_interval = 0.25 # <----- length between words when randomised below

# <---- print outs for the categories
hacked_items = ["Google Documents", "YouTube", "P O S E D D O N", "S p a c e X", "CIA MainFream Computer", "FBI MainFrame Computer", "Snap Chat", "Weather Channel", "Disney Site", "Hackolodic Hackagemy Mainframe Computer", "Khay Lok Phra Kroh (Chatuchak) Map", "Private Hotel Database", "Black Rock City Map", "O C U S C U S", "La X Mas", "Private Bank Website", "Rex MediaNet", "Corporate Security Cameras","London CCTV monitoring","Netflix","eBay","Virgin Medias","Virgin Airlines","Octopus Energy","New York Stock Exchange","British Stock Exhange","London Stock Exchange",]

censorship_items = ["our destop view is being blocked by the corporate scumbags", "corporate mainstream media becken calls blockage", "private security hacking from powerful illegal off shore investment groups \"W O O T\"", "dealing with a bugest amount of data security sources", "now securing hacktivisme spy researchers local data","PUSHING VKS DATABASE!", "INCREASING ISOLATION & DEPRIVATION OF THE POLICE STATE SCUMBAGS IN THIER NYPD DATA!", "ENHANCING FIREWALL AGAINST DECRACKING!!!!", "PLEASE WAIT: INITIALISING A.I. DECODER", "SSSSSSSSSSSSSSSSSSSSHHHHHHHHHHHHHHHHHHHHH", "FLASH FLASH!!", "CENSORSHIP FAILED PLEASE RESTART","Private Hotel Database", "Black Rock City Map", "O C U S C U S",]

# <---- new entorely to add the random words inbetween to make it more life like
transition_words = ["buiding", "broght", "enganged", "activated", "loading", "acktivating", "crkacking", "detecting", "pinpointng", "finding", "encrypting", "tracing", "rising", "tracking", "lashing", "seccussing", "upgrading", "accesing", "decoding", "shocking", "through"]


jargon = ["Hacker Screen Loaded", "Ofline", "WiFi Detected", "Illegal D.i.S.C.", "IP Found", "IP Resolved", "Adjented", "Unknow", "Subforstid", "Awkword", "Legal", "Illegal", "Censor", "Corporate Cenzorcorprate SCUMBAG", "Foren Waterdog", "COPYRIT HACKT (CN)", "Hacking in Progess", "Writting SSD HDD System", "Travling", "Locating", "L.a.X.a.T.i.o.P.u.T.r.T.u.M", "Living Past Work", "Living Off SETI 1 at the Moon","Atom Smasher Protocol Engaged"]

# <--------- this is where the random words generated from each category from above 
# <------------ this is also where in tincotain each line is secured un til next phrases
while True:
    sleep(wait)
    os.system("cls")
    for i in range (3):
        pos = int(random.randint(0, len(hacked_items)-1))
        print (hacked_items[pos])
        #print("\n")
    for i in range (3):
        pos = int(random.randint(0, len(censorship_items)-1))
        print (censorship_items[pos])
        #print("\n")
    for i in range (1):
        pos = int(random.randint(0, len(jargon)-1))
        print (jargon[pos])
        #print("\n")
    while True:
        pos = int(random.randint(0, len(transition_words)-1))
        print(transition_words[pos], end=" ")
        sleep(word_time)
        break
    pos = int(random.randint(0, len(transition_words)-1))
    print(transition_words[pos])
