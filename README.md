# Genre model as RDF: moves and steps of MMR discussion sections

A small Python project that represents a published genre-analysis model
as Linked Open Data (RDF), using [rdflib](https://rdflib.readthedocs.io/).

## What it models

The five-move model of the discussion section in mixed methods research (MMR)
articles in applied linguistics, from:

> Hashemi, M. R., & Gohari Moghaddam, I. (2019). A mixed methods genre analysis
> of the discussion section of MMR articles in applied linguistics.
> *Journal of Mixed Methods Research*, 13(2), 242-260.
> https://doi.org/10.1177/1558689816674626

The graph contains:

- the article, described with Dublin Core terms (title, creators, year, journal)
- one `GenreModel` linked to the article as its source
- five `Move` resources (Study, Results, Discussion, Evaluation, Suggestions),
  each with a position, a frequency (number of articles out of 38) and a status
  (obligatory / highly recommended / recommended)
- nineteen `Step` resources, each linked to its move, with a position and a
  frequency

Moves, steps and frequencies come from Figure 1 and Tables 2 and 3 of the
article and are stored in `moves_data.py`, separately from the code that builds
the graph.

## Run it

```bash
pip install rdflib
python rdf_moves.py
```

This writes `genre_model.ttl` (Turtle) and prints two SPARQL query results:
all moves and steps in order, and the steps that occur in at least 30 of the
38 articles.

## Files

| File | Purpose |
|------|---------|
| `moves_data.py` | The model as plain Python data (moves, steps, frequencies) |
| `rdf_moves.py` | Builds the RDF graph, saves it, runs SPARQL queries |
| `genre_model.ttl` | Output, created when you run the script |

## Notes

- The vocabulary under `https://example.org/mmr-discussion/` is a placeholder
  namespace for this exercise, not a published ontology.
- No personal data is used. The only inputs are bibliographic information and
  the published model.
- Possible next steps: link moves to an existing vocabulary, add the coded
  excerpts from the study as annotated text, and express the same model in
  TEI.
