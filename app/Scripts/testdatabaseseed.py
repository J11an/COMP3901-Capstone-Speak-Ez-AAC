import pandas as pd

def seed_database():
    print("test")
    df = pd.read_excel('Vocab_list .xlsx', sheet_name=None)

    for sheet_name, sheet_data in df.items():
        # if sheet_name == "Words":
        #     for index, row in sheet_data.iterrows():
        #         word = Words(

        #         word=(row['word']),
        #         partofspeech=(row['part_of_speech']),
        #         category=(row['category']),
        #         sub_category=(row['sub_category']),
        #         time=(row['time']),
        #         place=(row['place']),
        #         symbol_id=(row['symbol_id']),
        #         )
        #         print(word)
        # if sheet_name == "Parts_of_speech":
        #     for index, row in sheet_data.iterrows():
        #         print(row['pos_id'])
        #         print(row['pos'])
        # if sheet_name == "Adjectives":
        #     for index, row in sheet_data.iterrows():
        #         print(row['word_id'])
        #         print(row['word'])
        #         print(row['pos_id'])
        #         print(row['comparative'])
        #         print(row['superlative'])
        if sheet_name == "Nouns":
            for index, row in sheet_data.iterrows():
                print(row['word_id'])
                print(row['word'])
                print(row['pos_id'])
                print(row['plural'])
                print(row['possessive'])
                print(row['male'])
                print(row['Female'])
        # if sheet_name == "Verbs":
        #     for index, row in sheet_data.iterrows():
        #         print(row['word_id'])
        #         print(row['word'])
        #         print(row['pos_id'])
        #         print(row['plural'])
        #         print(row['past'])
        #         print(row['present_cont'])
        #         print(row['future'])
        #         print(row['perfect'])
        # if sheet_name == "Symbols":
        #     for index, row in sheet_data.iterrows():
        #         print(row['symbol_id'])
        #         print(row['symbol'])
        # break
    return "Database seeded successfully"

seed_database()