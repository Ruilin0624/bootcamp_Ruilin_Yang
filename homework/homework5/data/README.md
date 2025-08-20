Update README.md with a Data Storage section describing:

**Folder structure (data/raw/, data/processed/)**
raw = stored csv files
--> All datas are stored as plain text (`string`/`object`) dtype

processed = stored processed parquet files
--> data are datetime instead of float in raw, it recognize time 

**Formats used and why**
CSV
  - Human-readable and portable.  
  - Good for manual inspection or quick debugging.  
  - Widely supported by external tools.  

Parquet (processed)
  - Preserves dtypes (e.g. `datetime64[ns]`, `int64`, `float64`).  
  - Better suited for large-scale analytics and reproducible workflows.  


**How your code reads/writes using env variables**
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed
