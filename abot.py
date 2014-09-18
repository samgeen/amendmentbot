'''
Writes amendments to the US constititon
Sam Geen & Mike Cook, August 2014
'''

import string
import chooser
from templates import templates
from websters import websters
import twython
from twython import Twython
from secrets import *

capitalise = False

def strippunc(instring):
    '''
    Strips punctuation from the input string
    '''
    return instring.translate(string.maketrans("",""), string.punctuation)

def ordinal(i):
    '''
    Totally not ripped off of stackoverflow >_>
    '''
    k=i%10
    return"%d%s"%(i,"tsnrhtdd"[(i/10%10!=1)*(k<4)*k::4])

def subwordindict(word):
    for entry in websters.iterkeys():
        if entry in word:
            # HACK FOR SPECIAL CASE
            if entry == "VERB":
                if "VERBTGTED" in word:
                    return "VERBTGTED"
            return entry
    return ""

def parse(instring):
    # Should have used a class OH WELL
    global websters
    global capitalise
    word = strippunc(instring)
    # Turn on/off capitalisation
    if word == "CAP":
        capitalise = True
        return ""
    if word == "NOCAP":
        capitalise = False
        return ""
    # Is an entry in websters in the word?
    entry = subwordindict(word)
    if entry:
        # Choose from list if this is a keyword
        output = chooser.choice(websters[entry])
        # Capitalise?
        if capitalise:
            output = ' '.join(entry[0].upper() + entry[1:] for \
                                  entry in output.split())
        websters["SAME"] = [output]
    else:
        # Not a special keyword?
        output = instring
    # If we had any punctuation left over, put it back in
    if entry:
        output = instring.replace(entry,output)
    return output

def runfortemplate(template):
    output = ordinal(chooser.choice(range(0,100)))+" :"
    # Parse the template word by word to fill in keywords
    for item in template.split(" "):
        output += " "+parse(item)
    lout = len(output)
    # Diagnostic character count (disabled for release mode)
    #output += " ("+str(lout)+")"
    # Get rid of double spaces
    output = ' '.join(output.split())
    return output

def run():
    # Set up twitter
    twitter = twython.Twython(twitter_token,twitter_secret,access_token,access_secret)
    # Pick a template to use
    template = chooser.choice(templates)
    tweet = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaargh" # yes
    while len(tweet) > 140:
        tweet =  runfortemplate(template)
    twitter.update_status(status=tweet)

if __name__=='__main__':
    run()
