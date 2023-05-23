from cito.cite import cite
from cito.format import format_citations

if __name__ == "__main__":

    citations = cite("../test_argument.txt")

    formatted_citations = format_citations(citations)

    with open("formatted_citations.txt", "w") as f:
        f.write(formatted_citations)
