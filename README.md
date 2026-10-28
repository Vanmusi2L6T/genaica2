# Titanic Survival Prediction API

A machine learning project that predicts whether a passenger survived the Titanic disaster. This project demonstrates the complete machine learning workflow, from training a model in Google Colab to serving predictions through FastAPI and Docker, with automated testing using GitHub Actions.

## Project Overview

The goal of this project is to build and deploy a machine learning model through a REST API. It covers model training, model serialization, API development, containerization, automated testing, and continuous integration.

## Assignment Requirements Completed

### 1. Select a Machine Learning Case Study

Selected the Titanic Survival Prediction case study using the Titanic dataset.

### 2. Train and Test the Model

Trained and tested the machine learning model using Google Colab. The notebook contains the model training and data preprocessing workflow.

### 3. Save the Trained Model

Saved the trained machine learning model and its parameters in `model.joblib` for use in the API.

### 4. Build a Prediction API Using FastAPI

Developed a FastAPI application that accepts passenger information and returns a survival prediction and survival probability.

### 5. Execute the API Through Docker

Created a Docker image and ran the API inside a Docker container. Successfully tested the prediction endpoint through the containerized application.

### 6. Create a GitHub Repository

Created a GitHub repository and uploaded the project files.

Repository: [genaica2](https://github.com/Vanmusi2L6T/genaica2)

### 7. Create a GitHub Actions CI Pipeline

Configured a GitHub Actions workflow in `.github/workflows/ci.yml` to automate testing and Docker image building.

### 8. Verify Successful Pipeline Execution

Successfully executed the GitHub Actions workflow. The latest verified run showed all four tests passing and the Docker image building successfully.

## Technologies Used

- **Programming Language:** Python
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Notebook Environment:** Google Colab / Jupyter Notebook
- **API Framework:** FastAPI
- **Data Validation:** Pydantic
- **Testing:** Pytest
- **Containerization:** Docker
- **Version Control:** Git and GitHub
- **Continuous Integration:** GitHub Actions

## Project Structure

```text
genaica2/
├── main.py
├── model.joblib
├── requirements.txt
├── Dockerfile
├── README.md
├── titanic_model_training.ipynb
├── train.csv
├── tests/
│   └── test_api.py
└── .github/
    └── workflows/
        └── ci.yml
```

## Machine Learning Workflow

The machine learning pipeline follows these steps:

1. Load the Titanic training dataset.
2. Explore and preprocess the data.
3. Handle categorical features by converting them into numerical values.
4. Train and evaluate the machine learning model.
5. Save the trained model as `model.joblib`.
6. Load the saved model into the FastAPI application.
7. Accept passenger information through the prediction endpoint.
8. Return the predicted survival class and survival probability.

The `titanic_model_training.ipynb` notebook contains the model training workflow, while `train.csv` contains the training dataset.

## API Features

- Accepts passenger information through a REST API.
- Converts supported categorical inputs into numerical values.
- Generates a survival prediction.
- Returns the estimated survival probability.
- Provides interactive API documentation through Swagger UI.

### Prediction Endpoint

**Method:** `POST`

**Endpoint:** `/predict`

### Example Response

```json
{
  "survived": 0,
  "result": "Did not survive",
  "survival_probability": 0.09
}
```

This is an example response from the API.

## Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Vanmusi2L6T/genaica2.git
cd genaica2
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment on Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the FastAPI Server

```bash
uvicorn main:app --reload
```

### 6. Open the API Documentation

Visit the following address in your browser:

http://127.0.0.1:8000/docs

Use Swagger UI to send a request to the `/predict` endpoint and inspect the response.

## Run the Project Using Docker

### 1. Build the Docker Image

```bash
docker build -t titanic-survival-api .
```

### 2. Run the Docker Container

```bash
docker run --name titanic-api -p 8000:8000 titanic-survival-api
```

If a container named `titanic-api` already exists, remove it first:

```bash
docker rm -f titanic-api
```

Then run the Docker container command again.

### 3. Test the Containerized API

Open the following address:

http://127.0.0.1:8000/docs

Use the Swagger interface to test the prediction endpoint.

## Automated Testing

The project uses Pytest to test the API and its prediction functionality.

Run the tests locally using:

```bash
python -m pytest -v
```

**Verified result:** All four tests passed during the last verified local test run.

## GitHub Actions CI Pipeline

The GitHub Actions workflow is located at:

`.github/workflows/ci.yml`

The workflow automates the testing and Docker image building process when changes are pushed to the repository.

### CI Workflow Steps

1. Set up the Python environment.
2. Install the required dependencies.
3. Execute automated tests using Pytest.
4. Build the Docker image.
5. Report the workflow status on GitHub.

**Verified result:** The last verified workflow run completed successfully, with all four tests passing and the Docker image building successfully.

You can view the workflow runs in the repository's **Actions** tab.

## Repository

GitHub Repository: https://github.com/Vanmusi2L6T/genaica2

## Learning Outcomes

Through this project, I gained practical experience in:

- Training and testing a machine learning model.
- Preprocessing data and encoding categorical features.
- Saving and loading a trained model using Joblib.
- Building REST APIs with FastAPI.
- Integrating a machine learning model with a backend application.
- Containerizing an application using Docker.
- Writing automated tests using Pytest.
- Creating a continuous integration pipeline using GitHub Actions.
- Managing and publishing source code using Git and GitHub.

