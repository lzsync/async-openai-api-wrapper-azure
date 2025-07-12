# async-openai-api-wrapper-azure

[![Azure Functions](https://img.shields.io/badge/Azure--Functions-Python-blue?logo=azure-functions)](https://learn.microsoft.com/en-us/azure/azure-functions/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A lightweight, asynchronous API wrapper built with **Azure Functions (Python)** for interacting with the **Azure OpenAI Service**. This project exposes REST endpoints for **chat completions** and **embeddings**, using the official `openai` SDK and **Azure Active Directory (AAD)** authentication via `DefaultAzureCredential`.

---

## ✨ Features

- ⚡️ Asynchronous wrapper using `openai.AsyncAzureOpenAI`
- 🧠 `/chat-completion` endpoint for GPT model interactions
- 📊 `/embeddings` endpoint for vector generation
- 🔐 Secure token authentication with Azure Identity (no API key hardcoding)
- 🧱 Modular design with centralized config and error handling
- 🚀 Deployable via Azure Functions on Consumption or Premium Plan

---

## 📁 Project Structure

```text
src/
├── api_utils.py           # Error handling and response decorator
├── config.py              # Environment config using pydantic-settings
├── func_app.py            # Azure Function entry point with route handlers
├── requirements.txt
└── set-environment.bat    # (Optional) local env setup script
```

---

## 🚀 API Endpoints

### 🧠 Chat Completion

```http
POST /api/chat-completion
```

#### Request Body:

```json
{
  "input": "Tell me a joke about data scientists."
}
```

#### Response:

```json
{
  "result": "Why did the data scientist break up with the graph analyst? There was no correlation."
}
```

---

### 📊 Embeddings

```http
POST /api/embeddings
```

#### Request Body:

```json
{
  "input": "Machine learning is fascinating."
}
```

#### Response:

```json
[
  [0.0123, 0.9845, ...]  // Example 1536-dimension vector
]
```

---

## ⚙️ Environment Variables

Set the following values using a `.env` file or `local.settings.json`:

```env
LLM_DEPLOYMENT_NAME=gpt-35-turbo
EMBEDDING_DEPLOYMENT_NAME=text-embedding-ada-002
DEFAULT_CRED=https://cognitiveservices.azure.com/.default
API_VERSION=2023-05-15
ENDPOINT=https://your-resource.openai.azure.com/
MAX_RETRIES=3
TIMEOUT_SECONDS=30
```

> ✅ This project uses `DefaultAzureCredential` which supports local dev (`az login`) and production managed identity.

---

## 📦 Dependencies

- `azure-functions`
- `openai`
- `azure-identity`
- `pydantic-settings`

Install them with:

```bash
pip install -r requirements.txt
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙇 About

This repo was created as a clean, minimal template to demonstrate how to build async Azure Functions that wrap Azure OpenAI endpoints. Feel free to fork or adapt it for your own projects!
