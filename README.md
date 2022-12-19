# Emotion vs. Category in Books

Topics: Sentence Transformers, Apache Spark

## Abstract

A book's description often serves as a "hook" to entice the reader and preview its ambiance.  Examining how the emotional content of this description relates to the book's tagged categories may prove of interest for book recommendations, classification, etc. This project uses inferred sentence emotion from NLP transformer models along with Apache Spark's parallelism to chart this relationship in [over a million books](https://www.kaggle.com/datasets/sp1thas/book-depository-dataset) listed on [Book Depository](https://www.bookdepository.com/).

## Quick Start

### Browsing results

Visualizations, methodology, etc. are viewable as cell outputs and markdown in the Jupyter notebooks below:

| Order | File name (linked) | Description
:-: | :-- | :--
1 | [Data Wrangling](1-data-wrangling.ipynb) | Retrieving the [dataset](https://www.kaggle.com/datasets/sp1thas/book-depository-dataset) and cleaning before analysis.
2 | [Data Inspection](2-data-inspection.ipynb) | Assessing data characteristics / composition.
| | [Utilities](_utils.py) | General functions & constants used throughout the project.

### Running the project

Included Jupyter notebooks use the default IPython kernel for Python 3, so the included installs should be sufficient.

Using [this Docker image](https://github.com/jupyter/docker-stacks/tree/main/all-spark-notebook) is recommended, as it supports Apache Spark in Jupyter notebooks.  To do so, run this command from the project directory:

```
docker run --rm -p 4040:4040 -p 8888:8888 -v $(pwd):/home/jovyan/work jupyter/all-spark-notebook
```