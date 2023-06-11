import sys
import spacy

# Importar el Matcher
from spacy.matcher import Matcher

nlp = spacy.load("es_core_news_sm")


def main(args: dict) -> None:
    """
    Matching en Objetos Doc, no solamente en strings
    Matching en tokens y atrubutos de tokens
    Usa las predicciones del modelo
    Ejemplo 'araña' (verbo) vs 'araña' (sustantivo)
    """

    """
    Los Match Patterns
        1. Lista de diccionarios uno por token
        2. Encuentra por textos exactos de tokens
        3. Encuentra por atributos lexicos
        4. Encuentra por cualquier atributo de token
    """
    # Inicializa el matcher con el vocabulario compartido
    matcher = Matcher(nlp.vocab)

    # Añade el patron al matcher
    pattern = [{"TEXT": "adidas"}, {"TEXT": "zx"}]
    matcher.add("ADDIDAS_PATTERN", [pattern])

    # Procesa un texto
    doc = nlp("Nuevos diseños de zapatillas er la colleccion de adidas zx")

    # llama al matcher sobre el doc
    matches = matcher(doc)

    # itera sobre los resultados
    for match_id, start, end in matches:
        # Obten el span resultando
        matched_span = doc[start:end]
        print(matched_span.text)

    """
    match_id: valor hash del nombre del patron
    start: indice de inicio del span resultante
    end: indice del final del span resultante
    """
    print("**********************************")
    # Ahora, con atributos lexicos
    pattern = [
        {"IS_DIGIT": True},
        {"LOWER": "copa"},
        {"LOWER": "mundial"},
        {"LOWER": "fifa"},
        {"IS_PUNCT": True},
    ]
    matcher.add("FIFA_PATTERN", [pattern])
    doc = nlp("2014 Copa Mundial FIFA: Alemania gano!")
    matches = matcher(doc)
    # itera sobre los resultados
    for match_id, start, end in matches:
        # Obten el span resultando
        matched_span = doc[start:end]
        print(matched_span.text)

    print("**********************************")
    # Encontrando por atributos de token
    pattern = [{"LEMMA": "comer", "POS": "VERB"}, {"POS": "NOUN"}]
    matcher.add("VERB_PATTERN", [pattern])
    doc = nlp("Camila prefería comer tacos. Pero ahora esta comiendo pasta.")
    matches = matcher(doc)
    # itera sobre los resultados
    for match_id, start, end in matches:
        # Obten el span resultando
        matched_span = doc[start:end]
        print(matched_span.text)

    print("\n")
    print(spacy.explain("DET"))
    print(spacy.explain("POS"))

    print("**********************************")
    # Encontrando por operadores y cuantificadores
    pattern = [
        {"LEMMA": "comprar"},
        {"POS": "DET", "OP": "*"},  # opcional: encuentra 0 o 1 veces
        {"POS": "NOUN"},
    ]
    matcher.add("COMPRA_PATTERN", [pattern])
    doc = nlp("Me compré un smartphone. Ahora le estoy comprando aplicaciones.")
    matches = matcher(doc)
    # itera sobre los resultados
    for match_id, start, end in matches:
        # Obten el span resultando
        matched_span = doc[start:end]
        print(matched_span.text)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main(sys)
