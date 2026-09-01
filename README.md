# AI Text Translator using Qwen and Ollama

An AI-powered command-line text translation application built using **Python, Ollama, and the Qwen language model**.

The application accepts text from the user, takes the desired target language, sends the translation request to the locally running Qwen model through the Ollama API, and displays the translated text in the terminal.

---

## Features

- AI-powered text translation
- Supports multiple target languages
- Uses the Qwen language model
- Runs locally using Ollama
- Simple command-line interface
- Interactive translation loop
- Allows multiple translations in one session
- Basic input validation
- HTTP error handling
- No external API key required
- User can exit the application using the `exit` command

---

## Technologies Used

- **Python**
- **Ollama**
- **Qwen**
- **Requests**
- **REST API**

---

## Project Architecture

```text
User
  ↓
Python CLI
  ↓
Translation Prompt
  ↓
Ollama Local API
  ↓
Qwen Model
  ↓
Translated Text
  ↓
Terminal
```
## How It Works

The user provides two inputs:

The text that needs to be translated
The target language

The application then creates a prompt and sends it to the Ollama API.

For example:
```text

Translate the text into Hindi.

Text:
Hello, how are you?
```

The Qwen model processes the prompt and returns the translated text.

The result is then displayed in the terminal.

## Project Structure
AI-Text-Translator/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
## File Description
|File|	Description|
|main.py	|Main Python application|
|requirements.txt	|Python dependency list|
|README.md|	Project documentation|
|.gitignore	|Prevents unnecessary files from being uploaded to GitHub|
## Prerequisites

Before running the project, make sure you have:

-Python 3.8 or higher
-Ollama installed
-Qwen model installed in Ollama
-Git installed

## Installing Ollama

This project uses Ollama to run the Qwen model locally.

Install Ollama from the official Ollama website.

After installation, open a terminal and download the Qwen model:
```text

ollama pull qwen
```


Check that the model has been installed:
```text

ollama list
```

You should see the Qwen model in the list.

## Ollama API

The application communicates with the Ollama local generation API:
```text

http://localhost:11434/api/generate
```

The API is used to send the translation prompt to the Qwen model and receive the generated translation.

## Installation
1. Clone the Repository
```text
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project directory:
```text
cd AI-Text-Translator
```
2. Create a Virtual Environment

On Windows:
```
python -m venv .venv
```
Activate the virtual environment:
```
.venv\Scripts\activate
```
On macOS/Linux:
```
python3 -m venv .venv
```
Activate it:
```
source .venv/bin/activate
```
3. Install Dependencies:
Install the required Python package:
```
pip install -r requirements.txt
```
The project uses:
```
requests
```
## Running the Application

Make sure Ollama is running and the Qwen model is available.

Start the application:
```
python main.py
```
The program will ask:
```
Enter the text:
Translate to:
```
Example

English to Hindi
```
Enter the text: Hello, how are you?
Translate to: Hindi

Translated Text:
नमस्ते, आप कैसे हैं?
```
## Code Workflow

The application follows these steps:
```

1. User enters text
          ↓
2. User enters target language
          ↓
3. Python creates translation prompt
          ↓
4. HTTP POST request is sent
          ↓
5. Ollama receives the request
          ↓
6. Qwen processes the prompt
          ↓
7. Translation is returned
          ↓
8. Python displays the result
```
## API Request

The application sends a POST request to Ollama:
```

response = requests.post(
    OLLAMA_URL,
    json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }
)
```
The application uses:
```

OLLAMA_URL = "http://localhost:11434/api/generate"
```

and:
```

MODEL = "qwen"
```
## Translation Function

The main translation functionality is handled by:
```
def translate(text, target):
```

The function:

Receives the source text
Receives the target language
Creates an AI prompt
Sends the prompt to Ollama
Receives the model response
Returns the translated text
## Error Handling

The application uses:
```
response.raise_for_status()
```

to detect HTTP errors from the Ollama API.

This helps identify problems such as:

Ollama not running
Incorrect API endpoint
Server errors
Model-related API errors
## Requirements

The project requires the following Python package:
```
requests
```
Ollama and the Qwen model are installed separately and are not included in the Python requirements.



Author

Ananya Mishra

AI / Generative AI Projects
