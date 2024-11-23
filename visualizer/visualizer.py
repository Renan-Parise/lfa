import matplotlib.pyplot as plt
import networkx as nx

class AutomatonVisualizer:
    @staticmethod
    def visualize(states, transitions, start_state, accept_states, file_name="automaton_visual", highlight_edges=None):
        graph = nx.DiGraph()
        highlight_edges = highlight_edges or set()

        for state_id, state_name in states.items():
            shape = "doublecircle" if state_id in accept_states else "circle"
            graph.add_node(state_id, label=state_name, shape=shape)

        for (src, dest, symbol) in transitions:
            graph.add_edge(src, dest, label=symbol)

        pos = nx.spring_layout(graph)
        plt.figure(figsize=(12, 8))

        edge_colors = [
            "red" if (src, dest) in highlight_edges else "black"
            for (src, dest) in graph.edges
        ]

        nx.draw_networkx_nodes(
            graph,
            pos,
            node_color=["green" if state_id == start_state else "lightblue" for state_id in graph.nodes],
            node_size=2000,
            edgecolors="black",
        )

        nx.draw_networkx_edges(
            graph,
            pos,
            edge_color=edge_colors,
            connectionstyle="arc3,rad=0.2",
            arrowsize=20,
        )

        nx.draw_networkx_labels(graph, pos, labels=nx.get_node_attributes(graph, "label"), font_size=10)
        edge_labels = nx.get_edge_attributes(graph, "label")
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=8)

        plt.title("Visualização do Automato")
        plt.axis("off")
        plt.savefig(f"{file_name}.png", format="png")
        plt.close()
