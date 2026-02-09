# scripts/setup_knowledge_graph.py

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.graph_builder import Neo4jGraph

def main():
    """Connects to Neo4j and populates the initial knowledge graph."""

    # Connection details for our Docker container
    URI = "neo4j://localhost:7687"
    USER = "neo4j"
    PASSWORD = "ECai@69420"

    # Connect to the database
    graph_db = Neo4jGraph(URI, USER, PASSWORD)

    # Define the components of our graph
    nodes = [
        ('Interest Rates', {'type': 'Policy Tool'}),
        ('Inflation', {'type': 'Indicator'}),
        ('GDP', {'type': 'Indicator'}),
        ('Consumer Spending', {'type': 'Behavior'})
    ]
    edges = [
        ('Interest Rates', 'Inflation', {'label': 'suppresses'}),
        ('Interest Rates', 'Consumer Spending', {'label': 'reduces'}),
        ('Consumer Spending', 'GDP', {'label': 'contributes to'}),
        ('Inflation', 'GDP', {'label': 'negatively affects'})
    ]

    # Populate the database
    graph_db.populate_graph(nodes, edges)

    # Close the connection
    graph_db.close()
    print("\n✅ Knowledge graph successfully populated in Neo4j database.")

if __name__ == "__main__":
    main()