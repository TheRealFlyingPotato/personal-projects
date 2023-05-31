from abc import ABC, abstractmethod

class Ability(ABC):
    def __init__(self, obj):
        self.obj = obj

    @abstractmethod
    def apply(self, game_state):
        pass

    @abstractmethod
    def check_timing(self, timing):
        pass

class IncreaseForAdjacentStrikes(Ability):
    def apply(self, game_state):
        if game_state.state == 'on_draw':
            for card in game_state.card_handler.hand:
                if card == self.obj:
                    print(card.id)
    
    def check_timing(self, timing):
        return timing in ['on_draw','on_damage']

class Card:
    def __init__(self, name='unknown', desc=None, id=None, abilities=None):
        self.id=id
        self.name=name
        if abilities != None:
            self.abilities = [ability(self) for ability in abilities]
            #for ability in self.abilities:
            #    print(ability.obj.id)
        else:
            self.abilities = []
        self.desc=desc

    def apply_abilities(self, game_state):
        for ability_name, ability in self.abilities.items():
            ability.apply(game_state)

    def __str__(self):
        return f'{self.name}: {self.desc}'

class CardHandler:
    def __init__(self, game_state):
        self.hand_size = 5
        self.deck = [
                Card(id=0, name="Mirror Strike", desc="Deal 5 Damage", abilities=[IncreaseForAdjacentStrikes]),
                Card(id=1, name="Mirror Strike", desc="Deal 5 Damage. Deals +1 damage per strike adjacent.", abilities=[IncreaseForAdjacentStrikes]),
                Card(id=2, name="Strike", desc="Deal 5 Damage"),
                Card(id=3, name="Strike", desc="Deal 5 Damage"),
                Card(id=4, name="Mirror Strike", desc="Deal 5 Damage. Deals +1 damage per strike adjacent.",abilities=[IncreaseForAdjacentStrikes]),
                Card(id=5, name="Defend", desc="Block 6 Damage"),
                Card(id=6, name="Mirror Strike", desc="Deal 5 Damage",abilities=[IncreaseForAdjacentStrikes]),
                Card(id=7, name="Strike", desc="Deal 5 Damage"),
                Card(id=8, name="Strike", desc="Deal 5 Damage"),
                Card(id=9, name="Mirror Strike", desc="Deal 5 Damage",abilities=[IncreaseForAdjacentStrikes])
            ]
        #self.deck = [Card(id=x, name=f'card {x}') for x in range(10)]
        self.hand = list()
        self.discard = list()
        self.game_state = game_state

    def get_deck(self):
        return self.deck

    def str_hand(self):
        return '\n'.join([f'{i}. {self.hand[i]}' for i in range(len(self.hand))])
        
    def draw_card(self):
        self.hand.append(self.deck.pop(0))
        for ability in self.hand[-1].abilities:
            if ability.check_timing('on_draw'):
                self.game_state.add_ability(ability)

    def draw_hand(self):
        while len(self.hand) < self.hand_size:
            self.draw_card()
        self.game_state.state = "on_draw"

class GameStateHandler:
    def __init__(self):
        self.ability_stack = []
        self.card_handler = CardHandler(self)
        self.game_state = None

    def add_ability(self, ability):
        self.ability_stack.append(ability)

    def main_loop(self):
        self.card_handler.draw_hand()
        while self.ability_stack != []:
            #breakpoint()
            self.ability_stack.pop(0).apply(self)

def main():
    GAME_STATE = GameStateHandler()
    #GAME_STATE.card_handler.draw_hand()
    GAME_STATE.main_loop()
    #CARD_HANDLER = CardHandler()
    #CARD_HANDLER.draw_hand()
    #print(CARD_HANDLER.str_hand())

main()
