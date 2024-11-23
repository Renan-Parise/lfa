import re

class ER:
    def __init__(self, regex):
        self.regex = regex

    def process(self, input_string):
        steps = [f"Regex: {self.regex}", f"Input: {input_string}"]
        matched = bool(re.fullmatch(self.regex, input_string))
        steps.append(f"Resultado: {'Correspondido' if matched else 'Não correspondido'}")
        return matched, steps
