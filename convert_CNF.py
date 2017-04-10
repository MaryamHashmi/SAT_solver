# convert_CNF
import SAT_solver

def bicon(phi):  #resolving biconditional to implication
    if type(phi) is str:
        return phi
    elif type(phi) is list and phi[0] == "bicon":
        return ([
            "and",
            ["imp", bicon(phi[1]), bicon(phi[2])],
            ["imp", bicon(phi[2]), bicon(phi[1])]
        ])
    else:
        return [phi[0]]+[bicon(x) for x in phi[1:]]


def imp(phi):  #resolving implication to or
    if type(phi) is str:
        return phi
    elif type(phi) is list and phi[0] == "imp":
        return ([
            "or",
            ["not",
            imp(phi[1])],
            [imp(phi[2])]
        ])

    else:
        return [phi[0]]+[imp(x) for x in phi[1:]]


def neg(phi): #resolving double negation using DeMorgan's law
    if type(phi) is str:
        return phi
    elif type(phi) is list and phi[0] == "not"  and  type(phi[1]) is list and phi[1][0] == "and":
        return (["or"] + [neg(["not",x]) for x in phi[1][1:]])
    elif type(phi) is list and phi[0] == "not"  and  type(phi[1]) is list and phi[1][0] == "or":
        return (["and"] + [neg(["not",x]) for x in phi[1][1:]])
    else:
        return [phi[0]]+[neg(x) for x in phi[1:]]

def double_neg(phi):  #removing double negation
    if type(phi) is str:
        return phi
    elif type(phi) is list and phi[0] == "not"  and  type(phi[1]) is list and phi[1][0] == "not":
        return double_neg(phi[1][1])
    else:
        return [phi[0]]+[double_neg(x) for x in phi[1:]]


def distributivity(phi):  #resolving or over and
    if type(phi) is str:
        return phi
    elif type(phi) is list and phi[0] == "or"  and  type(phi[1]) is list and phi[1][0] == "and":
        return(["and"] + [distributivity(["or", i, phi[2]]) for i in phi[1][1:]])
    elif type(phi) is list and phi[0] == "or"  and  type(phi[2]) is list and phi[2][0] == "and":
        return(["and"] + [distributivity(["or",  phi[1],i]) for i in phi[2][1:]])
    else:
        return ([phi[0]] + [distributivity(i) for i in phi[1:]])

def orAssociativity(phi): #resolving or association
    if type(phi) is str:
        return phi
    elif type(phi) is list and phi[0] == "or":
        result = ["or"]
        # iterate through disjuncts looking for "or" lists
        for i in phi[1:]:
            if type(i) is list and i[0] == "or":
                result = result + i[1:]
            else:
                result.append(i)
        return result
    else:
        return([phi[0]] + [orAssociativity(i) for i in phi[1:]])


def andAssociativity(phi):  #resolving and asscoiation
    if type(phi) is str:
        return phi
    elif type(phi) is list and phi[0] == "and":
        result = ["and"]
        # iterate through disjuncts looking for "or" lists
        for i in phi[1:]:
            if type(i) is list and i[0] == "and":
                result = result + i[1:]
            else:
                result.append(i)
        return result
    else:
        return([phi[0]] + [andAssociativity(i) for i in phi[1:]])

def cnf(phi):
    phi=bicon(phi)
    phi=imp(phi)
    phi=double_neg(phi)
    phi=neg(phi)
    phi=distributivity(phi)
    phi=orAssociativity(phi)
    phi=andAssociativity(phi)
    print "Conjunctive normal form: ", phi
    return phi


#
# # phi=["not",["not","b"]]
# # cnf(phi)
# #
# # phi=["bicon","a","b"]
# # phi=cnf(phi)
# # print " "
# # print solver.dpll(phi)
# #
# # phi=["not", ["or", "P", "Q"]]
# # cnf(phi)
# #
# # phi=["not", ["and", ["or","p","q"], "R"]]
# # cnf(phi)
# # print 5
# # phi=["or", ["and",["not", "P"], "Q"],"R"]
# # phi=cnf(phi)
#
# # phi=["or",["or", "P", "Q"],"R" ]
# # cnf(phi)
# #
# phi=["imp","P","R"]
# print "phi: ",phi
# phi=cnf(phi)
#
# print SAT_solver.output(SAT_solver.dpll(phi))
# print " "
# phi=["or","A",["not","A"]]
# phi=cnf(phi)
# print " "
# print SAT_solver.output(SAT_solver.dpll(phi))
#
# phi=["and","1",["not","1"]]
# phi=cnf(phi)
# print " "
# print SAT_solver.output(SAT_solver.dpll(phi))
