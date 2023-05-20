from cito.cite import cite
from cito.format import format_citations

citations = cite("~/Projects/legal-hackathon/test_argument.txt"):

print(format_citations(citations))


