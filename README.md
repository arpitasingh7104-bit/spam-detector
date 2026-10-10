# Spam Message Detector

## Abstract
Unwanted spam messages waste time and expose people to scams and phishing links. This project presents a simple spam message detector built with Python and scikit-learn. Messages are converted into numerical features using TF-IDF, and a Multinomial Naive Bayes classifier is trained to label each message as spam or not spam. The model is trained on a small labelled dataset of 151 messages and evaluated on a held-out 20% test set, where it reached 100% accuracy. Because the dataset is small and similar in style, this result should be read as a proof of concept rather than real-world performance. A Gradio web interface lets users paste any message and instantly see the prediction with a confidence score. The project shows that a lightweight, fast and free machine learning pipeline can effectively flag spam without any paid API.

## Tech Stack
- Python
- scikit-learn (TF-IDF + Naive Bayes)
- pandas, joblib
- Gradio (web UI)

## Setup

1. Clone this repo

```bash
git clone https://github.com/arpitasingh7104-bit/spam-detector.git
cd spam-detector
```

2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. (Optional) Regenerate the dataset and retrain

```bash
python make_data.py
python train.py
```

5. Run the app

```bash
python app.py
```

## Files
- `make_data.py` creates the dataset (`spam.csv`)
- `train.py` trains and evaluates the model
- `app.py` runs the Gradio app