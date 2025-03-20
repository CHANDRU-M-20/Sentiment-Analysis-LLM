# Sentiment-Analysis-LLM
Sentiment-Analysis for Customer Review using Azure Service

# Sentiment Analysis for Customer Reviews

## Project Overview
This project performs **Sentiment Analysis** on customer reviews using **Azure Cognitive Services**. It provides functionalities to analyze text from customer feedback and convert **audio reviews into text** before performing sentiment analysis. The application is built using **Streamlit** for a user-friendly interface and utilizes **Azure Text Analytics API** to process and determine the sentiment of reviews.

## Features
- **Text Sentiment Analysis**: Enter customer reviews directly and analyze their sentiment.
- **Audio Sentiment Analysis**: Upload audio files, convert speech to text, and analyze the sentiment.
- **Bulk Sentiment Analysis**: Upload CSV files containing multiple reviews for batch processing.
- **Sentiment Score**: Get sentiment confidence scores for better analysis.
- **Data Visualization**: Generate charts and insights from sentiment analysis results.

## Technologies Used
- **Python**
- **Streamlit** (for UI)
- **Azure Cognitive Services**
  - **Azure Speech-to-Text**: Converts audio customer reviews into text.
  - **Azure Text Analytics API**: Performs sentiment analysis on text data.
- **Pandas** (for handling bulk review analysis)
- **Matplotlib & Seaborn** (for data visualization)
- **Dotenv** (for managing environment variables)

## How It Works
### 1. Text Analysis
- Enter a customer review manually in the text box.
- Click "Analyze" to process the sentiment using the **Azure Text Analytics API**.
- The output displays whether the sentiment is **positive, negative, or neutral**, along with a confidence score.

### 2. Audio Sentiment Analysis
- Upload an **MP3 or WAV** file.
- The **Azure Speech-to-Text API** converts the audio into text.
- The transcribed text is analyzed for sentiment using the **Azure Text Analytics API**.
- The sentiment and confidence score are displayed.

### 3. Bulk Review Analysis
- Upload a CSV file containing customer reviews.
- The application extracts the text and performs batch sentiment analysis.
- The results are displayed in a structured format with sentiment scores.
- Visualize sentiment distribution using bar charts and pie charts.

## Installation & Setup
### Prerequisites
- Python 3.8+
- Azure Subscription with **Azure Text Analytics API** and **Azure Speech-to-Text API** enabled.
- API Keys for Azure services.

### Installation Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/sentiment-analysis.git
   cd sentiment-analysis
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Create a **.env** file and add your Azure credentials:
   ```sh
   AZURE_LANGUAGE_ENDPOINT=<your_azure_endpoint>
   AZURE_LANGUAGE_KEY=<your_api_key>
   ```
4. Run the application:
   ```sh
   streamlit run app.py
   ```

## Usage
- **Navigate to the Streamlit UI**.
- **Choose a tab**: Text, Audio, or Bulk Analysis.
- **Upload a file or enter text**.
- **Click "Analyze"** to get the sentiment insights and scores.
- **View Visualizations**: Charts summarizing sentiment trends.

## Output Interpretation
- **Positive (Green)**: The review expresses positive sentiment.
- **Negative (Red)**: The review expresses negative sentiment.
- **Neutral (Blue)**: The review does not lean toward positive or negative.
- **Confidence Score**: Higher scores indicate stronger sentiment.

## Future Enhancements
- Add **multilingual support** for analyzing reviews in different languages.
- Implement **real-time streaming analysis** for live customer feedback.
- Enhance **visualizations** for sentiment trends using more advanced analytics.
- Deploy as a **cloud-based API** for integration with other applications.

