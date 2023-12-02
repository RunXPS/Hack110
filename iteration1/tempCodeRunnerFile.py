"""The backend of the movie_guesser project."""

from csv import DictReader
import random



def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Take in all rows of a csv file and output them as a list of dictionaries."""
    result: list[dict[str, str]] = []
    file_handle = open(path, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    #print(result[0])
    return result

# Current: row with lables

def randMovie(data: list[dict[str,str]]):
    """One session of the game."""
    # print(data)
    row: dict[str, str] = data[random.randrange(0, len(data))]

    guesses: int = 1
    print(f"---Where is this quote from?---\n{row['quote']}\n")
    while (guesses < 3):
        
        usr_inp: str = input(f"Guess {guesses}/3: ")
        if (usr_inp.lower() in row['movie'].lower() and len(usr_inp) >= 5):
            print(f"Correct! Solved in {guesses}/3 tries")
            return
        else:
            print(f"Incorrect. Try again.")
        guesses += 1
             
    print(f"It was: '{row['movie']}'. Better luck next time!")


def main():
    movie_data: list[dict[str, str]] = []
    movie_data = read_csv_rows("/workspaces/Hack110/iteration1/movie_quotes.csv")
    randMovie(movie_data)

if __name__ == "__main__":
    main()