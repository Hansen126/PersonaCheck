# 🎭 PersonaCheck: AI Personality Checker

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/) [![Django](https://img.shields.io/badge/Django-3.x-green.svg)](https://www.djangoproject.com/) [![scikit-learn](https://img.shields.io/badge/scikit--learn-0.24-orange.svg)](https://scikit-learn.org/)

## 📖 Project Overview

**PersonaCheck** is an AI-powered personality prediction website built with Django. The tool uses **machine learning** to classify users' MBTI (Myers-Briggs Type Indicator) personality types based on textual input. Simply enter a brief description of yourself or your behavior, and PersonaCheck will predict your MBTI type in seconds! 

This project leverages the **LinearSVC** model (Support Vector Classifier) with **TF-IDF vectorization** for text classification. It provides a fast, fun, and insightful way to explore personality traits.

---

## 🎯 Features

- **MBTI Personality Prediction**: Enter your description, and PersonaCheck predicts one of the 16 MBTI types.
- **Machine Learning Model**: LinearSVC provides fast and accurate personality predictions.
- **Minimalist UI**: Simple and clean user interface for easy interaction.
- **No Database Needed**: Instant predictions without the need for persistent storage.
  
---

## ⚙️ Technologies Used

- **Backend**: [Django](https://www.djangoproject.com/) (Python Web Framework)
- **Machine Learning**: [scikit-learn](https://scikit-learn.org/) (TF-IDF Vectorizer, LinearSVC)
- **Frontend**: HTML, CSS
- **Database**: Not required (no persistent data storage)

---

## 🚀 Getting Started

Follow the instructions below to get this project up and running on your local machine.

### Prerequisites

- Python 3.7+
- Django 3.x
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-github-username>/PersonaCheck.git

2. **Navigate to the project directory:**:
   ```bash
   cd PersonaCheck

3. **Set up a virtual environment (recommended):**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac:
   source venv/bin/activate

4. **Install the required dependencies:**:
   ```bash
   pip install -r requirements.txt

5. **Run migrations (if required):**:
   ```bash
   python manage.py migrate

6. **Run the development server:**:
   ```bash
   python manage.py runserver

7. **Open the website in your browser:**:
   ```bash
   http://127.0.0.1:8000/

## 🧠 Machine Learning Model

PersonaCheck uses **LinearSVC** (Linear Support Vector Classifier) for personality prediction:

- **TF-IDF Vectorization**: Converts input text into numerical features based on word frequency, adjusted for how important a word is across the dataset.
- **LinearSVC**: A powerful classification model that finds the hyperplane to separate text features and predicts the correct MBTI type.

### Why LinearSVC?

LinearSVC was chosen because of its:
- **Efficiency**: It's fast and scalable for text classification tasks.
- **Accuracy**: It provides robust predictions by capturing complex patterns in text data.
  
---

## 🛠 How it Works

1. **User Input**: The user enters a description of themselves or their behavior.
2. **Text Processing**: The input is vectorized using a **TF-IDF vectorizer**.
3. **Prediction**: The **LinearSVC model** predicts the MBTI personality type based on the processed text.
4. **Output**: The predicted personality type is displayed on the results page.

---

## 📊 Example Predictions

Here are some example inputs and their predicted MBTI types using **LinearSVC**:

| Input Text | Predicted MBTI Type |
|------------|---------------------|
| "I enjoy spending time alone, analyzing situations deeply." | INTP |
| "I love organizing events and leading teams." | ENTJ |
| "I'm always the one trying to make people laugh in social situations." | ENFP |
| "I prefer staying in and reading rather than going to parties." | ISFJ |

---

## 📈 Future Improvements

- **Model Tuning**: Explore hyperparameter tuning to further improve accuracy.
- **Add More Models**: Experiment with alternative classifiers like Random Forests or deep learning models for improved performance.
- **REST API**: Integrate a REST API to allow developers to use personality prediction in their own applications.
- **User Profiles**: Optionally allow users to save and track their personality predictions over time (with database integration).

---

## 💡 Inspiration

This project was inspired by the growing interest in personality types and how AI and machine learning can help predict human traits based on language. The MBTI framework is widely used in personal development and team building, making it an interesting area to explore with AI.

---

## 👨‍💻 Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

---


## 📬 Contact

For any questions or suggestions, feel free to reach out:

- **GitHub**: [Hansen126](https://github.com/Hansen126)
- **Email**: hansen126187@gmail.com
