import sys
import spacy

# Importar el Matcher
from spacy.matcher import Matcher

nlp = spacy.load("es_core_news_sm")


def main(args: dict) -> None:
    """
    Vocabulario compartido y String
        vocab: guarda datos compartidos a traves de multiples documentos
        1. para usar menos memoria spaCy codifica todos los string en valores hash
        2. los strings solo son guardaddos una vez en el StringStore via nlp.vocab.strings
    """
    cafe_hash = nlp.vocab.strings["cafe"]
    print(cafe_hash)
    cafe_string = nlp.vocab.strings[cafe_hash]
    print(cafe_string)

    # los hashes no pueden  ser revertidos - es por eso que debemos proveer un vocabulario compartido

    string = nlp.vocab.strings[10569699879655997926]
    print(string)

    """
    El doc tambien expone su vocabulario y sus strings
    """
    doc = nlp("Ines toma café")
    print("hash value: {}".format(doc.vocab.strings["cafe"]))

    """
    Lexemas:
        Son entradas en el vocabulario
        un objeto lexeme es una entrada en el vocabulario
    """
    doc = nlp("Ines toma cafe")
    lexeme = nlp.vocab["cafe"]
    print(lexeme.text, lexeme.orth, lexeme.is_alpha)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main(sys)
