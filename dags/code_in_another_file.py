# I put this code in another file to show one way to use code in multiple files
def load_csv(local_path, **kwargs):
    import pandas as pd
    data = pd.read_csv(local_path)
    data.to_csv(local_path + ".loaded")
