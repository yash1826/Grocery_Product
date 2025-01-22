# Grocery Product Detection and Classification

## Project Overview
This project aims to train a model to detect and classify various grocery products using images. The dataset used for training and evaluation is sourced from the [Grocery Store Dataset](https://github.com/marcusklasson/GroceryStoreDataset/tree/master/dataset). The project is designed for smart checkout systems or inventory management applications.

## Dataset
The dataset consists of images of various grocery products, organized into different categories. You can find the dataset on GitHub in the following [Grocery Store Dataset link](https://github.com/marcusklasson/GroceryStoreDataset/tree/master/dataset).

### Dataset Structure:
- `train/`: Contains images for training the model.
- `val/`: Contains images for validating the model.
- `test/`: Contains images for testing the model.

Each folder contains images classified into various grocery product categories.

## Requirements

- Python 3.x
- YOLOv5
- PyTorch
- OpenCV
- Matplotlib
- Pandas
- NumPy

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
