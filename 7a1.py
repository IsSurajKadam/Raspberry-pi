from simpleai.search import CspProblem , backtrack,min_conflicts
from simpleai.search.viewers import ConsoleViewer
from simpleai.search.csp import(
  MOST_CONSTRAINED_VARIABLE,
  LEAST_CONSTRAINING_VALUE,
  HIGHEST_DEGREE_VARIABLE
)

variables=('WA','NT','SA','V','T','NSW','Q')
domains=dict((v ,['red','green','blue']) for v in variables)

def const_different(values, variables):
  return values[0] != values[1]

constraints=[
  (('WA','NT'),const_different),
  (('WA','SA'),const_different),
  (('NT','SA'),const_different),
  (('NT','V'),const_different),
  (('SA','T'),const_different),
  (('T','NSW'),const_different),
  (('NSW','Q'),const_different)

]

my_problem=CspProblem(variables,domains,constraints)

print("\nsolution with default backtracking: ",backtrack(my_problem))

print("\n solution with most contraints variables herstics: ",backtrack(my_problem,variable_heuristic=MOST_CONSTRAINED_VARIABLE))

print("\n solution with highest constraints varible herustics: ",backtrack(my_problem,variable_heuristic=HIGHEST_DEGREE_VARIABLE))

print('\n solution with lest constraints values heriticts: ',backtrack(my_problem,value_heuristic=LEAST_CONSTRAINING_VALUE))

print("\n solution with most constraineted varible and lest value: ",backtrack(my_problem,value_heuristic=LEAST_CONSTRAINING_VALUE,variable_heuristic=MOST_CONSTRAINED_VARIABLE))

print("\n solution with mincnfilic value: ",min_conflicts(my_problem))