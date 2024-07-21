import requests


class Vacansy:
    title: str
    link: str
    salary: int | float
    description: str
    requirement: str

    def __init__(self, title, link, description, requirement, salary=0):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description
        self.requirement = requirement
