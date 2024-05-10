
# AutoSeg - Segment and Classify your images

## Introduction

Welcome to AutoSeg! This Python application facilitates automatic image segmentation leveraging cutting-edge machine learning models. This is intended to automate the data annotation in images to some extent.

## Prerequisites

Before you begin, ensure you have Python installed on your system. This project is tested with Python 3.8+. You can download Python from [python.org](https://www.python.org/downloads/).

## Repository Contents

* **app.py**: The main application file where the segmentation logic is implemented.
* **requirements.txt**: Lists all dependencies required to run the application.
* **README.md**: This file, which provides installation and usage instructions.

## Installation Guide

### 1. Clone the Repository

First, clone the repository to your local machine. Open your terminal and run the following command:

```python
git clone [https://github.com/taherpat/AutoSeg.git](https://github.com/taherpat/AutoSeg.git)
cd AutoSeg
```

2. Set Up a Virtual Environment (Optional)
It's a good practice to use a virtual environment for Python projects. This keeps your dependencies organized and isolated. To set up a virtual environment, run:

```python
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

3. Install Required Packages
Install all required packages using the requirements.txt file:

```python
pip install -r requirements.txt
```

4. Download Model Checkpoints
The application requires specific model checkpoints to function. Download these files using the following commands:

```pythonh
wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth
wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_l_0b3195.pth
wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth
```

Please ensure these files are placed in the directory expected by the application. You may need to adjust the paths in app.py accordingly.

5. Running the Application
With the dependencies installed and model checkpoints in place, you're ready to run the application:

```python
python app.py
```
##Usage Tips
Adjust the paths to the model files in app.py if you store them in a different directory.
Use high-quality images for better segmentation results.
###Contributing
We welcome contributions to AutoSeg! If you have suggestions or improvements, please fork the repository and submit a pull request.
