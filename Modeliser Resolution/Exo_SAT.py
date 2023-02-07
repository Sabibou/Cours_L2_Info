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
    with open(file, "r") as fileIn:
        line = fileIn.readline().strip()

        clauses = line.split(",")

        for clause in clauses:
            yield clause.split("&")

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
        for clause in clauses:
            fSet.add(variable_of_literal(clause))
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


def boolean_value_of_formula(assignment, formula):
    """Given an assignment and a formula, returns the Boolean value of the
       formula."""
    pass


def number_of_true_clauses(assignment, formula):
    """Given an assignment and a formula, returns the number of clauses having
       a Boolean value True."""
    pass


def number_of_clauses(formula):
    """Returns the number of clauses of the formula."""
    pass


def pretty_print_formula(formula):
    """Print a nice/readable view of the formula."""
    pass


def pretty_print_assigned_formula(assignment, formula):
    """Print a nice/readable view of the formula with each variable replaced
       by its Boolean value; also print the value of each clause. Illustration
       True       not(False) True        = True
       not(True)  False      not(True)   = False
       True       False      True        = True"""
    pass


def random_formula(n=26, c=10, min_len=1, max_len=10, file="FX"):
    """Generate a random formula with at most n variables, exactly c clauses,
       each with at least min_len literals and at most max_len literals.
    Put the final formula in file.
    Each variable must be a non capital letter (a, b, c,...,z). """
    pass


def iter_all_assignments(d):
    """An iterator to generate all the possible assignments of a dictionary d.
    NB: the call returns an iterator of assignments, not the assignments."""
    pass


def evaluate_all_assignments(formula):
    """Returns, for each possible assignment of the variables of the formula,
    the list of the number of satisfied clauses (with Boolean value True)."""
    pass


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
