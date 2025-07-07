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
    ## Python is all you need: an overview of the<br/>composable, Python-native data stack

    Deepyaman Datta · SciPy 2025 · July 9, 2025
    """
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md("## Why should _you_ care?"),
            mo.image("public/ai-hierarchy-of-needs.avif", height=600),
        ]
    )
    return


@app.cell
def _(mo):
    # https://dadoverflow.com/2021/08/17/making-timelines-with-python/
    from datetime import date

    import matplotlib.pyplot as plt
    import numpy as np

    labels, dates = zip(
        *[
            ("Chartio", date(2010, 6, 1)),
            ("Looker", date(2011, 8, 1)),
            ("Google BigQuery", date(2011, 11, 1)),
            ("Periscope", date(2012, 1, 1)),
            ("Amazon Redshift", date(2013, 2, 1)),
            ("Fivetran", date(2013, 3, 1)),
            ("Mode", date(2013, 10, 1)),
            ("Snowflake", date(2014, 10, 1)),
            ("Metabase", date(2014, 11, 1)),
            ("Redash", date(2015, 12, 1)),
            ("dbt", date(2016, 3, 1)),
            ("Stitch", date(2016, 8, 1)),
        ]
    )

    min_date = date(np.min(dates).year - 1, np.min(dates).month, np.min(dates).day)
    max_date = date(np.max(dates).year + 1, np.max(dates).month, np.max(dates).day)

    fig, ax = plt.subplots(figsize=(15, 4), constrained_layout=True)
    _ = ax.set_ylim(-2, 1.75)
    _ = ax.set_xlim(min_date, max_date)
    _ = ax.axhline(0, xmin=0.05, xmax=0.95, c="deeppink", zorder=1)

    _ = ax.scatter(dates, np.zeros(len(dates)), s=120, c="palevioletred", zorder=2)
    _ = ax.scatter(dates, np.zeros(len(dates)), s=30, c="darkmagenta", zorder=3)

    label_offsets = np.zeros(len(dates))
    label_offsets[::2] = 0.35
    label_offsets[1::2] = -0.5
    for i, (l, d) in enumerate(zip(labels, dates)):
        _ = ax.text(
            d,
            label_offsets[i],
            l,
            ha="center",
            fontfamily="serif",
            fontweight=(
                "bold"
                if l in ["Google BigQuery", "Amazon Redshift", "Snowflake"]
                else "normal"
            ),
            color="royalblue",
            fontsize=12,
        )

    stems = np.zeros(len(dates))
    stems[::2] = 0.3
    stems[1::2] = -0.3
    markerline, stemline, baseline = ax.stem(dates, stems)
    _ = plt.setp(markerline, marker=",", color="darkmagenta")
    _ = plt.setp(stemline, color="darkmagenta")

    # hide lines around chart
    for spine in ["left", "top", "right", "bottom"]:
        _ = ax.spines[spine].set_visible(False)

    # hide tick labels
    _ = ax.set_yticks([])

    mo.vstack(
        [
            mo.md(
                """## What is the modern data stack?

    > [a set of products that a) redesigned the analytics workflow to take advantage of the cloud and b) all interacted with one another via SQL](https://roundup.getdbt.com/p/is-the-modern-data-stack-still-a)"""
            ),
            ax,
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## ELT vs ETL

    * ETL: transform before loading into the warehouse
    * ELT: load first, then transform inside the warehouse

    ![](public/etl-vs-elt.png)
    """
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md("""## [The modern data stack as we know it](https://www.linkedin.com/pulse/what-steps-tools-setting-up-modern-saas-based-bi-tristan-handy/) (circa 2016)

    * **Ingestion**: Fivetran, Stitch
    * **Storage**: Bigquery, Databricks, Redshift, Snowflake
    * **Transformation**: dbt
    * **BI**: Looker, Mode, Periscope, Chartio, Metabase, Redash"""),
            mo.image("public/dbt-wau.png", width=1200),
        ]
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(
                """## What about Python?

    * Python now rivals SQL in developer popularity
    * Second-class support in the modern data stack
        * Still seen as the fallback option for complex cases
    * Python-first data pipelines couldn't scale*"""
            ),
            mo.image("public/top-programming-languages.png"),  # TODO(deepyaman): Replace with https://altair-viz.github.io/gallery/bump_chart.html
        ]
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
    * Enables language interoperability
        * 
          ```python
          t.filter(t.a > 1).select("a", "b", "c")
          ```
          is equivalent to
          ```sql
          SELECT a, b, c FROM t WHERE a > 1
          ```
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
