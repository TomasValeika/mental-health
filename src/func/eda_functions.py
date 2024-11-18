import pandas as pd


def question_df(df: pd.DataFrame, question_no: int, col_name: str):
    """Return filtered DF"""

    return df.loc[df["QuestionID"] == question_no].rename(
        columns={"AnswerText": col_name}
    )


def age_bucket(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates column with age groups
    """
    if (df["Age"] >= 18) & (df["Age"] <= 24):
        return "18-24"
    elif (df["Age"] >= 25) & (df["Age"] <= 34):
        return "25-34"
    elif (df["Age"] >= 35) & (df["Age"] <= 44):
        return "35-44"
    elif (df["Age"] >= 45) & (df["Age"] <= 54):
        return "45-54"
    else:
        return "55-67"
