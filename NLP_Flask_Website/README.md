# Sentiment Analysis Web Application

This project implements a sentiment analysis web application using Flask. It provides two types of sentiment analysis:

* **Humor/Sci-Fi Classifier:** Predicts whether a given text is humorous or belongs to the science fiction genre.
* **Polarity/Subjectivity Analysis:** Determines the polarity (positive/negative) and subjectivity (intensity) of the sentiment expressed in the text.

## Libraries Used

* Flask
* scikit-learn
* spaCy
* pandas
* TextBlob

## Installation

1. Clone the repository:

    ```bash
    git clone [https://github.com/Prosper1kwo/NLP_Sentiment_Analysis/tree/main/NLP_Flask_Website](https://github.com/Prosper1kwo/NLP_Sentiment_Analysis/tree/main/NLP_Flask_Website)
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    ```bash
    # On Windows
    venv\Scripts\activate
    
    # On macOS/Linux
    source venv/bin/activate
    ```

4. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Navigate to the project directory:

    ```bash
    cd sentiment_analysis_project
    ```

2. Run the Flask application:

    ```bash
    python app.py
    ```

3. Open your web browser and go to `http://127.0.0.1:5000/` to access the application.

## Usage

1. Enter the text you want to analyze in the text area.
2. Select the type of sentiment analysis you want to perform from the dropdown menu.
3. Click the "Analyze" button.
4. The results of the analysis will be displayed below the form.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the Apache License - see the [LICENSE](https://github.com/Prosper1kwo/NLP_Sentiment_Analysis/blob/main/LICENSE) file for details.
