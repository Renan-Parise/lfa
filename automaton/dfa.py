from .base import Automaton

class DFA(Automaton):
    def process(self, input_string):
        current_state = self.start_state
        steps = []

        for char in input_string:
            found = False
            for (src, dest, symbol) in self.transitions:
                if src == current_state and symbol == char:
                    steps.append(f"{current_state} --({char})--> {dest}")
                    current_state = dest
                    found = True
                    break
            if not found:
                steps.append(f"{current_state} --({char})--> ERRO (Sem transição)")
                return False, steps

        accepted = current_state in self.accept_states
        steps.append(f"Estado final: {current_state} ({'Aceito' if accepted else 'Rejeitado'})")
        return accepted, steps
