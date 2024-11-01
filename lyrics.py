import sys
import time

def julius_speech():
    lines = [
        ("No one is going to tell me,", 0.03),
        ("what to do at what time", 0.04),
        ("I'm in charge,", 0.04),
        ("So please put that proposal on the table,", 0.06),
        ("and then let's discuss it,", 0.04),
        ("And if the need arises,", 0.03),
        ("You can't say 'MHM MHM' because", 0.05),
        ("There is a,", 0.04),
        ("..there is a rule here,", 0.04),
        ("we work according to,", 0.03),
        ("The Rules.", 0.01),
        ("We are here today,", 0.1),
        ("to say to you,", 0.07),
        ("take your ministers who are,", 0.05),
        ("Instagram celebrities,", 0.06),
        ("to go and vote for you.", 0.11),
        ("And I continued,", 0.06),
        ("And then someone said SHUT UP,", 0.09),
        ("And and,", 0.06),
        ("and I said,", 0.03),
        ("in answering that person,", 0.03),
        ("don't say UBANI,", 0.03),
        ("Because it's not you,", 0.05),
        ("OKAY TAKE A SEAT NOW,", 0.02),
        ("So I answered maybe someone from the Gallery there,", 0.05),
        ("Why is this one jumping,", 0.05),
        ("saying it's UNPARLIAMENTARY,", 0.05),
        ("YOU don't know who I'm talking to,", 0.05),
        ("stop being...", 0.05),
    ]
    
    delays = [0.3] * len(lines)
    
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='', flush=True)
            time.sleep(char_delay)  
        time.sleep(delays[i])  
        print('')

julius_speech()
