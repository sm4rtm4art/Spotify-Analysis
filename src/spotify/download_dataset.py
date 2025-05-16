"""
Script to download and explore the 900k+ Spotify dataset.
"""
from pathlib import Path
import os
import shutil
from typing import List, Optional, Union, Dict, Any

import kagglehub
import pandas as pd


def download_spotify_dataset(output_dir: str = None) -> pd.DataFrame:
    """
    Download the 900k-spotify dataset from Kaggle.
    
    Args:
        output_dir: Directory to save the data files. If None, will use the 'data' 
                   directory in the project root.
    
    Returns:
        pd.DataFrame: The downloaded dataset
        
    Raises:
        Exception: If there's an issue downloading or accessing the dataset
    """
    print("Downloading the Spotify dataset...")
    
    # Set up output directory
    if output_dir is None:
        # Get the project root directory (two levels up from this file)
        project_root = Path(__file__).resolve().parent.parent.parent
        output_dir = project_root / "data"
    else:
        output_dir = Path(output_dir)
    
    # Create data directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Using data directory: {output_dir}")
    
    try:
        # First download the dataset files
        print("Downloading the dataset from Kaggle...")
        dataset_path = kagglehub.dataset_download("devdope/900k-spotify")
        print(f"Dataset downloaded to: {dataset_path}")
        
        # Look for CSV files in the downloaded dataset
        csv_files = list(Path(dataset_path).glob("*.csv"))
        if not csv_files:
            raise FileNotFoundError("No CSV files found in the downloaded dataset")
        
        # Load the first CSV file found (or you can specify which one to load)
        first_csv = csv_files[0]
        print(f"Loading data from: {first_csv}")
        df = pd.read_csv(first_csv)
        
        # Copy the original CSV to our data directory for reference
        source_file = str(first_csv)
        dest_file = str(output_dir / "spotify_dataset_original.csv")
        print(f"Copying original dataset to: {dest_file}")
        shutil.copy2(source_file, dest_file)
        
        print(f"Dataset loaded with {len(df)} rows and {df.shape[1]} columns")
        return df
    except Exception as e:
        print(f"Error downloading dataset: {e}")
        raise


def save_dataset(df: pd.DataFrame, output_path: str = None, format: str = "csv") -> str:
    """
    Save the dataset to the specified format for faster loading.
    
    Args:
        df: The dataset to save
        output_path: Path where to save the dataset. If None, will use a default
                    in the project root.
        format: Format to save the data in ('csv' or 'parquet')
    
    Returns:
        str: Path where the dataset was saved
        
    Raises:
        IOError: If there's an issue saving the file
    """
    if output_path is None:
        # Get the project root directory (two levels up from this file)
        project_root = Path(__file__).resolve().parent.parent.parent
        if format.lower() == "parquet":
            output_path = str(project_root / "data" / "spotify_dataset.parquet")
        else:
            output_path = str(project_root / "data" / "spotify_dataset.csv")
    
    print(f"Saving dataset to {output_path}...")
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Save in the appropriate format
        if format.lower() == "parquet":
            try:
                df.to_parquet(output_path)
            except ImportError:
                print("Warning: Could not save as parquet (pyarrow not available). Saving as CSV instead.")
                output_path = output_path.replace(".parquet", ".csv")
                df.to_csv(output_path, index=False)
        else:
            df.to_csv(output_path, index=False)
            
        print(f"Dataset saved to {output_path}")
        return output_path
    except Exception as e:
        print(f"Error saving dataset: {e}")
        raise


def explore_dataset(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Perform a basic exploration of the dataset.
    
    Args:
        df: The dataset to explore
        
    Returns:
        Dict[str, Any]: A dictionary containing summary statistics and information
    """
    print("\n--- Dataset Overview ---")
    print(f"Shape: {df.shape}")
    print("\nFirst 5 rows:")
    print(df.head())
    
    print("\nColumns:")
    print(df.columns.tolist())
    
    print("\nData types:")
    print(df.dtypes)
    
    print("\nMissing values:")
    missing_values = df.isna().sum()
    print(missing_values)
    
    print("\nBasic statistics:")
    numeric_cols = df.select_dtypes(include=['number']).columns
    stats = df[numeric_cols].describe()
    print(stats)
    
    # Return a dictionary with all the analysis information
    return {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes,
        "missing_values": missing_values,
        "stats": stats
    }


if __name__ == "__main__":
    # Download and load the dataset
    df = download_spotify_dataset()
    
    # Save for faster loading in the future (use CSV by default)
    saved_path = save_dataset(df, format="csv")
    
    # Explore the dataset
    explore_dataset(df)
    
    print(f"\nDataset download and exploration complete! Data saved to: {saved_path}") 