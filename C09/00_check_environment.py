import duckdb
import polars as pl

# 재현 가능한 분석을 위해 실제 설치 버전을 기록합니다.
print("Polars 버전:", pl.__version__)
print("DuckDB 버전:", duckdb.__version__)

# DuckDB 엔진이 정상적으로 SQL을 실행하는지 확인합니다.
result = duckdb.sql("SELECT 40 + 2 AS answer").fetchone()
print("DuckDB 계산 결과:", result[0])