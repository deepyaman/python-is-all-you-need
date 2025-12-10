import marimo

__generated_with = "0.14.17"
app = marimo.App(
    width="medium",
    layout_file="layouts/presentation.slides.json",
)


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Python is all you need: an overview of the<br/>composable, Python-native data stack

    Deepyaman Datta · PyData Boston 2025 · December 10, 2025
    """
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"## Why should _you_ care?"),
            mo.image(
                "public/ai-hierarchy-of-needs.avif",
                height=600,
                caption='Source: <a href="https://hackernoon.com/the-ai-hierarchy-of-needs-18f111fcc007">The AI Hierarchy of Needs (Rogati, 2017)</a>',
            ),
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
                r"""
    ## What is the modern data stack?

    > [a set of products that a) redesigned the analytics workflow to take advantage of the cloud and b) all interacted with one another via SQL](https://roundup.getdbt.com/p/is-the-modern-data-stack-still-a)
    """
            ),
            ax,
        ]
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(
                r"""
    ## ELT vs ETL

    * ETL: transform before loading into the warehouse
    * ELT: load first, then transform inside the warehouse
    """
            ),
            mo.image(
                "public/etl-vs-elt.png",
                caption='Source: <a href="https://www.fivetran.com/blog/etl-vs-elt">ETL vs. ELT (Wang, 2022)</a>',
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(
                r"""
    ## [The modern data stack as we know it](https://www.linkedin.com/pulse/what-steps-tools-setting-up-modern-saas-based-bi-tristan-handy/) (circa 2016)

    * **Ingestion**: Fivetran, Stitch
    * **Storage**: Bigquery, Databricks, Redshift, Snowflake
    * **Transformation**: dbt
    * **BI**: Looker, Mode, Periscope, Chartio, Metabase, Redash
    """
            ),
            mo.image(
                "public/dbt-wau.png",
                width=1200,
                caption='Source: <a href="https://www.getdbt.com/blog/next-layer-of-the-modern-data-stack">The next layer of the modern data stack (Handy, 2024)</a>',
            ),
        ],
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"## What about Python?"),
            mo.hstack(
                [
                    mo.md(
                        r"""
    * Python now rivals SQL in developer popularity
    * Second-class support in the modern data stack
        * Still seen as the fallback option for complex cases
    * Python-first data pipelines couldn't scale*
    """
                    ),
                    # TODO(deepyaman): Replace with https://altair-viz.github.io/gallery/bump_chart.html
                    mo.image(
                        "public/top-programming-languages.png",
                        width=450,
                        caption='Source: <a href="https://github.blog/news-insights/octoverse/octoverse-2024/">Octoverse (GitHub Staff, 2024)</a>',
                    ),
                ],
                gap=2.25,
                widths="equal",
            ),
        ],
        gap=2.25,
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(
                r"""
    ## Enter the bird

    * **Ibis**: a lightweight Python library for data wrangling
    * Provides:
        * Pythonic dataframe API
        * Interfaces to 20+ query languages
        * Deferred execution model
    * Enables language interoperability
    """
            ),
            mo.hstack(
                [
                    mo.md(
                        r"""
    ```python
    t.filter(t.a > 1).select("a", "b", "c")
    ```
    """
                    ),
                    mo.md(r"$\equiv$"),
                    mo.md(
                        r"""
    ```sql
    SELECT a, b, c FROM t WHERE a > 1
    ```
    """
                    ),
                ],
                justify="center",
                align="center",
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(
                r"## [Fundamental components of any data stack](https://www.ibm.com/think/topics/modern-data-stack)"
            ),
            mo.hstack(
                [
                    mo.md(
                        r"""
    * Data storage
    * Data ingestion
    * Data transformation
    * BI and analytics
    * Data observability
    """
                    ),
                    mo.image(
                        "public/data-engineering-lifecycle.png",
                        caption='Source: <a href="https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/ch02.html#components_and_undercurrents_of_the_dat">Fundamentals of Data Engineering (Reis and Housley, 2022)</a>',
                    ),
                ]
            ),
        ],
        gap=2.25,
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Data storage

    * **Data warehouses**: Ibis supports most common data warehouse providers (e.g. Snowflake, Databricks, BigQuery) as backends
    * **Data lakes**: Ibis supports Parquet, CSV, JSON, and more depending on the backend
    * **Data lakehouses**: Ibis supports Delta; Iceberg supported by some backends
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Data ingestion

    * **dlt**: open-source, Python-native EL (and Reverse ETL)
    * Features:
        * Loads data from [REST APIs](https://dlthub.com/docs/tutorial/rest-api), [SQL databases](https://dlthub.com/docs/tutorial/sql-database), [cloud storage](https://dlthub.com/docs/tutorial/filesystem), [Python data structures](https://dlthub.com/docs/tutorial/load-data-from-an-api), and [more](https://dlthub.com/docs/dlt-ecosystem/verified-sources)
        * Supports a variety of [popular destinations](https://dlthub.com/docs/dlt-ecosystem/destinations/)
        * Also supports [Reverse ETL](https://dlthub.com/blog/reverse-etl-dlt)
        * Built-in [Ibis integration](https://dlthub.com/docs/general-usage/dataset-access/ibis-backend)
    * Proven part of the modern data stack
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## dlt example

    ```python
    import dlt
    from dlt.sources.filesystem import filesystem, read_csv

    files = filesystem(bucket_url="gs://filesystem-tutorial", file_glob="encounters*.csv")
    reader = (files | read_csv()).with_name("encounters")
    pipeline = dlt.pipeline(
        pipeline_name="hospital_data_pipeline",
        dataset_name="hospital_data",
        destination="duckdb",
    )

    info = pipeline.run(reader)
    print(info)
    ```
    """
    )
    return


@app.cell
def _(mo):
    mo.hstack(
        [
            mo.md(
                r"""
    ## Data transformation

    * **Kedro**: an open-source Python framework for building reproducible, maintainable, modular data pipelines
    * Features:
        * Nodes are vanilla Python functions
        * [Native support for reading and writing Ibis tables using Kedro-Datasets](https://kedro.org/blog/building-scalable-data-pipelines-with-kedro-and-ibis)
        * [Extensible by design](https://docs.kedro.org/en/0.19.14/extend_kedro/plugins.html)
        * Graduate-stage project of the LF AI & Data Foundation
    """
            ),
            mo.md(
                r"""
    > "When I learned about Kedro (while at dbt Labs), I commented that it was like dbt if it were created by Python data scientists instead of SQL data analysts (including both being created out of consulting companies)."

    <div style="font-size: 0.75em; text-align: right;">— Cody Peterson, Product Manager @ Ascend.io</div>
    """
            ),
        ],
        align="center",
        gap=2.25,
        widths="equal",
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## From SQL (dbt) to Python (Kedro + Ibis)

    **SQL (using Jinja):**

    ```sql
    {% set payment_methods = ['credit_card', 'coupon', 'bank_transfer', 'gift_card'] %}

    ...

    {% for payment_method in payment_methods %}
    sum(...) as {{ payment_method }}_amount,
    {% endfor %}
    ```

    **Python (using Ibis):**

    ```python
    payment_methods = ["credit_card", "coupon", "bank_transfer", "gift_card"]

    ...

    total_amount_by_payment_method = {}
    for payment_method in payment_methods:
        total_amount_by_payment_method[f"{payment_method}_amount"] = ...
    ```
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Data validation

    * **Pandera**: the open-source framework for validating Python dataframes
    * Supports:
        * pandas, Dask, Modin, PySpark, and now... Ibis!
        * Built-in checks for common validation tasks
        * Custom checks in Ibis syntax
        * Integrations with other tools in the Python ecosystem
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Pandera example

    ```python
    def total_amount_positive(data: IbisData) -> ibis.Table:
        w = ibis.window(group_by="order_id")
        with_total_amount = data.table.mutate(total_amount=data.table.amount.sum().over(w))
        return with_total_amount.order_by("order_id").select(_.total_amount >= 0)


    schema = pa.DataFrameSchema(
        columns={
            "order_id": pa.Column(int),
            "amount": pa.Column(float),
            "status": pa.Column(
                str,
                pa.Check.isin(
                    ["placed", "shipped", "completed", "returned", "return_pending"]
                ),
            ),
        },
        checks=[pa.Check(total_amount_positive)],
    )
    ```
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## BI and analytics

    * [Ibis supports the Streamlit `connection()` interface](https://ibis-project.org/how-to/visualization/streamlit)
    * It can also be used with most other data visualization libraries
        * pandas/Polars interoperability where needed
    * Developing integration with the Boring Semantic Layer
    * Great fit for teams doing analytics and modeling
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Kedro Semantic Layer example

    ```yaml
    orders:
      type: ibis.TableDataset
      table_name: orders
      connection: ${_duckdb}
      save_args:
        materialized: table
      metadata:
        kedro-semantic-layer:
          description: "Order fact table. This table is at the order grain with one row per order."

          dimensions:
            order_date:
              expr: _.order_date
              is_event_timestamp: True
              smallest_time_grain: "day"
            status: _.status

          measures:
            order_total:
              expr: _.amount.sum()
              description: "Sum of total order amount."
            order_count:
              expr: _.count()
              description: "Count of orders."
    ```
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Current gaps and limitations

    * Still new: some missing features (e.g. upserts in Ibis)
    * Community integrations maturing (Kedro-Pandera, orchestrators, OpenLineage)
    * Real-world examples
    * Awareness
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Why this stack works

    * Built organically to solve real user problems
    * Unified Python tooling = lower context switching
    * Solid fundamentals: based on composable, open standards
    * Python is no longer the fallback—it's the foundation
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Where to learn more

    **Let's build better data pipelines—in Python.**

    * Tools we talked about
        * Ibis: https://ibis-project.org/
        * Kedro: https://kedro.org/
        * Pandera + Ibis: https://pandera.readthedocs.io/en/latest/ibis.html
        * dlt: https://dlthub.com/docs/intro
        * Boring Semantic Layer: https://boringdata.github.io/boring-semantic-layer/
    * Putting it all together
        * Jaffle Shop demo: https://github.com/deepyaman/jaffle-shop/tree/jaffle-stack
        * Kedro + Ibis: https://kedro.org/blog/building-scalable-data-pipelines-with-kedro-and-ibis
        * Kedro + Ibis tutorial: https://www.youtube.com/watch?v=ffDHdtz_vKc
        * Kedro + Boring Semantic Layer: https://github.com/deepyaman/kedro-semantic-layer
    * Dive deeper
        * Does Ibis understand SQL? https://ibis-project.org/posts/does-ibis-understand-sql/
    """
    )
    return


if __name__ == "__main__":
    app.run()
