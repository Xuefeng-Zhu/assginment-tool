from random import randint

question_set = set([1, 2, 3])
people = {
    "Zhu": None,
    "Ye": None,
    "Liu": None
}


def helper(person):
    rnd = randint(1, 3)
    if rnd in question_set:
        people[person] = rnd
        question_set.remove(rnd)
    else:
        helper(person)

for person in people:
    helper(person)

print people
