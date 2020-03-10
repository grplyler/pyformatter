import json
from bs4 import BeautifulSoup
import xml.dom.minidom
from yapf.yapflib.yapf_api import FormatCode

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

def format_python(source, indent=2):
    
    # Format Python with Google's Yapf library
    formatted = FormatCode(source)[0]
    return formatted
