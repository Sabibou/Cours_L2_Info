import random

"""Each agency has a name (a string) and each candidate has a name (a string).
The number of agencies must be the equal to the number of candidates. 
An instance is:
    + A dictionary containing the choices of the agencies: 
    its keys are the names of agencies and the value of each key/agency 
    is the list of choices of this agency. 
    + A dictionary containing the choices of the candidates: 
    its keys are the names of candidates and the value of each key/candidate 
    is the list of choices of this candidate.
Each list must be a permutation of the n elements of the choices.

An assignment is:
    One candidate C associated to each agency A (C->A) and 
    one agency A to each candidate C (A->C).
    This must be symmetric: A->C if and only if C->A.
An assignment is represented by two dictionaries (one for candidates and the
other for agencies). Each element (candidate or agency) is a key and its
assigned element is the corresponding value. 
"""

# ------------------------------------------------------------------------------


def extract_instance_from_file(file):
    """Get the instance in the file. Returns a 3-tuple where the first element
    is n (the number of agencies and candidates), the second element is the
    dictionary containing the choices of the n agencies, the last element is the
    dictionary containing the choices of the n candidates.
    The format of a file is:
    n (alone on the first line)
    followed by n lists for agencies followed by n lists for candidates.
    Each line is X:Y1:Y2:...:Yn where X is agency or candidate and the Yi's are
    the choices of X. The separator is ':' with no space between elements."""
    with open(file, "r") as buffer:
        n = int(buffer.readline())

        agencies = {}
        candidates = {}

        for _ in range(n):
            line = buffer.readline().strip().split(":")

            key = line[0]

            agencies[key] = line[1:]

        for _ in range(n):
            line = buffer.readline().strip().split(":")

            key = line[0]

            candidates[key] = line[1:]

        return n, agencies, candidates

# print(extract_instance_from_file("./couple.txt"))


# ------------------------------------------------------------------------------
def generate_random_instance(n, version_number=1):
    """Generate a random instance with n agencies, n candidates and put the
    result in a file that is named GSEntries_Rand_{n}_{version_number}
    (for example GSEntries_Rand_10_3) to distinguish different random files."""

    indexes = [str(i) for i in range(1, n+1)]
    agencies = {
        f"A{i}": ["C"+el for el in random.sample(indexes, n)] for i in range(1, n+1)}
    candidates = {
        f"C{i}": ["A"+el for el in random.sample(indexes, n)] for i in range(1, n+1)}

    with open(f"GSEntries_Rand_{n}_{version_number}", "w") as file:
        file.write(f"{n}\n")

        for agency in agencies:
            file.write(f"{agency}:{':'.join(agencies[agency])}\n")

        for candidate in candidates:
            file.write(f"{candidate}:{':'.join(candidates[candidate])}\n")

# generate_random_instance(5, 1)


# ------------------------------------------------------------------------------
def generate_random_assignment(agencies_choices, candidates_choices):
    """Returns a random assignment as a 2 tuple of dictionaries."""

    agenciesAssign = {agency: random.choice(
        agencies_choices[agency]) for agency in agencies_choices}

    candidatesAssign = {candidate: random.choice(
        candidates_choices[candidate]) for candidate in candidates_choices}

    return agenciesAssign, candidatesAssign

# ------------------------------------------------------------------------------


def generate_straight_assignment(agencies_choices, candidates_choices):
    """Returns a straight assignment as a 2 tuple of dictionaries."""
    agencies = list(agencies_choices.keys())
    candidates = list(candidates_choices.keys())

    agenciesAssign = {agency: candidates[i]
                      for i, agency in enumerate(agencies)}
    candidatesAssign = {candidate: agencies[i]
                        for i, candidate in enumerate(candidates)}

    return agenciesAssign, candidatesAssign


def number_of_non_stable_couples(agencies_assign, candidates_assign,
                                 agencies_choices, candidates_choices):
    """Returns the number of non stable couples in the assignment."""
    # A non stable couple is as situation where there are two couples : (A,B) and (C,D), and where A prefers C to B and C prefers A to D.
    number = 0

    for agencyName in agencies_assign:

        agencyAssignement = agencies_assign[agencyName]
        agencyAssignementIndex = agencies_choices[agencyName].index(
            agencyAssignement)

        if agencyAssignementIndex == 0:
            continue

        selectedCandidate = agencies_assign[agencyName]

        for i in range(agencyAssignementIndex):
            candidate = agencies_choices[agencyName][i]

            candidateAgency = candidates_assign[candidate]
            candidateAgencyIndex = candidates_choices[candidate].index(
                candidateAgency)

            candidateAgencyRank = candidates_choices[candidate].index(
                agencyName)

            if candidateAgencyRank < candidateAgencyIndex:
                print(
                    f"Agency {agencyName} prefers {candidate} to {selectedCandidate} and {candidate} prefers {agencyName} to {candidateAgency}.")
                number += 1

    return number


n, agencies, candidates = extract_instance_from_file("./couple.txt")
# agenciesAssign, candidatesAssign = generate_random_assignment(
#     agencies, candidates)
agenciesAssign, candidatesAssign = generate_straight_assignment(
    agencies, candidates)

print(number_of_non_stable_couples(agenciesAssign,
      candidatesAssign, agencies, candidates))


# ------------------------------------------------------------------------------
def gale_shapley_algorithm(Oagencies_choices, Ocandidates_choices):
    """Run the Gale-Shapley algorithm and returns an assignment."""
    # While not all agencies are assigned
    agencies_choices = dict(Oagencies_choices)
    candidates_choices = dict(Ocandidates_choices)

    agenciesAssign = {}
    candidatesAssign = {}
    n = len(agencies_choices)
    while not len(agenciesAssign) == n:
        for agency in agencies_choices:
            if agency in agenciesAssign:
                continue

            candidate = agencies_choices[agency][0]

            if candidate not in candidatesAssign:
                agenciesAssign[agency] = candidate
                candidatesAssign[candidate] = agency
            else:
                candidateAgency = candidatesAssign[candidate]

                candidateAgencyRank = candidates_choices[candidate].index(
                    agency)
                candidateAgencyIndex = candidates_choices[candidate].index(
                    candidateAgency)

                if candidateAgencyRank < candidateAgencyIndex:
                    agenciesAssign[agency] = candidate
                    candidatesAssign[candidate] = agency

                    del agenciesAssign[candidateAgency]
                else:
                    agencies_choices[agency].remove(candidate)

    return agenciesAssign, candidatesAssign


def gale_shapley_algorithm2(agencies_choices, candidates_choices):
    """Run the Gale-Shapley algorithm and returns an assignment."""
    # While not all agencies are assigned
    agenciesAssign = {}
    candidatesAssign = {}

    agenciesIndexes = {agency:0 for agency in agencies_choices}

    n = len(agencies_choices)
    while not len(agenciesAssign) == n:
        for agency in agencies_choices:
            if agency in agenciesAssign:
                continue

            candidate = agencies_choices[agency][agenciesIndexes[agency]]

            if candidate not in candidatesAssign:
                agenciesAssign[agency] = candidate
                candidatesAssign[candidate] = agency
            else:
                candidateAgency = candidatesAssign[candidate]

                candidateAgencyRank = candidates_choices[candidate].index(
                    agency)
                candidateAgencyIndex = candidates_choices[candidate].index(
                    candidateAgency)

                if candidateAgencyRank < candidateAgencyIndex:
                    agenciesAssign[agency] = candidate
                    candidatesAssign[candidate] = agency

                    del agenciesAssign[candidateAgency]
                else:
                    agenciesIndexes[agency]+=1

    return agenciesAssign, candidatesAssign

agenciesAssign, candidatesAssign = gale_shapley_algorithm2(agencies, candidates)

for agency in agenciesAssign:
    print(f"{agency} -> {agenciesAssign[agency]}")

# After the algorithm, we can check if the result is stable or not
print("\n---------------------\n")
print(number_of_non_stable_couples(agenciesAssign,
      candidatesAssign, agencies, candidates))

# ------------------------------------------------------------------------------


def all_assignments(agencies_choices, candidates_choices):
    """Returns an iterator on all the possible (stable or not stable)
    assigments. Uses the itertools library. """
    import itertools  # You can use tools from this library

    agencies = list(agencies_choices.keys())
    candidates = list(candidates_choices.keys())
    n = len(agencies)

    def h(i):
        if i == n:
            yield resultat
        else:
            for j in range(n):
                if j not in resultat.values():
                    resultat[agencies[i]] = candidates[j]
                    yield from h(i+1)

    resultat = {agency: 0 for agency in agencies}
    yield from h(0)

# for assignment in all_assignments(agencies, candidates):
#     print(assignment)
