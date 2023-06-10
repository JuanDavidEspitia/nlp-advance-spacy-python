import sys

from spacy.lang.es import Spanish


nlp = Spanish()


def main(args: dict) -> None:
    # Procesando un string de texto con el objeto nlp
    doc = nlp("Hol mundo, Soy Juan David!")

    # Itera sobre los tokens en un Doc (Document)
    for token in doc:
        print(token.text)

    # Podemos usar indices del Doc para obtener un solo token
    print("Obtenemos un token del objeto Doc: \n")
    token = doc[4]
    # Obtenemos el texto del token con el atributo .text
    print(f"El valor del indice es: {token.text}")

    # El objeto Span
    # Es un slice de un Doc que puede obtener mas de un token
    span = doc[3:6]
    print(f"El texto del span es: {span}")

    # Atributos lexicos
    doc = nlp("Eso cuesta 5 $ .")

    print("Index:      ", [token.i for token in doc])
    print("Text:       ", [token.text for token in doc])

    print(
        "is_alpha:   ", [token.is_alpha for token in doc]
    )  # Devuelve true si es alfanumerico
    print(
        "is_punct:   ", [token.is_punct for token in doc]
    )  # Devuelve true si es puntp
    print(
        "like_num:   ", [token.like_num for token in doc]
    )  # Devuelve true si es numerico


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main(sys)
