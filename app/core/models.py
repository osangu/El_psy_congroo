from datetime import datetime


class User:
    id: int
    email: str
    password: str


class Word:
    id: int
    alphabet: str
    mean: str


class Exam:
    id: int
    exam_at: datetime


class ExamWord:
    exam_id: int
    user_id: int
    word_id: int
    did_correct: bool
