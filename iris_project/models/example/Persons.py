def model(dbt, session):
    dbt.config(materialized="table")

    persons_df = dbt.source("dbt_iris_source", "Persons")
    return persons_df