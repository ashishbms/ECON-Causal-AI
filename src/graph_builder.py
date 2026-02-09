# src/graph_builder.py

from neo4j import GraphDatabase
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Neo4jGraph:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))
        logging.info("Graph database driver initialized.")

    def close(self):
        self._driver.close()
        logging.info("Graph database connection closed.")

    def populate_graph(self, nodes, edges):
        with self._driver.session() as session:
            # Clear the database before populating to avoid duplicates on re-runs
            session.execute_write(lambda tx: tx.run("MATCH (n) DETACH DELETE n"))
            logging.info("Cleared existing database content.")

            for node, attributes in nodes:
                session.execute_write(self._create_node, node, attributes)
            for source, target, attributes in edges:
                session.execute_write(self._create_relationship, source, target, attributes)
            logging.info(f"Graph populated with {len(nodes)} and {len(edges)} edges.")

    @staticmethod
    def _create_node(tx, name, attributes):
        query = (
            "MERGE (n:Concept {name: $name}) "
            "SET n += $props"
        )
        tx.run(query, name=name, props=attributes)

    @staticmethod
    def _create_relationship(tx, source_name, target_name, attributes):
        query = (
            "MATCH (a:Concept {name: $source_name}) "
            "MATCH (b:Concept {name: $target_name}) "
            "MERGE (a)-[r:INFLUENCES {label: $label}]->(b)"
        )
        tx.run(query, source_name=source_name, target_name=target_name, label=attributes.get('label'))