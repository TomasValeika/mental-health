sql_all_data = """
SELECT 
    a.UserID
    , a.SurveyID AS 'Year'
    , a.QuestionID 
    , q.questiontext 
    , a.AnswerText 

FROM Answer AS a 
    LEFT JOIN Question AS q 
    ON a.questionid = q.questionid;
"""
