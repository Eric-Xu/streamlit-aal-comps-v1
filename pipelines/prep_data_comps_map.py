import logging
import os
from typing import Dict

from pandas import DataFrame

from constants.file import DATA_DIR, NEARBY_FLIPS_DATA_FILE, TMP_DIR, TMP_TEST_JSON
from functions.io import load_df, save_json


def prep_data() -> None:
    test_data: Dict = {"address": "123 Main St"}

    save_json(
        os.path.join(TMP_DIR, TMP_TEST_JSON),
        test_data,
    )

    nearby_flips_df: DataFrame = load_df(os.path.join(DATA_DIR, NEARBY_FLIPS_DATA_FILE))
    logging.info(f"Size: {nearby_flips_df.size}")
