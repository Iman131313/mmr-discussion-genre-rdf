"""
Five-move model of the discussion section of mixed methods research (MMR)
articles in applied linguistics.

Source: Hashemi, M. R., & Gohari Moghaddam, I. (2019). A mixed methods genre
analysis of the discussion section of MMR articles in applied linguistics.
Journal of Mixed Methods Research, 13(2), 242-260.
https://doi.org/10.1177/1558689816674626

Moves, steps and frequencies follow Figure 1 and Tables 2 and 3 of the article.
Frequencies are the number of articles (out of 38) in which a move or step
occurred.
"""

CORPUS_SIZE = 38  # number of MMR articles analysed

ARTICLE = {
    "doi": "10.1177/1558689816674626",
    "title": (
        "A Mixed Methods Genre Analysis of the Discussion Section "
        "of MMR Articles in Applied Linguistics"
    ),
    "journal": "Journal of Mixed Methods Research",
    "year": 2019,
    "creators": ["Hashemi, M. R.", "Gohari Moghaddam, I."],
}

MOVES = [
    {
        "label": "Study",
        "frequency": 35,
        "status": "Highly recommended",
        "steps": [
            ("Objectives", 15),
            ("Method", 26),
            ("Significance/novelty/reference to previous research", 19),
            ("Research questions", 3),
        ],
    },
    {
        "label": "Results",
        "frequency": 38,
        "status": "Obligatory",
        "steps": [
            ("Summary of findings", 38),
            ("Visual presentation of findings", 14),
            ("Observation/report", 38),
            ("Examples/extracts", 7),
        ],
    },
    {
        "label": "Discussion",
        "frequency": 38,
        "status": "Obligatory",
        "steps": [
            ("Judgments", 26),
            ("Explanations", 26),
            ("Meta-inferences", 10),
            ("Explaining meta-inferences", 13),
            ("Comparison with the existing literature", 37),
        ],
    },
    {
        "label": "Evaluation",
        "frequency": 16,
        "status": "Recommended",
        "steps": [
            ("Limitations", 13),
            ("Delimitations", 2),
            ("Generalizability", 3),
        ],
    },
    {
        "label": "Suggestions",
        "frequency": 35,
        "status": "Highly recommended",
        "steps": [
            ("Solutions to the present problem", 15),
            ("Implications and applications", 23),
            ("Suggestions for further research", 10),
        ],
    },
]
