class Automaton:
    def __init__(self, states, transitions, start_state, accept_states):
        self.states = states
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def process(self, input_string):
        raise NotImplementedError("Subclasses devem implementar este método")
