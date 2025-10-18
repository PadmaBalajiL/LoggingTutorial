# Python Logging Example

A simple Python project to demonstrate the use of the `logging` module.

## How to Run

To run the project, simply execute the `main.py` file:

```bash
python main.py
```

## Files

*   `main.py`: The main entry point of the application. It configures and demonstrates the logging functionality.
*   `TestClass.py`: Contains the `Test1` and `Test2` classes, which are used to demonstrate logging from different modules.
*   `logging.conf`: A configuration file for the `logging` module.
*   `example.log`: The log file where error messages are written.

## Logging Configuration

The logging is configured in `main.py`. Here's a breakdown of the configuration:

*   **Logger:** A logger named `example` is created.
*   **Handlers:**
    *   A `StreamHandler` is configured to output log messages to the console. It's set to handle messages with a level of `DEBUG` and higher.
    *   A `FileHandler` is configured to write log messages to `example.log`. It's set to handle messages with a level of `ERROR` and higher.
*   **Formatter:** A formatter is used to define the format of the log messages: `%(asctime)s  -%(name)s  -%(levelname)s  -%(message)s`.

The `main.py` file also contains a commented-out section that shows how to configure logging using the `logging.conf` file.
