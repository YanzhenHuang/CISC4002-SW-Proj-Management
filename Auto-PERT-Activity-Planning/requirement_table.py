requirement = {
    "A": {
        "DUR": 2,
        "PREV": [],
    },
    "B": {
        "DUR": 10,
        "PREV": ["A"]
    },
    "C": {
        "DUR": 2,
        "PREV": ["A"]
    },
    "D": {
        "DUR": 2,
        "PREV": ["C"]
    },
    "E": {
        "DUR": 3,
        "PREV": ["C"]
    },
    "F": {
        "DUR": 2,
        "PREV": ["C"]
    },
    "G": {
        "DUR": 4,
        "PREV": ["B", "D", "E", "F"]
    }
}
