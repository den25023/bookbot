from stats import get_num_words, broj_karaktera, sortirana_dict
import sys

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)

    # Broj reči
    num_words = get_num_words(book_text)

    # Broj pojavljivanja karaktera
    broj_ponavljanja_slova = broj_karaktera(book_text)
    sortirani_broj_slova = sortirana_dict(broj_ponavljanja_slova)

    # ----- Format ispisa -----
    print("=========== BOOKBOT ===========")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char, count in sortirani_broj_slova:
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()
