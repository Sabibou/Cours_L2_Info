import random


"""Data structure of a formula F.
   -----------------------------
    A variable is a string (with no ',', no '&', no ' ' and no '-')
    A positive literal is a variable. 
    A negative literal is a variable with an additional '-' as first character.
    A clause is a list of literals.
    A formula is a list of clauses.
    
    The dictionary of a formula is the dictionary whose keys are the variables
    of the formula. 

   Boolean values of variables, literals, clauses, formulas.
   ---------------------------------------------------------
    An assignment for a formula is a Boolean value for each variable of the 
    dictionary of the formula. 
    Given a formula F and an assignment A:
        The boolean value of a positive literal with variable x is the Boolean
            value of A[x].
        The boolean value of a negative literal with variable x (-x) is the 
            Boolean value of not(A[x]).
        The boolean value of a clause is the logical OR Boolean value 
            of its literals. A clause is 'satisfied' if its value is True.
        The boolean value of a formula is the logical AND Boolean value 
            of its clauses. A formula is 'satisfied' if its value is True.
    
    Illustration.
    ------------
    F = [['a', '-b', 'c'], ['-a', 'b', '-d'], ['a', 'b', 'c'], ['-b', 'd', '-e']]
    The dictionary of F has keys 'a', 'b', 'c', 'd', 'e'
    An example of an assignment:
    {'a':False, 'b':True, 'c':True, 'd':False, 'e':False}
"""


def get_formula_from_file(file):
    """Extract a formula from file and returns it as a list.
    In file:
        A variable is a string (with no ',', no '&', no ' ' and no '-').
        A literal is either:
            a variable (positive literal) or a variable beginning with
            '-' (negative literal).
        Literals in clauses are separated by ','.
        Clauses are separated by '&'.
        Formula is on one line in the file.
    Example of formula: a,-b,cloclo&b,-a,-c&d,-a,-b&-cloclo,-name,-a,-b
    """
    formula = []

    with open(file, "r") as fileIn:
        line = fileIn.readline().strip()

        clauses = line.split("&")

        for clause in clauses:
            literals = clause.split(",")
            formula.append(literals)

    return formula

# for clause in get_formula_from_file("formula.txt"):
#     print(clause)


def variable_of_literal(literal):
    """Returns the name of the variable of the literal."""
    return literal.replace("-", "")


def sign_of_literal(literal):
    """Returns the sign of the literal: '-' for a negative literal and
    '+' otherwise."""
    return "+" if not literal[0] == '-' else "-"


def set_of_variables_from_formula(f):
    """Returns the set of the names of variables appearing in the formula."""
    fSet = set()

    for clauses in f:
        for litteral in clauses:
            fSet.add(variable_of_literal(litteral))
    return fSet

# print(set_of_variables_from_formula(get_formula_from_file("formula.txt")))


def construct_dictionary_from_vars(set_of_vars):
    """Constructs a dictionary from the set of variables.
    The value of each entry is None (no assignment)."""
    return {key: None for key in set_of_vars}


# print(construct_dictionary_from_vars(set_of_variables_from_formula(get_formula_from_file("formula.txt"))))


def random_assignment(d):
    """Takes a dictionary as input and puts a random Boolean value to each
    variable. """
    return {key: True if random.randint(0, 1) == 1 else False for key in d}


# print(random_assignment(construct_dictionary_from_vars(
#     set_of_variables_from_formula(get_formula_from_file("formula.txt")))))


def boolean_value_of_literal(assignment, literal):
    """Given an assignment and a literal, returns the Boolean value of the
       literal."""
    return assignment if sign_of_literal(literal) == "+" else not (assignment)


def boolean_value_of_clause(assignment, clause):
    """Given an assignment and a clause, returns the Boolean value of the
       clause."""
    return any([boolean_value_of_literal(assignment[variable_of_literal(literal)], literal) for literal in clause])


# assignment = random_assignment(construct_dictionary_from_vars({"a", "b", "c"}))
# assignment = {"a": False, "b": False, "c": True}
# print(assignment)
# print(boolean_value_of_literal(assignment["a"], "a"))
# print(boolean_value_of_clause(assignment, ["a", "b", "c"]))
# print(boolean_value_of_clause(True, ["a", "-b", "c"]))

def boolean_value_of_formula(assignment, formula):
    """Given an assignment and a formula, returns the Boolean value of the
       formula."""
    return all([boolean_value_of_clause(assignment, clause) for clause in formula])


def number_of_true_clauses(assignment, formula):
    """Given an assignment and a formula, returns the number of clauses having
       a Boolean value True."""
    return sum([boolean_value_of_clause(assignment, clause) for clause in formula])


def number_of_clauses(formula):
    """Returns the number of clauses of the formula."""
    return len(formula)


def pretty_print_formula(formula):
    """Print a nice/readable view of the formula."""
    for clause in formula:
        print(" or ".join(clause))


# formula = get_formula_from_file("formula.txt")
# pretty_print_formula(formula)


def pretty_print_assigned_formula(assignment, formula):
    """Print a nice/readable view of the formula with each variable replaced
       by its Boolean value; also print the value of each clause. Illustration
       True       not(False) True        = True
       not(True)  False      not(True)   = False
       True       False      True        = True"""
    for clause in formula:
        for literal in clause:
            literalName = variable_of_literal(literal)

            if sign_of_literal(literal) == "+":
                print(assignment[literalName], end="\t")
            else:
                print(not assignment[literalName], end="\t")

        print(" = ", end="\t")

        print(boolean_value_of_clause(assignment, clause))


# formula = get_formula_from_file("formula.txt")
# assignment = random_assignment(construct_dictionary_from_vars(
#     set_of_variables_from_formula(formula)))
# pretty_print_assigned_formula(assignment, formula)


def random_formula(n=26, c=10, min_len=1, max_len=10, file="FX"):
    """Generate a random formula with at most n variables, exactly c clauses,
       each with at least min_len literals and at most max_len literals.
    Put the final formula in file.
    Each variable must be a non capital letter (a, b, c,...,z). """

    # First we create a list of vars (random 3 long strings)
    vars = []

    for _ in range(n):
        newVar = ""

        while newVar in vars or len(newVar) != 3:
            newVar = ""

            for j in range(3):
                newVar += chr(random.randint(97, 122))

        vars.append(newVar)

    formula = []

    for _ in range(c):

        # We get a number between min_len and max_lend
        n = random.randint(min_len, max_len)

        formulaVars = random.sample(vars, n)

        signedVars = [random.choice(["", "-"]) + var for var in formulaVars]

        formula.append(signedVars)

    with open("formula2.txt", "w") as file:

        for i in range(len(formula)):
            clause = formula[i]

            file.write(",".join(clause))

            if i < len(formula) - 1:
                file.write("&")


# random_formula()


def iter_all_assignments(d):
    """An iterator to generate all the possible assignments of a dictionary d.
    NB: the call returns an iterator of assignments, not the assignments."""
    keys = list(d.keys())
    n = len(keys)

    def binIter():
        for i in range(2**n):
            l = []
            for j in range(n):
                l.append((i >> j) % 2)
            yield l

    for it in binIter():
        yield {keys[i]: bool(it[i]) for i in range(n)}


# for assign in iter_all_assignments({"a": None, "b": None, "c": None}):
#     print(assign)


def evaluate_all_assignments(formula):
    """Returns, for each possible assignment of the variables of the formula,
    the list of the number of satisfied clauses (with Boolean value True)."""

    evaluations = []

    for assignment in iter_all_assignments(construct_dictionary_from_vars(
            set_of_variables_from_formula(formula))):
        evaluations.append(number_of_true_clauses(assignment, formula))

    return evaluations

print(evaluate_all_assignments(get_formula_from_file("formula.txt")))

"""
Example of pretty print of formula a,-b,c&-a,b,-d&a,b,c&-b,d,-e&a,-c,e :
 a or -b or  c
-a or  b or -d
 a or  b or  c
-b or  d or -e
 a or -c or  e

Example of a pretty print of an assignment for this formula:

False      not(False) False       = True
not(False) False      not(False)  = True
False      False      False       = False
not(False) False      not(True)   = True
False      not(False) True        = True """
