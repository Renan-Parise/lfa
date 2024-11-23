from .base import Automaton

class NFA(Automaton):
    def process(self, input_string):
        steps = []

        stack = [(self.start_state, 0)]

        while stack:
            current_state, idx = stack.pop()
            if idx == len(input_string):
                steps.append(f"At end of input: State: {current_state}")
                if current_state in self.accept_states:
                    steps.append(f"Final Result: Accepted")
                    return True, steps

            if idx < len(input_string):
                char = input_string[idx]
                steps.append(f"Current state: {current_state}, char: '{char}'")

                for (src, dest, symbol) in self.transitions:
                    if src == current_state and (symbol == char or symbol == ""):
                        steps.append(f"Transition: {src} --({symbol})--> {dest}")
                        stack.append((dest, idx + (symbol != "")))

        steps.append(f"Resultado final: Rejeitado")
        return False, steps
