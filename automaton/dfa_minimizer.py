class DFAMinimizer:
    @staticmethod
    def minimize(states, transitions, start_state, accept_states):
        groups = [accept_states, set(states.keys()) - accept_states]

        def find_group(state):
            for i, group in enumerate(groups):
                if state in group:
                    return i
            return -1

        changed = True
        while changed:
            new_groups = []
            for group in groups:
                subgroups = {}
                for state in group:
                    key = tuple(
                        (symbol, find_group(dest))
                        for (src, dest, symbol) in transitions if src == state
                    )
                    subgroups.setdefault(key, set()).add(state)
                new_groups.extend(subgroups.values())
            changed = new_groups != groups
            groups = new_groups

        state_map = {state: f"q{i}" for i, group in enumerate(groups) for state in group}
        minimized_states = {new_state: states[old_state] for old_state, new_state in state_map.items()}
        minimized_start_state = state_map[start_state]
        minimized_accept_states = {state_map[state] for state in accept_states if state in state_map}
        minimized_transitions = [
            (state_map[src], state_map[dest], symbol)
            for (src, dest, symbol) in transitions if src in state_map and dest in state_map
        ]

        return minimized_states, minimized_transitions, minimized_start_state, minimized_accept_states
