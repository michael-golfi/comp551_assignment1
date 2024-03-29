def init_pandas(pd, np):
    def equals(df, key, value):
        return df[df[key] == value]

    def greater_than(df, key, value):
        return df[df[key] > value]

    def not_equals(df, key, value):
        return df[df[key] != value]

    def convert_time(df):
        def get_sec(time_str):
            h, m, s = time_str.split(':')
            return int(h) * 3600 + int(m) * 60 + int(s)
        df['Time'] = df['Time'].apply(get_sec)
        return df

    def cut(df, key, bins):
        df[key] = pd.cut(df[key], bins=bins, include_lowest=True, right=False)
        return df

    def remove_duplicate_runners(df, cols):
        df = df \
            .groupby(["Year", "Id", "Age Category", "Sex"]) \
            .agg({'Rank': np.mean,'Time': np.mean}) \
            .reset_index()
        return df[cols]

    def reigel(df):
        df["Time"] = df[df["Year"] == 2013]["Time"].apply(lambda x: x * 2**1.06)
        return df

    pd.DataFrame.equals = equals
    pd.DataFrame.greater_than = greater_than
    pd.DataFrame.not_equals = not_equals
    pd.DataFrame.convert_time = convert_time
    pd.DataFrame.cut = cut
    pd.DataFrame.reigel = reigel
    pd.DataFrame.remove_duplicate_runners = remove_duplicate_runners

def save_groups(basePath, groups):
    [g.to_csv("{0}{1}.csv".format(basePath, k)) for (k,g) in groups]
