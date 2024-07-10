import zipfile

zip_file = "train.csv.zip"
extract_to = "dataset"

with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print("Extraction completed successfully.")
