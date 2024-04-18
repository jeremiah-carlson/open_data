import polars as pl
from typing import List
import pickle as pkl

from utils.types import OutFile

def parse_zip_centroids(root_path: str, output: List[OutFile]):
    df_usa = pl.read_csv('%s/input/geo/zip_code_centroids/USA.csv' % root_path)

    parsed = df_usa.select([
        pl.col('STD_ZIP5').cast(pl.String).str.zfill(5).alias('zip'),
        pl.col('LAT').alias('lat'),
        pl.col('LGT').alias('lgt')
    ])

    if OutFile.CSV in output:
        parsed.write_csv('%s/output/geo/zip_code_centroids/USA.csv' % root_path)

    if OutFile.PARQUET in output:
        parsed.write_parquet('%s/output/geo/zip_code_centroids/USA.parquet' % root_path)

    if OutFile.XLSX in output:
        parsed.write_excel('%s/output/geo/zip_code_centroids/USA.xlsx' % root_path)

    if OutFile.PICKLE in output:
        np_arr = parsed.to_numpy(structured=True)
        with open('%s/output/geo/zip_code_centroids/USA.pkl' % root_path, 'wb+') as f:
            pkl.dump(np_arr, f)
