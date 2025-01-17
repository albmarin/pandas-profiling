"""
Test for issue 120:
https://github.com/ydataai/pandas-profiling/issues/120
"""
import pandas as pd

from pandas_profiling import ProfileReport


def test_issue_120(get_data_file):
    file_name = get_data_file(
        "pandas_profiling_bug.txt",
        "https://github.com/ydataai/pandas-profiling/files/2386812/pandas_profiling_bug.txt",
    )
    df = pd.read_csv(file_name)

    report = ProfileReport(
        df,
        correlations=None,
        progress_bar=False,
        pool_size=1,
        vars={"cat": {"words": True, "characters": True}},
    )
    _ = report.report
    assert report.description_set is not None
