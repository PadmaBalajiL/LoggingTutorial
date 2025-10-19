from loguru import logger
import sys

# Remove the default handler to have more control over the output.
logger.remove()
# Add a default handler back for the basic usage section.
logger.add(sys.stderr, level="INFO")

print("--- Basic Usage ---")
logger.debug("This is a debug message (will not be shown because level is INFO)")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
print("--------------------\\n")


print("--- Logging to a File ---")
# The logger is configured to write to "file.log"
logger.add("file.log")
logger.info("This message will be written to file.log")

# This logger is configured to only write ERROR messages and above to "file_error.log"
logger.add("file_error.log", level="ERROR")
logger.info("This message will NOT be written to file_error.log")
logger.error("This message WILL be written to file_error.log")
print("Messages have been written to file.log and file_error.log")
print("--------------------\\n")


print("--- Formatting ---")
# This logger is configured to use a specific format
logger.add("file_formatted.log", format="{time} {level} {message}")
logger.info("This is a test message")
print("A formatted message has been written to file_formatted.log")
print("--------------------\\n")


print("--- Exception Handling ---")
# The @logger.catch decorator will automatically log any exception
@logger.catch
def my_function(x, y, z):
    return 1 / (x + y + z)

my_function(1, -1, 0)
print("The exception from my_function was caught and logged.")
print("--------------------\\n")
