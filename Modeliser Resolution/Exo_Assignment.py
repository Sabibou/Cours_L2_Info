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
def number_of_non_stable_couples(agencies_assign, candidates_assign,
                                 agencies_choices, candidates_choices):
    """Returns the number of non stable couples in the assignment."""
    n = len(agencies_assign)

    nonStable = 0

    for i in range(1, n+1):
        
        # We get both the agency and the candidate
        agency = f"A{i}"
        candidate = agencies_assign[agency]

        # Check if the agency choice is the first one, if yes, you can continue
        if agencies_choices[agency][0] == candidate:
            continue
    
        # We get the index of the agency in the candidate choices
        index = candidates_choices[candidate].index(agency)

        # We check if the agency is in the first index of the candidate choices
        if index == 0:
            continue

        

        
        

    return nonStable

n, agencies, candidates = extract_instance_from_file("./couple.txt")
print(number_of_non_stable_couples(agencies, candidates, agencies, candidates))

# ------------------------------------------------------------------------------
def generate_random_assignment(agencies_choices, candidates_choices):
    """Returns a random assignment as a 2 tuple of dictionaries."""
    pass


# ------------------------------------------------------------------------------
def gale_shapley_algorithm(agencies_choices, candidates_choices):
    """Run the Gale-Shapley algorithm and returns an assignment."""
    pass


# ------------------------------------------------------------------------------
def all_assignments(agencies_choices, candidates_choices):
    """Returns an iterator on all the possible (stable or not stable)
    assigments. Uses the itertools library. """
    import itertools  # You can use tools from this library
    pass  # Question plus difficile.
