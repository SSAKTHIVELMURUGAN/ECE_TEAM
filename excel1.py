import pandas as pd

def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    return df

def find_top_three_rank_holders(df):
    top_three = df.sort_values(by='Rank').head(3)
    return top_three

def write_to_text_file(top_three, output_file):
    with open(output_file, 'w') as file:
        file.write("Top Three Rank Holders:\n")
        file.write(top_three.to_string(index=False))

def main():
    file_path = r"C:\Users\21ecb\Downloads\sample.csv"

    df = read_csv_file(file_path)
    
    if df is not None:
        top_three = find_top_three_rank_holders(df)

        output_file = "top_three_rank_holders.txt"
        write_to_text_file(top_three, output_file)
        print(f"Top three rank holders written to '{output_file}' successfully.")

if __name__ == "__main__":
    main()
