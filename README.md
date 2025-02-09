# LLM as a Judge (Using DeepSeek)

This Flask application uses DeepSeek (a hypothetical alternative LLM API) to judge user submissions. Enter your text submission, and DeepSeek will evaluate it and provide a fair judgment.

## Setup

1. Clone the repository or download the ZIP.
2. Install the dependencies:
3. Set your DeepSeek API key as an environment variable:
(On Windows, use `set DEEPSEEK_API_KEY=your_api_key_here`)
4. Run the application:
5. Open your browser and go to [http://localhost:5000](http://localhost:5000).

## How It Works

- The homepage provides a form where you can enter a submission.
- Upon submission, the application sends your text (with a judgment prompt) to DeepSeek via its Python API.
- The resulting judgment is displayed on the same page.

*Note: This project assumes DeepSeek provides a function `judge_text(prompt)` that returns a judgment string.*
