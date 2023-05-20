from cito.cite import cite

for index, evidence in cite("~/Projects/legal-hackathon/test_argument.txt"):
    print(index, evidence)
