"""
Model a genre analysis (moves and steps) as RDF with rdflib.

Reads the five-move model of MMR discussion sections from moves_data.py,
builds an RDF graph, saves it as Turtle, and runs two SPARQL queries.

Usage:
    pip install rdflib
    python rdf_moves.py
"""

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, RDF, RDFS, XSD

from moves_data import ARTICLE, CORPUS_SIZE, MOVES

EX = Namespace("https://example.org/mmr-discussion/")


def build_graph() -> Graph:
    g = Graph()
    g.bind("ex", EX)
    g.bind("dcterms", DCTERMS)
    g.bind("rdfs", RDFS)

    # --- The article ---------------------------------------------------
    article = URIRef(f"https://doi.org/{ARTICLE['doi']}")
    g.add((article, RDF.type, EX.JournalArticle))
    g.add((article, DCTERMS.title, Literal(ARTICLE["title"], lang="en")))
    g.add((article, DCTERMS.issued, Literal(str(ARTICLE["year"]), datatype=XSD.gYear)))
    g.add((article, DCTERMS.isPartOf, Literal(ARTICLE["journal"])))
    for creator in ARTICLE["creators"]:
        g.add((article, DCTERMS.creator, Literal(creator)))

    # --- The model: one GenreModel with ordered moves and steps ---------
    model = EX.DiscussionModel
    g.add((model, RDF.type, EX.GenreModel))
    g.add((model, RDFS.label, Literal("Five-move model of MMR discussion sections", lang="en")))
    g.add((model, DCTERMS.source, article))
    g.add((model, EX.corpusSize, Literal(CORPUS_SIZE, datatype=XSD.integer)))

    for i, move_data in enumerate(MOVES, start=1):
        move = EX[f"Move{i}"]
        g.add((move, RDF.type, EX.Move))
        g.add((move, RDFS.label, Literal(move_data["label"], lang="en")))
        g.add((move, EX.position, Literal(i, datatype=XSD.integer)))
        g.add((move, EX.frequency, Literal(move_data["frequency"], datatype=XSD.integer)))
        g.add((move, EX.status, Literal(move_data["status"], lang="en")))
        g.add((model, EX.hasMove, move))

        for j, (step_label, step_freq) in enumerate(move_data["steps"], start=1):
            step = EX[f"Move{i}_Step{j}"]
            g.add((step, RDF.type, EX.Step))
            g.add((step, RDFS.label, Literal(step_label, lang="en")))
            g.add((step, EX.position, Literal(j, datatype=XSD.integer)))
            g.add((step, EX.frequency, Literal(step_freq, datatype=XSD.integer)))
            g.add((move, EX.hasStep, step))

    return g


QUERY_ALL_STEPS = """
PREFIX ex:   <https://example.org/mmr-discussion/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?move ?step ?freq WHERE {
    ?m a ex:Move ;
       rdfs:label ?move ;
       ex:position ?mp ;
       ex:hasStep ?s .
    ?s rdfs:label ?step ;
       ex:position ?sp ;
       ex:frequency ?freq .
}
ORDER BY ?mp ?sp
"""

QUERY_FREQUENT_STEPS = """
PREFIX ex:   <https://example.org/mmr-discussion/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?move ?step ?freq WHERE {
    ?m rdfs:label ?move ; ex:hasStep ?s .
    ?s rdfs:label ?step ; ex:frequency ?freq .
    FILTER (?freq >= 30)
}
ORDER BY DESC(?freq)
"""


def main() -> None:
    g = build_graph()
    g.serialize(destination="genre_model.ttl", format="turtle")
    print(f"Saved {len(g)} triples to genre_model.ttl\n")

    print("All moves and steps (frequency = number of articles out of "
          f"{CORPUS_SIZE}):")
    for row in g.query(QUERY_ALL_STEPS):
        print(f"  {row.move}  ->  {row.step}  ({row.freq})")

    print("\nSteps that occur in at least 30 of the articles:")
    for row in g.query(QUERY_FREQUENT_STEPS):
        print(f"  {row.step}  [{row.move}]  ({row.freq})")


if __name__ == "__main__":
    main()
