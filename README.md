# Spotify Song Analysis: A Data Science Journey 🎵

Welcome to this exciting data science project where we dive deep into the world of music through the lens of the [900k Spotify Songs Dataset](https://www.kaggle.com/datasets/devdope/900k-spotify)! This project aims to uncover insights, patterns, and perhaps even predict song characteristics using a rich dataset featuring nearly a million tracks.

## About the Dataset

The dataset provides a wealth of information for over 900,000 songs, including:

- **Core Song Attributes:** Title, Artist(s), Album, Release Date, Genre.
- **Audio Features (from Spotify API):** Popularity, Energy, Danceability, Positiveness (Valence), Speechiness, Liveness, Acousticness, Instrumentalness, Tempo, Loudness.
- **Lyrical Content:** Full song lyrics (`text`).
- **Emotional Tags:** Categorized emotions based on lyrics.
- **Contextual Tags:** Suitability for various activities (Party, Work/Study, Relaxation, Exercise, etc.).
- **Similarity Metrics:** Information on similar songs and artists.

This comprehensive collection allows for a multifaceted analysis, from exploring trends in audio features across genres to understanding lyrical sentiment and song context.

## Project Goals 🚀

This project is an exploratory and learning endeavor. Our primary objectives include:

1.  **Thorough Exploratory Data Analysis (EDA):**
    - Understanding data distributions and identifying outliers.
    - Visualizing relationships between different song features.
    - Investigating trends in music across genres, time, and popularity.
    - Analyzing lyrical content and its connection to emotion and audio features.
2.  **Data Cleaning and Preprocessing:**
    - Handling missing values and inconsistencies.
    - Transforming features into suitable formats for analysis and modeling.
3.  **(Potential) Predictive Modeling:**
    - Building models to predict song popularity.
    - Exploring genre classification based on audio features or lyrics.
    - Investigating other interesting predictive tasks.
4.  **Clean Code & Reproducibility:**
    - Employing best practices in Python programming.
    - Ensuring the analysis is reproducible using `uv` for environment management.

## Tools & Technologies

- **Python:** The core programming language.
- **uv:** For lightning-fast Python packaging and environment management. It's used to create virtual environments, install dependencies defined in `pyproject.toml`, and ensure reproducible builds.
- **Polars (& Pandas):** For efficient data manipulation and analysis.
- **NumPy:** For numerical operations.
- **Matplotlib & Seaborn:** For data visualization.
- **YData-Profiling:** For generating detailed EDA reports.
- **Scikit-learn:** For machine learning tasks.
- **KaggleHub:** For programmatic dataset access.
- **Ruff:** For linting and formatting, ensuring clean code.

## Getting Started

1.  **Install `uv` (if you haven't already):**
    `uv` is a fast Python package installer and resolver, written in Rust. You can install it using pip, or by following the instructions on the [official `uv` documentation](https://github.com/astral-sh/uv#installation).

    ```bash
    # Example using pip (ensure pip is for Python 3.7+)
    pip install uv
    ```

    Or via curl/powershell:

    ```bash
    # macOS and Linux
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # Windows
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

2.  **Clone the repository (if applicable).**

    ```bash
    # git clone <repository-url>
    # cd <repository-name>
    ```

3.  **Set up the project environment using `uv`:**
    This project uses `uv` to manage its virtual environment and dependencies, as defined in `pyproject.toml`.

    ```bash
    # Create the virtual environment (if it doesn't exist) and sync dependencies
    uv sync
    ```

    This command reads the `pyproject.toml` (and `uv.lock` if present), creates a virtual environment (typically `.venv` in the project root), and installs all necessary packages.

4.  **Activate the virtual environment:**

    ```bash
    # On macOS and Linux
    source .venv/bin/activate
    # On Windows (Powershell)
    .venv\\Scripts\\Activate.ps1
    # On Windows (CMD)
    .venv\\Scripts\\activate.bat
    ```

    Your terminal prompt should now indicate that you are in the `.venv` environment.

5.  **Download the data:** The dataset can be downloaded using the `kagglehub` library. A script or notebook will be provided within the `notebooks` or `scripts` directory for this purpose. (We'll add this part soon!)

6.  **Explore the notebooks and scripts!**
    You'll likely find these in a `notebooks/` or `scripts/` directory.

**Basic `uv` usage for this project:**

- `uv sync`: Installs/updates dependencies according to `pyproject.toml` and `uv.lock`. Run this after pulling new changes.
- `uv add <package_name>`: Adds a new package to your `pyproject.toml` and installs it.
- `uv run <command>`: Runs a command within the project's virtual environment.

Let's unlock the stories hidden within these 900,000 songs!
