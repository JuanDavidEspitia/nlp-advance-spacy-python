import sys
import spacy


nlp = spacy.load("es_core_news_sm")
"""
    1. Parametros binarios
    2. Vocabulario
    3. Metadata (lenguaje, pipeline)
"""


def main(args: dict) -> None:
    """
    Prediciendo part-of-speech tags
    """
    # Procesa texto
    doc = nlp("Ella comío pizza")

    # Itera sobre los tokens
    for token in doc:
        print(token.text, token.pos_)

    print("*************************")
    # Itera sobre los tokens
    for token in doc:
        print(token.text, token.pos_, token.dep_, token.head.text)
        # Esquema dependency label

    """
    Prediciendo entidades nombradas
    """
    print("*************************")
    doc = nlp(
        "Apple es una marca que mas satisfaccion genera en EE.UU., "
        "pero el Iphone, fue superado por el Galaxy Note 9"
    )
    # Itera sobre las entidades predichas
    for ent in doc.ents:
        # Imprime en pantalla el texto y el label de la entidad
        # MISC es categoria Miscelanea
        print(ent.text, ent.label_)

    # Tip: El metodo spacy.explain(), retornna una ayuda y definicion de los tipos de entidades y tags
    print(spacy.explain("NNP"))
    print(spacy.explain("LOC"))
    print(spacy.explain("MISC"))


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main(sys)
