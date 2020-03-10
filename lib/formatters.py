import json
from bs4 import BeautifulSoup
import xml.dom.minidom

def format_json(source, indent=2, minify=False):

    # Parse json into python dictionary
    parsed = json.loads(source)

    # Format
    formatted = None

    # Check if we are going to minify json
    if minify:
        formatted = json.dumps(parsed, indent=None, separators=(':',','))
    else:
        formatted = json.dumps(parsed, indent=indent)

    # Return formatted json
    return formatted

def format_html(source, indent=2):

    # Format with BeautifulSoup
    soup = BeautifulSoup(source)
    return soup.prettify(indent_width=2)

    # # Format with xml minidom
    # dom = xml.dom.minidom.parseString(source)
    # return dom.toprettyxml(" " * indent)

def format_python():
    pass
