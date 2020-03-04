
from players.player import Player
import random
from players.scripts.DSL import DSL

class Script10003(Player):

    def __init__(self):
        self._counter_calls = []
        for i in range(3):
            self._counter_calls.append(0)
            
    def get_counter_calls(self):
        return self._counter_calls 

    def get_action(self, state):
        actions = state.available_moves()
        
        for a in actions:
        
            if  DSL.containsNumber(a, 4 ) :
                self._counter_calls[0] += 1
                return a
                    
            if  DSL.numberPositionsProgressedThisRoundColumn(state, 2 ) > 0 :
                self._counter_calls[1] += 1
                return a
                    
            if  DSL.containsNumber(a, 5 ) :
                self._counter_calls[2] += 1
                return a
                    
        return actions[0]
                    