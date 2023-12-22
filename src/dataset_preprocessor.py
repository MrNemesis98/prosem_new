import pandas as pd
import uuid

def create_output_table(input_file, output_file, label, search_words):
    df = pd.read_csv(input_file)

    df = df.rename(columns={'No.': 'idx', 'Hit': 'text'})
    df = df.drop(columns=['Date', 'Bibl', 'Genre', 'URL'])

    # label column
    df['label'] = label

    # span-column and nltk column
    spans = []
    indexes = []
    for entry in df['text']:

        index = uuid.uuid4()
        indexes.append(index)

        entry = str(entry)
        span_found = False
        for word in search_words:
            start_index = entry.find(word)
            if start_index != -1 and not span_found:
                end_index = start_index + len(word)
                span = "[" + str(start_index) + ", " + str(end_index) + "]"
                spans.append(span)
                span_found = True
                break  # breche die innere Schleife ab, nachdem ein Span gefunden wurde
        else:
            # Diese Zeile wird nur dann ausgeführt, wenn die innere Schleife nicht mit einem 'break' beendet wurde
            span = "[ N / V ]"
            spans.append(span)


    df['span'] = spans

    df['idx'] = indexes
    df['idx'] = df['idx'].shift(1)
    df.loc[0, 'idx'] = "idx"
    # df['text'] = df['text'].astype(str)
    df['text'] = df['text'].shift(1)
    # df['label'] = df['label'].astype(str)
    df['label'] = df['label'].shift(1)
    # df['span'] = df['span'].astype(str)
    df['span'] = df['span'].shift(1)

    df.to_csv(output_file, index=False)

    print(f"Process finished! Output saved to {output_file}.")


input_file = "corona/raw/non_cpd/prosem_data_corpus-corona_term-warum.csv"
output_file = "corona/preprocessed/non_cpd/prosem_data_corpus-corona_term-warum_processed.csv"
label = "corona"

"""Search word lists for direct_cpd terms"""
# search_words = ["Maske", "Masken", "'Maske", "Maske."]
# search_words = ["Mutation", "Mutationen"]
# search_words = ["Querdenker", "Querdenkers", "Querdenkern", "'Querdenker"]
# search_words = ["Variante", "Variante'", "Variante.", "'Variante", "'Variante'", "Varianten", "Varianten.", #
#                 "'Varianten'", "Variant", "'Variant'"]
# search_words = ["Virus", "Virus'", "Virus.", "'Virus", "'Virus'", "Viren", "Viren.", "'Viren'"]

"""Search word lists for indirect_cpd terms"""
# search_words = ["Haus", "Hause", "zuhause", "Häuser", "Häusern", "Hauses"]
# search_words = ["Leben", "Lebens"]
# search_words = ["Mensch", "Menschen"]
# search_words = ["Tier", "Tieres", "Tiere", "Tieren"]
# search_words = ["Urlaub", "Urlaubes", "Urlaubs", "Urlaube", "Urlauben"]

"""Search word lists for non_cpd terms"""
# search_words = ["!"]
# search_words = ["bei", "Bei"]
# search_words = ["manche", "manchen", "mancher", "manchem", "manches",
#                 "Manche", "Manchen", "Mancher", "Manchem", "Manches"]
# search_words = ["schlafen", "schlafe", "schläfst", "schläft", "schlaft", "schlief", "schliefst",
#                 "schliefen", "schlieft", "schliefet", "geschlafen","Schlafen", "Schlafe",
#                 "Schläfst", "Schläft", "Schlaft", "Schlief", "Schliefst", "Schliefen",
#                 "Schlieft", "Schliefet", "Geschlafen"]
search_words = ["warum", "Warum"]

create_output_table(input_file, output_file, label, search_words)