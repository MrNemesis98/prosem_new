import pandas as pd
from nltk.tokenize import word_tokenize


def create_output_table(input_file, output_file, label, search_words):

    df = pd.read_csv(input_file)

    df = df.rename(columns={'No.': 'idx', 'Hit': 'text'})
    df = df.drop(columns=['Date', 'Bibl', 'Genre', 'URL'])

    # label column
    df['label'] = label

    # span-column and nltk column
    spans = []
    nltk = []
    for entry in df['text']:
        tokens = word_tokenize(str(entry))     # watch out if this str wrapping really works for all csv tables!
        sentence = " ".join(tokens)
        nltk.append(sentence)
        entry = ""
        stop = False
        for token in tokens:
            for sw in search_words:
                if not stop and token.lower() == sw.lower():
                    index = tokens.index(token)
                    entry = "[" + str(index) + ", " + str(index+1) + "]"
                    stop = True
        spans.append(entry)
    df['span'] = spans
    df['nltk'] = nltk

    df['idx'] = df['idx'].astype(str)
    df['idx'] = df['idx'].shift(1)
    df.at[0, 'idx'] = "idx"
    # df['text'] = df['text'].astype(str)
    df['text'] = df['text'].shift(1)
    # df['label'] = df['label'].astype(str)
    df['label'] = df['label'].shift(1)
    # df['span'] = df['span'].astype(str)
    df['span'] = df['span'].shift(1)
    # df['nltk'] = df['nltk'].astype(str)
    df['nltk'] = df['nltk'].shift(1)

    df.to_csv(output_file, index=False)

    print(f"Process finished! Output saved to {output_file}.")


input_file = "corona/raw/non_cpd/prosem_data_corpus-corona_term-!.csv"
output_file = "corona/preprocessed/non_cpd/prosem_data_corpus-corona_term-!_autoprocessed.csv"
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
search_words = ["!"]
# search_words = ["bei"]
# search_words = ["manche", "manchen", "mancher", "manchem"]
# search_words = ["schlafen", "schlafe", "schläfst", "schläft", "schlaft",
#                 "schlief", "schliefst", "schliefen", "schlieft",
#                 "schliefet", "geschlafen"]
# search_words = ["warum", "Warum"]

# create_output_table(input_file, output_file, label, search_words)


text = "Die Maske"
probe = "Maskem"
print(
    text.find(probe),
    text.find(probe) + len(probe)
)
# print(text[4:9])