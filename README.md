# LLaMa_LoRa

This project uses LLaMa with LoRA (Low-Rank Adaptation) to efficiently fine-tune language models. Here you will find the files and configurations needed to implement and run the model.

## Project Structure

- **LLaMa_LoRA_Bot.py**: Main script to interact with the fine-tuned model.
- **Ngrok.py**: Configuration to expose local services using Ngrok.
- **requirements.txt**: List of dependencies required to run the project.
- **llama2-lora-spanish-final/**: Contains the fine-tuned model files, including:
  - `adapter_config.json`: LoRA adapter configuration.
  - `adapter_model.safetensors`: Weights of the fine-tuned model.
  - `tokenizer.*`: Files related to the tokenizer.

## Prerequisites

1. Python 3.10 or higher.
2. Install the dependencies by running:
   ```bash
   pip install -r requirements.txt 
   ```

## Usage

1. Set up the environment variables in the `.env` file.
2. Run the main script:
    ```bash
    python LLaMa_LoRA_Bot.py
    ```
3. If you need to `expose` the service, use Ngrok.py:
    ```bash
    python Ngrok.py
    ```