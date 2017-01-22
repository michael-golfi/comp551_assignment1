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
        def get_sec_pace(time_str):
            m, s = time_str.split(':')
            return int(m) * 60 + int(s)

        df['Time'] = df['Time'].apply(get_sec)
        df['Pace'] = df['Pace'].apply(get_sec_pace)
        return df

    def cut(df, key, bins):
        df[key] = pd.cut(df[key], bins=bins, include_lowest=True, right=False)
        return df

    def remove_duplicate_runners(df):
        df = df \
            .groupby(["Year", "Id", "Name", "Age Category", "Sex"]) \
            .agg({'Rank': np.mean,'Time': np.mean,'Pace': np.mean}) \
            .reset_index()
        df = df[["Id", "Name", "Age Category", "Sex", "Pace", "Rank", "Time", "Year"]]
        return df

    pd.DataFrame.equals = equals
    pd.DataFrame.greater_than = greater_than
    pd.DataFrame.not_equals = not_equals
    pd.DataFrame.convert_time = convert_time
    pd.DataFrame.cut = cut
    pd.DataFrame.remove_duplicate_runners = remove_duplicate_runners

def save_groups(basePath, groups):
    [g.to_csv("{0}{1}.csv".format(basePath, k)) for (k,g) in groups]