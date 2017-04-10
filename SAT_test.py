#SAT solver
#MARYAM HASHMI
#DUA ANJUM

#sat solver takes input in preorder form
#like ["operator", ["clause"], ["clause"]]

import SAT_solver
import convert_CNF

#contradictions
print " "
print " "
print "Contradictions"
print " "

c1=["and","A",["not","A"]]
print "c1: ",c1
c1=convert_CNF.cnf(c1)
print SAT_solver.output(SAT_solver.dpll(c1))
c2=["and",["and","P",["not","P"]],"Q"]
print " "

print "c2: ",c2
c2=convert_CNF.cnf(c2)
print SAT_solver.output(SAT_solver.dpll(c2))


#Tautology
print " "
print " "
print "Tautology"
print " "

t1=["or","1",["not","1"]]
print "t1: ",t1
t1=convert_CNF.cnf(t1)
print SAT_solver.output(SAT_solver.dpll(t1))

t2=["or",["imp","P","Q"],["imp","Q","P"]]
print " "
print "t2: ",t2
t2=convert_CNF.cnf(t2)
print SAT_solver.output(SAT_solver.dpll(t2))

t3=['not',['and','P',['not','P']]]
print " "
print "t3: ",t3
t3=convert_CNF.cnf(t3)
print SAT_solver.output(SAT_solver.dpll(t3))

#contigency
print " "
print " "
print "Contigency"
print " "

c1=['bicon','A','B']
print "c1: ",c1
c1=convert_CNF.cnf(c1)
print SAT_solver.output(SAT_solver.dpll(c1))
print " "

c2=['and', 'A', 'B']
print "c2: ",c2
c2=convert_CNF.cnf(c2)
print SAT_solver.output(SAT_solver.dpll(c2))
print ' '

c3=["or",["and", "P", "Q"],"R" ]
print "c3: ",c3
c3=convert_CNF.cnf(c3)
print SAT_solver.output(SAT_solver.dpll(c3))
print " "