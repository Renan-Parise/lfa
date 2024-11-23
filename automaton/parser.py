from lxml import etree

class AutomatonParser:
    @staticmethod
    def parse_jff(file_path):
        try:
            tree = etree.parse(file_path)
        except Exception as e:
            raise ValueError(f"Failed to parse JFF file: {e}")

        root = tree.getroot()

        states = {}
        transitions = []
        start_state = None
        accept_states = set()

        for state in root.findall(".//state"):
            state_id = state.get("id")
            state_name = state.get("name")
            states[state_id] = state_name
            if state.find("initial") is not None:
                start_state = state_id
            if state.find("final") is not None:
                accept_states.add(state_id)

        for transition in root.findall(".//transition"):
            src = transition.find("from").text
            dest = transition.find("to").text
            symbol = transition.find("read").text or ""

            if root.find(".//type").text.strip() == "turing":
                write_symbol = transition.find("write").text or ""
                direction = transition.find("move").text or ""
                transitions.append((src, dest, symbol, write_symbol, direction))
            else:
                transitions.append((src, dest, symbol))

        return states, transitions, start_state, accept_states
