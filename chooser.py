'''
Chose items from a list, reducing probability for items that have already been picked recently
Sam Geen & Mike Cook, September 2014
'''

import cPickle as pik

import random, os, collections

MAXLEN = 100

class ItemHistory(object):
    '''
    Makes a fixed-length queue that returns whether an item has 
    been used recently
    '''
    def __init__(self,filename):
        self._filename = filename
        self._queue = None
        self._load()

    def _load(self):
        if os.path.exists(self._filename):
            f = open(self._filename)
            self._queue = pik.load(f)
        else:
            self._queue = collections.deque(maxlen=MAXLEN)
        
    def _save(self):
        f = open(self._filename,"w")
        pik.dump(self._queue,f)

    def checkitem(self,item):
        if item in self._queue:
            #print "Item", item," in queue, REJECTED"
            return True
        else:
            self._queue.append(item)
            self._save()
            return False
    
        
class Chooser(object):
    def __init__(self):
        self._history = ItemHistory("itemhistory.dat")
    
    def choose(self,items):
        icount = 0
        while icount < 50: # Prevents a death loop if queue isn't saturated
            icount += 1
            # This checks the item history for the item, and
            #   returns if not already found
            chosen = random.choice(items)
            if not self._history.checkitem(chosen):
                return chosen
        return chosen

chooser = Chooser()

def choice(items):
    return chooser.choose(items)
