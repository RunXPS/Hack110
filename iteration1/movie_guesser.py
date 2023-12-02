"""The backend of the movie_guesser project."""

from csv import DictReader
import random

movie_data: list[dict[str,str]] = []

def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Take in all rows of a csv file and output them as a list of dictionaries."""
    result: list[dict[str, str]] = []
    file_handle = open(path, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    print(result[0])
    return result

# Current: row with lables

def randMovie():
    """One session of the game."""
    print(movie_data)
    #row: int = random.randrange(0, len(movie_data))
    #print(f"Where is this quote from?\n{row['quote']}")


def main():
    movie_data = read_csv_rows("/workspaces/Hack110/iteration1/movie_quotes.csv")
    randMovie()

if __name__ == "__main__":
    main()