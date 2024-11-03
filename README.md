# Query-Link-Bot

LinkWise AI is a web-based question-answering bot that takes a website URL as input, scrapes the data from that site, and allows users to ask questions related to the content scraped. This project utilizes Flask for the backend and Hugging Face Transformers for natural language processing.

## Features

- Enter a website URL and a question related to that website.
- The bot scrapes the website for content and uses a trained model to provide answers.
- Simple and user-friendly interface.

## Requirements

- Python 3.x
- Flask
- Beautiful Soup
- Requests
- Hugging Face Transformers
- Other dependencies as specified in `requirements.txt`

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/querybot.git
   cd querybot
2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install the required packages**:
   ```bash
    pip install -r requirements.txt

## Running the project

1. **Run the Flask application**:
   ```bash
        python app.py
2.**Access the web application**: Open your web browser and go to http://127.0.0.1:5000
3.**Use the application**:
  1.Enter the website URL in the input field.
  2.Type your question related to the website's content.
  3.Click "Get Answer" to receive the response from the bot.
    

   
