
import re

def is_valid_url(url):
    """
    Checks if the given string matches a URL pattern.
    """
    pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'[^\s/$.?#].[^\s]*$'  # domain and path
    )
    return bool(pattern.match(url))

def format_url(url):
    """
    Ensures the URL starts with 'https://'.
    """
    if not url.startswith("http://") and not url.startswith("https://"):
        return "https://" + url
    return url

def shorten_url(url, length=20):
    """
    Truncates the URL to the specified length and appends '...'.
    """
    return (url[:length] + '...') if len(url) > length else url
