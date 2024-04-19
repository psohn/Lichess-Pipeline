import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def column_name_util(x):
    raw_data = x["raw_data"].strip()
    if raw_data.startswith("["):
        return x["raw_data"].split(" ")[0].replace("[", "")
    elif raw_data.startswith("1."):
        return "Moves"
    elif raw_data in ["0-1", "1-0"]:
        return "ResultRepeat"
    else:
        print(raw_data)
        raise ValueError

def value_util(x):
    raw_data = x["raw_data"].strip()
    if raw_data.startswith("["):
        return " ".join(x["raw_data"].split(" ")[1:]).replace("]", "").replace('"', '')
    elif raw_data.startswith("1."):
        return raw_data
    elif raw_data in ["0-1", "1-0"]:
        return raw_data
    else:
        print(raw_data)
        raise ValueError


@transformer
def transform(data, *args, **kwargs):
    data["column_name"] = data.apply(lambda x: column_name_util(x), axis = 1)
    data["value"] = data.apply(lambda x: value_util(x), axis = 1)
    data["grouping"] = data["column_name"] == "Event"
    data["grouping"] = data["grouping"].cumsum() - 1
    data = data.pivot(index="grouping", columns="column_name", values="value")
    data.reset_index(drop=True, inplace=True)
    data.rename_axis(None, axis=1, inplace=True)

    data["Date"] = pd.to_datetime(data["UTCDate"].str.replace(".", "-") + " " + data["UTCTime"], utc=True)
    data["WhiteVictory"] = data["Result"] == "1-0"
    data.drop(columns=["ResultRepeat", "UTCDate", "UTCTime", "Result"], inplace=True)
    data.columns = data.columns.str.lower()

    return data

@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
