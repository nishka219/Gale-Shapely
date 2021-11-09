def stableMatching(n, menPreferences, womenPreferences):

# Initially, all n men are unmarried
unmarriedMen = list(range(n))

# None of the men has a spouse yet, we denote this by the value
None
manSpouse = [None] * n

# None of the women has a spouse yet, we denote this by the
value None
womanSpouse = [None] * n

# to compare the preference of women when there are two
proposing men
hisweight = [0] * n

# While there exists at least one unmarried man:
while unmarriedMen:

# Pick an arbitrary unmarried man
he = unmarriedMen[0]

# Store his ranking in this variable for convenience
hisPreferences = menPreferences[he]

# Find a woman to propose to
she = hisPreferences[0]

# Store her ranking in this variable for convenience
herPreferences = womenPreferences[she]

# if the man is rejected by the woman yet
if he in herPreferences:

# if she is unmarried
if womanSpouse[she]==None:

# engage the unmarried woman to the proposing man
womanSpouse[she]=he

# record his ranking in a separate list, used later to

compare if any other proposer asks for her
hisweight[she]=herPreferences.index(he)

# engage the proposing man to the unmarried woman
manSpouse[he]=she

# remove the newly married man from the unmarriedMen

list

unmarriedMen.remove(he)

# if the proposed woman is already married
else:

# store the ranking of the proposing man
currwt = herPreferences.index(he)

# if he has higher preference than her previous husband
if currwt<hisweight[she]:

# remove the new proposer from the unmarriedMen list
unmarriedMen.remove(he)

# add her previous husband to the unmarriedMen list
unmarriedMen=[womanSpouse[she]]+unmarriedMen

# update the rejected mans marriage status list
manSpouse[womanSpouse[she]]=None

# update the womans husband to the new(more

preferred) proposer

womanSpouse[she]=he

# record his ranking in the list, used later to compare if

any other proposer asks for her

hisweight[she]=herPreferences.index(he)

# update the new proposers marriage status and engage

him to this woman

manSpouse[he]=she

# remove the woman the proposer has already tried on
menPreferences[he].remove(she)

return manSpouse
