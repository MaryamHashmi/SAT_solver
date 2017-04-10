#solver
#This solver takes input in phi

#based on DPLL logic

def standardize(phi):
    if type(phi) is str:  # must be a single positive literal
        return ["and", ["or", phi]]
    elif phi[0] == "not":  # must be a single negative literal
        return ["and", ["or", phi]]
    elif phi[0] == "or":  # a single clause
        return ["and", phi]
    else:
        result = ["and"]
        for c in phi[1:]:
            if type(c) == str:
                result.append(["or", c])
            elif c[0] == "not":
                result.append(["or", c])
            else:
                result.append(c)
        return result


def all_true(phi, model):  # at least one member of model in each clause
    for clause in phi[1:]:  # skip the "and"
        if len([var for var in clause[1:] if var in model]) == 0:
            return False
    return True


def negation(model):  # returns the compliment of each model literal
    result = []
    for literal in model:
        if type(literal) is str:
            result.append(["not", literal])
        else:
            result.append(literal[0])
    return result


def false(phi, model):  # some clause cannot be satisfied
    modelnegation = negation(model)
    for clause in phi[1:]:
        if len([var for var in clause[1:] if var not in modelnegation]) == 0:
            return True
    return False


def pure_literal(phi, model):  # finds 1 pure literal not already in model
    modelnegation = negation(model)
    candidates = []
    for clause in phi[1:]:
        if len([var for var in clause[1:] if var in model]) == 0:
            # clause not yet satisfied by model
            candidates = candidates + [var for var in clause[1:]]
    candidatenegation = negation(candidates)
    pure = [var for var in candidates if var not in candidatenegation]
    for var in pure:
        if var not in model and var not in modelnegation:
            return var
    return False


def unit_clause(phi, model):  # finds 1 literal not in model appearing by itself in a clause
    modelnegation = negation(model)
    for clause in phi[1:]:
        remaining = [var for var in clause[1:] if var not in modelnegation]
        if len(remaining) == 1:
            if remaining[0] not in model:
                return remaining[0]
    return False


def positive_literal(phi, model):  # finds a positive literal not in model or model negation
    combined = model + negation(model)
    for clause in phi[1:]:
        for literal in clause[1:]:
            if type(literal) is str and literal not in combined:
                return literal
    return False


def dpll(phi):
    #
    return dpll1(standardize(phi), [])
    # return dpll1(phi, [])


def dpll1(phi, model):
    if all_true(phi, model):
        return model
    
    
    if false(phi, model):
        return False
    pure = pure_literal(phi, model)
    if pure:
        return dpll1(phi, model + [pure])
    unit = unit_clause(phi, model)
    if unit:
        return dpll1(phi, model + [unit])
    pick = positive_literal(phi, model)
    if pick:
        # try positive
        result = dpll1(phi, model + [pick])
        if result:
            return result
        else:
            # try negative
            result = dpll1(phi, model + [['not', pick]])
            if result:
                return result
            else:
                return False


def output(result):

    if result == False:
        return ["Contradiction"]
    if len(result) == 1:
        return ["Tautology"]
    else:
        mod = ["true"]
        for v in result:
            if type(v) is str:
                mod.append(v + "=true")
            else:
                mod.append(v[1] + "=false")
        return mod
