# Loguru Tutorial

Loguru is a Python logging library that aims to be a simple and powerful replacement for the standard `logging` module.

## Getting Started

First, you need to install `loguru`:

```bash
pip install loguru
```

Or, if you are using `uv`:

```bash
uv pip install loguru
```

## Examples

All the code examples for this tutorial can be found in the `loguru_examples/examples.py` file.

To run the examples, you can execute the file from your terminal:

```bash
python loguru_examples/examples.py
```

This will demonstrate:
*   Basic Usage
*   Logging to a File
*   Formatting
*   Exception Handling

After running the script, you will find the following log files in your project directory:
*   `file.log`
*   `file_error.log`
*   `file_formatted.log`

## Comparison with the standard `logging` module

| Feature | `logging` | `loguru` |
| --- | --- | --- |
| **Configuration** | Complex, requires handlers, formatters, and filters | Simple, one-line configuration |
| **Exception handling** | Requires manual handling of exceptions | Automatic exception handling with `@logger.catch` |
| **Formatting** | Requires `Formatter` objects | Simple string formatting |
| **Thread safety** | Yes | Yes |
| **Multiprocessing safety** | Yes | Yes |
| **Structured logging** | Requires custom formatters | Built-in support for structured logging |
