import os
from automaton.parser import AutomatonParser
from automaton.dfa import DFA
from automaton.nfa import NFA
from automaton.tm import TuringMachine
from automaton.er import ER
from automaton.dfa_minimizer import DFAMinimizer
from visualizer.visualizer import AutomatonVisualizer

def test_automaton(automaton, test_file):
    if not os.path.exists(test_file):
        print(f"Erro: Arquivo de teste '{test_file}' não encontrado.")
        return {}

    with open(test_file, "r") as f:
        inputs = f.readlines()

    results = {}
    for input_str in inputs:
        input_str = input_str.strip()
        accepted, steps = automaton.process(input_str)
        results[input_str] = accepted

        print(f"\nInput: '{input_str}'")
        print("\n".join(steps))
        print("-" * 30)

    return results


if __name__ == "__main__":
    automaton_type = input("Selecione o tipo de autômato: (DFA/NFA/TM/ER): ").strip().lower()
    test_dir = f"tests/{automaton_type}"

    if not os.path.isdir(test_dir):
        print(f"Error: Diretório de teste '{test_dir}' não existe.")
        exit(1)

    jff_file = os.path.join(test_dir, "input.jff")
    txt_file = os.path.join(test_dir, "input.txt")

    try:
        if automaton_type == "dfa":
            states, transitions, start_state, accept_states = AutomatonParser.parse_jff(jff_file)
            automaton = DFA(states, transitions, start_state, accept_states)

            minimize = input("Você gostaria de minimizar o DFA? (y/n): ").strip().lower() == "y"
            if minimize:
                states, transitions, start_state, accept_states = DFAMinimizer.minimize(
                    states, transitions, start_state, accept_states
                )
                print("DFA minimizado!")

        elif automaton_type == "nfa":
            if not os.path.exists(jff_file):
                print(f"Erro: arquivo NFA JFF '{jff_file}' não encontrado.")
                exit(1)

            states, transitions, start_state, accept_states = AutomatonParser.parse_jff(jff_file)
            automaton = NFA(states, transitions, start_state, accept_states)

        elif automaton_type == "tm":
            if not os.path.exists(jff_file):
                print(f"Erro: arquivo TM JFF '{jff_file}' não encontrado.")
                exit(1)

            states, transitions, start_state, accept_states = AutomatonParser.parse_jff(jff_file)
            automaton = TuringMachine(states, transitions, start_state, accept_states)

        elif automaton_type == "er":
            if not os.path.exists(txt_file):
                print(f"Erro: arquivo ER JFF '{jff_file}' não encontrado.")
                exit(1)

            regex = input("Insira a expressão regular: ").strip()
            automaton = ER(regex)

        else:
            print("Erro: Autômato selecionado inválido.")
            exit(1)

        if automaton_type != "er":
            AutomatonVisualizer.visualize(states, transitions, start_state, accept_states, file_name=f"automaton_{automaton_type}")

        results = test_automaton(automaton, txt_file)
        for input_str, result in results.items():
            print(f"Input '{input_str}': {'Aceito' if result else 'Rejeitado'}")

    except Exception as e:
        print(f"Erro: {e}")
