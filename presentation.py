import marimo

__generated_with = "0.14.7"
app = marimo.App(
    width="medium",
    layout_file="layouts/presentation.slides.json",
)


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Python is all you need: an overview of the composable, Python-native data stack

    Deepyaman Datta · Kedro Tech Design · June 25, 2025
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# The modern data stack""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Definition of the modern data stack

    > [a set of products that a) redesigned the analytics workflow to take advantage of the cloud and b) all interacted with one another via SQL](https://roundup.getdbt.com/p/is-the-modern-data-stack-still-a)
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## A brief history of the modern data stack

    * **2010–2014**: Google BigQuery, Amazon Redshift, and Snowflake launched
    * [Around the same time, core products of the would-be modern data stack were founded](https://www.getdbt.com/blog/future-of-the-modern-data-stack)
        * **2010**: Chartio
        * **2011**: Looker
        * **2012**: Mode
        * **2012**: Periscope
        * **2012**: Fivetran
        * **2014**: Metabase
        * **2015**: Stitch
        * **2015**: Redash
        * **2016**: dbt

    ![](public/mds-funding.png)
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## ELT vs ETL

    * ETL: transform before loading to warehouse
    * ELT: load first, then transform inside the warehouse

    ![](public/etl-vs-elt.png)
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## [The modern data stack as we know it](https://www.linkedin.com/pulse/what-steps-tools-setting-up-modern-saas-based-bi-tristan-handy/) (circa 2016)

    * **Ingestion**: Fivetran, Stitch
    * **Storage**: Bigquery, Databricks, Redshift, Snowflake
    * **Transformation**: dbt
    * **BI**: Looker, Mode, Periscope, Chartio, Metabase, Redash

    ![](public/dbt-wau.png)
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# And now, Python""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Where were we in all this?

    * Python: exploding in popularity, but second-class in MDS
    * Until now: Python-first data pipelines couldn't scale*

    ![](public/top-programming-languages.png)
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Enter the bird

    * **Ibis**: a lightweight Python library for data wrangling
    * Provides:
        * Pythonic dataframe API
        * Interfaces to 20+ query languages
        * Deferred execution model
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## [SKIP] Slide 3: Key Takeaways

    * Python-native data engineering is here—and it's powerful
    * You can build end-to-end pipelines with:

      * Ibis (transforms)
      * Kedro (orchestration)
      * dlt (ingestion)
      * Pandera (validation)
    * Composability means flexibility and reuse
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## [SKIP] Slide 4: The Rise of the Modern Data Stack

    * Born with cloud-native SQL tools: Redshift, BigQuery, Snowflake
    * ELT workflows took over from ETL
    * dbt popularized SQL transformations
    * But: everything assumed SQL at the core
    """
    )
    return


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md(r""" """)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## [SKIP] Slide 6: So... What About Python?

    * Python now rivals SQL in developer popularity
    * But still seen as the “fallback” for complex cases
    * Can we build **first-class** pipelines in Python?
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Slide 7: Introducing the Python Analytics Stack

    * Inspired by modular data system vision
    * Open standards, composability, and language flexibility
    * Key building block: **Ibis**
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Slide 8: Composable Data Management (Visual)



    * 5 logical layers
    * Language frontends (like Python) plug into many engines
    * Portable intermediate representation (IR)

    ![](public/modular-data-stack.png)
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Ibis = SQL Power + Python Syntax

    ```python
    t.filter(t.a > 1).select("a", "b", "c")
    ```

    Equivalent to:

    ```sql
    SELECT a, b, c FROM t WHERE a > 1
    ```

    * 20+ backends (BigQuery, DuckDB, Spark, Polars, etc.)
    * Lazily builds IR, compiles to backend-native SQL
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Slide 10: The Layers of the Python Stack

    * Data Storage: Lakehouse, DW, file formats
    * Data Ingestion: dlt
    * Transformation: Kedro + Ibis
    * Validation: Pandera
    * BI / Analytics: Streamlit, ML workflows
    * Optional: Orchestration (Airflow, Dagster)
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Slide 11: Data Storage & Ingestion

    * Ibis supports Parquet, CSV, JSON, Delta, Iceberg, etc.
    * dlt for ingestion:

      * Python-native EL and reverse ETL
      * Built-in Ibis integration
      * Often used with dbt; works great with Kedro too
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Slide 12: Transformation with Kedro + Ibis

    * Kedro = modular Python pipeline framework (DAGs, catalogs)
    * Our contribution: native Ibis support in Kedro datasets
    * Model code as composable, reusable Python functions
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Slide 13: From SQL (dbt) to Python (Kedro + Ibis)

    **dbt example (Jinja):**

    ```sql
    {% for method in methods %}
    SUM(...) as {{ method }}_amount,
    {% endfor %}
    ```

    **Python + Ibis:**

    ```python
    for method in methods:
        sum_exprs[f"{method}_amount"] = ...
    ```

    * Cleaner, debuggable, IDE-friendly code
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Slide 14: Visualizing the Query Plan

    !\[IR Visualization]

    * Ibis constructs an intermediate representation (IR)
    * Lazily compiled to backend-specific SQL
    * Enables dev on DuckDB, prod on BigQuery/Snowflake
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Slide 15: Pandera for Data Validation

    * Originated for pandas; now supports Ibis
    * Declarative validation: types, ranges, uniqueness, etc.

    ```python
    import pandera as pa

    class Schema(pa.IbisSchemaModel):
        column: pa.typing.Series[int] = pa.Field(ge=0)
    ```

    * Custom checks in Ibis syntax
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Slide 16: BI & Analytics in Python

    * Ibis outputs → Streamlit, Plotly, ML workflows
    * Pandas compatibility where needed
    * Great fit for teams doing analytics + modelin
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Slide 17: Current Gaps & Limitations

    * Still new: some missing features (e.g. upserts in Ibis)
    * Ecosystem coordination needed (esp. orchestration)
    * Community integrations maturing (Kedro ↔ Pandera, Dagster)
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Slide 18: Why This Stack Works

    * Built organically to solve real user problems
    * Unified Python tooling = lower context switching
    * Composability = portability across engines
    * Python is no longer the fallback—it's the foundation
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Slide 19: Where to Learn More

    * Kedro + Ibis Jaffle Shop demo: \[GitHub link]
    * Ibis project: \[ibis-project.org]
    * dlt docs: \[dlthub.com]
    * Pandera docs: \[pandera.readthedocs.io]
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Slide 20: Thank You!

    **Questions?**
    Let’s build better data pipelines—in Python.
    """
    )
    return


if __name__ == "__main__":
    app.run()
