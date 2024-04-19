import pandas as pd
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    url = "https://database.lichess.org/standard/lichess_db_standard_rated_2014-01.pgn.zst"

    return pd.read_csv(url, on_bad_lines="skip", header=None, names = ["raw_data"])


@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
