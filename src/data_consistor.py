import pandas as pd
import regex as re


def scan_for_errors(file, make_corrections=False):
    df = pd.read_csv(file)
    counts = 0
    for index, row in df.iterrows():
        current_span = str(row['span'])

        # Regulärer Ausdruck, um die erste Zahl zu extrahieren
        pattern = r'\[([0-9]+),\s*[0-9]+\]'
        match = re.match(pattern, current_span)
        current_row = index + 2
        if not match and current_row != 2:
            print("Span error in Zeile {}: {}".format(current_row, current_span))
            if make_corrections and current_row != 2:
                print(current_row)
                df['span'].replace(current_span, pd.NA, inplace=True)
                df_cleaned = df.dropna(subset=['span'])
                df_cleaned.to_csv(file, index=False)
            counts += 1
            print(counts)


scan_for_errors("../data/raw_and_preprocessing/web2/preprocessed/non_cpd/"
                "prosem_data_corpus-web2_term-warum_processed.csv",
                make_corrections=False)

