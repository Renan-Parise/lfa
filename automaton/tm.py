from .base import Automaton

class TuringMachine(Automaton):
    def __init__(self, states, transitions, start_state, accept_states):
        super().__init__(states, transitions, start_state, accept_states)
        self.blank_symbol = " "
        self.tape = []
        self.head_position = 0

    def process(self, input_string):
        self.tape = list(input_string) + [self.blank_symbol]
        self.head_position = 0 
        current_state = self.start_state
        steps = [f"Inicial: {''.join(self.tape)}"]

        while True:
            read_symbol = self.tape[self.head_position]
            transition_found = False

            for (src, dest, symbol, write_symbol, direction) in self.transitions:
                if src == current_state and symbol == read_symbol:
                    self.tape[self.head_position] = write_symbol
                    self.head_position += 1 if direction == "R" else -1
                    current_state = dest
                    transition_found = True
                    break

            if not transition_found:
                break

        accepted = current_state in self.accept_states
        steps.append(f"Estado final: {current_state} ({'Aceito' if accepted else 'Rejeitado'})")
        return accepted, steps
