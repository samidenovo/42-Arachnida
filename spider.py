import argparse
from html.parser import HTMLParser
from urllib.error import URLError
from urllib.request import urlopen
from urllib.parse import urljoin, urlsplit
from pathlib import Path
MAX_DOWNLOADS = 10

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.image_refs = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            attributes = dict(attrs)
            src = attributes.get("src")
            if src:
                self.image_refs.append(src)

# parsing command-line arguments
parser = argparse.ArgumentParser(prog="spider")

parser.add_argument("url", help="Website URL to crawl")
parser.add_argument(
    "-r",
    dest="recursive",
    action="store_true",
    help="Enable recursive crawling",
)
parser.add_argument(
    "-l",
    dest="depth",
    type=int,
    nargs='?',
    default=5,
    const=5,
    metavar="N",
    help="Maximum depth for recursive crawling (default: 5)",
)
parser.add_argument(
    "-p",
    dest="path",
    nargs='?',
    default="./data/",
    const="./data/",
    metavar="PATH",
    help="Directory to save crawled data (default: ./data/)",
)

args = parser.parse_args()

# Fetching the HTML content and parsing it
try:
    with urlopen(args.url, timeout=40) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        page_html = response.read().decode(charset, errors="replace")
except (URLError, TimeoutError, ValueError) as error:
    parser.error(f"Could not fetch URL: {error}")

html_parser = PageParser()
html_parser.feed(page_html)

allowed_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
image_urls = []

for image_ref in html_parser.image_refs:
    image_url = urljoin(args.url, image_ref)
    image_path = urlsplit(image_url).path.lower()

    if image_path.endswith(allowed_extensions):
        image_urls.append(image_url)

output_dir = Path(args.path)

# Creating the output directory if it doesn't exist and downloading images
try:
    output_dir.mkdir(parents=True, exist_ok=True)
except OSError as error:
    parser.error(f"Could not create output directory: {error}")

for index, image_url in enumerate(image_urls[:MAX_DOWNLOADS], start=1):
    extension = Path(urlsplit(image_url).path).suffix
    output_file = output_dir / f"data_{index}{extension}"

    try:
        with urlopen(image_url, timeout=40) as response:
            image_data = response.read()

        with output_file.open("wb") as image_file:
            image_file.write(image_data)
    except (URLError, TimeoutError, OSError) as error:
        parser.error(f"Could not download {image_url}: {error}")

    print(f"Downloaded {image_url} -> {output_file}")
