import pandas as pd

participants = pd.DataFrame(
    {
        "participant_id": ["sub-01", "sub-02"],
        "age": [20, 30],
        "sex": ["m", "f"],
    }
)
participants.to_csv("participants.tsv")
