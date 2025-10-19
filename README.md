# AI Web Scraping MCP Server

An intelligent web scraping tool built with the Model Context Protocol (MCP) that searches documentation, fetches web content, and provides AI-powered responses using Groq's LLM API.

## 🚀 Features

- **Smart Documentation Search**: Search through popular library documentation (LangChain, OpenAI, Llama-Index, UV)
- **AI-Powered Web Scraping**: Automatically clean and extract meaningful content from web pages
- **Rate-Limited API Integration**: Built-in handling for Groq API rate limits
- **MCP Protocol**: Seamless integration with MCP-compatible clients
- **Async Processing**: High-performance asynchronous operations

## 📋 Prerequisites

- Python 3.10 or higher
- UV package manager
- Valid API keys for:
  - **Serper API** (for web search)
  - **Groq API** (for LLM processing)

## 🔧 Installation

1. **Clone the repository**:
   ```bash
   git clone <https://github.com/iqbal-waqar/MCP-SERVER>
   cd mcp-server-python
   ```

2. **Install dependencies using UV**:
   ```bash
   uv sync
   ```

3. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```env
   SERPER_API_KEY=your_serper_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

## 🔑 API Keys Setup

### Serper API Key
1. Visit [Serper.dev](https://serper.dev/)
2. Sign up for a free account
3. Get your API key from the dashboard
4. Add it to your `.env` file

### Groq API Key
1. Visit [Groq Console](https://console.groq.com/)
2. Create an account and verify your email
3. Navigate to API Keys section
4. Generate a new API key
5. Add it to your `.env` file

**⚠️ Important**: Use a **good quality API key** with sufficient rate limits. The free tier has limited tokens per minute (6000 TPM) which may cause rate limiting issues during heavy usage.

## 🏗️ Project Structure

```
mcp-server-python/
├── mcp_server.py      # Main MCP server implementation
├── client.py          # Example client for testing
├── utils.py           # Utility functions for HTML cleaning and LLM calls
├── .env              # Environment variables (create this)
├── pyproject.toml    # Project dependencies
└── README.md         # This file
```

## 🚀 Usage

### Running the MCP Server

The server runs using the stdio transport protocol:

```bash
uv run mcp_server.py
```

### Using the Client

Test the server with the included client:

```bash
uv run client.py
```

### Available Tools

#### `get_docs`
Search documentation for specific libraries and queries.

**Parameters**:
- `query` (string): The search query (e.g., "How to publish a package with UV")
- `library` (string): The library to search in (`langchain`, `openai`, `llama-index`, `uv`)

**Example**:
```python
result = await session.call_tool("get_docs", {
    "query": "How to publish a package with uv on gitlab",
    "library": "uv"
})
```

## 🔧 Configuration

### Supported Libraries
- **LangChain**: `python.langchain.com/docs`
- **OpenAI**: `platform.openai.com/docs`
- **Llama-Index**: `docs.llamaindex.ai/en/stable`
- **UV**: `docs.astral.sh/uv`

### LLM Model
Currently configured to use `llama-3.1-8b-instant` from Groq. You can modify this in:
- `mcp_server.py` (line 52)
- `client.py` (line 41)

## ⚠️ Common Issues & Solutions

### Rate Limiting
If you encounter rate limit errors:
1. **Wait**: Rate limits reset after a short period (usually 60 seconds)
2. **Upgrade**: Consider upgrading your Groq plan for higher limits
3. **Optimize**: Reduce the chunk size in `fetch_url` function
4. **Retry**: The system will automatically retry after rate limit resets

### API Key Issues
- Ensure your `.env` file is in the root directory
- Verify API keys are valid and active
- Check that you have sufficient credits/quota

### Import Errors
Make sure you're running commands from within the virtual environment:
```bash
source .venv/bin/activate  # On Linux/Mac
# or
.venv\Scripts\activate     # On Windows
```

## 🛠️ Development

### Adding New Documentation Sources
To add support for new documentation sites, update the `docs_urls` dictionary in `mcp_server.py`:

```python
docs_urls = {
    "your-library": "docs.yourlibrary.com",
    # ... existing entries
}
```

**Popular Libraries You Can Add**:
- **FastAPI**: `fastapi.tiangolo.com`
- **Django**: `docs.djangoproject.com`
- **Flask**: `flask.palletsprojects.com`
- **Pandas**: `pandas.pydata.org/docs`
- **NumPy**: `numpy.org/doc`
- **Scikit-learn**: `scikit-learn.org/stable`
- **TensorFlow**: `tensorflow.org/api_docs`
- **PyTorch**: `pytorch.org/docs`
- **Requests**: `docs.python-requests.org`
- **Pydantic**: `docs.pydantic.dev`
- **SQLAlchemy**: `docs.sqlalchemy.org`
- **Celery**: `docs.celeryq.dev`
- **Streamlit**: `docs.streamlit.io`
- **Gradio**: `gradio.app/docs`

Simply add any library's official documentation URL to expand the search capabilities!

### Customizing LLM Behavior
Modify the system prompts in:
- `fetch_url()` function for web scraping behavior
- `client.py` for response formatting

## 📊 Performance Notes

- **Token Usage**: Each web page can consume 1000-5000 tokens depending on content size
- **Rate Limits**: Free Groq tier allows 6000 tokens per minute
- **Processing Time**: Typical response time is 5-15 seconds per query
- **Concurrent Requests**: Limited by API rate limits

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter issues:
1. Check the [Common Issues](#-common-issues--solutions) section
2. Verify your API keys and quotas
3. Ensure you're using the latest dependencies
4. Open an issue with detailed error messages

## 🔗 Useful Links

- [MCP Documentation](https://modelcontextprotocol.io/)
- [FastMCP Framework](https://gofastmcp.com/)
- [Groq API Documentation](https://console.groq.com/docs)
- [Serper API Documentation](https://serper.dev/api-documentation)

---

**Note**: This tool is designed for educational and development purposes. Please respect rate limits and terms of service for all APIs used.