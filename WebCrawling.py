import os
import re
import urllib

def extract_link_urls(html, page_url):
    """Return normalized intra-site link URLs found in the HTML."""
    pattern = """
        <a            # beginning of anchor tag
        .+?           # stuff before href attribute
        href="        # beginning of href attribute
        (.+?\.html?)  # contents of href attribute (HTML only)
        "             # end of href attribute
        .+?           # stuff after href attribute
        >             # end of the anchor tag
    """

    matches = re.findall(pattern, html, re.VERBOSE)

    # Found link URLs that don't leave the site.
    link_urls = []

    # Only add intra-site link URLs to the returned list.
    for match in matches:
        if match[:7] != "http://":
            link_urls.append(normalize_url(match, page_url))

    return link_urls

def normalize_url(link_url, page_url):
    """Return the normalized form of the given link (relative to the page URL)."""
    # Strip off the file name from the current page's URL.
    page_path = os.path.dirname(page_url)
    # Join (concatenate) the current page's URL path to the new link.
    joined_url = os.path.join(page_path, link_url)
    # Normalize the resulting path (deal with relative folder references).
    normalized_url = os.path.normpath(joined_url)
    # Return the result, replacing backslashes with slashes.
    return normalized_url.replace("\\", "/")
   
def validate_url(candidate_url):
    """Return (True, Normalized URL) if the given URL is valid."""
    # Only match URLs that end with .htm or .html (http:// is optional).
    matches = re.findall(r"^(http://)?(.+/.+\.html?)$", candidate_url)

    if matches:
        # Pull out the URL from the second group in the pattern.
        normalized_url = matches[0][1]
    else:
        # Invalid URL, so normalized form is irrelevant.
        normalized_url = ""

    # Return a (Boolean, String) tuple to the calling code.
    return (len(matches) == 1, normalized_url)


# Ask the user for a starting URL.
while True:
    start_url = raw_input("Enter the starting URL: ")
    (is_valid_url, start_url) = validate_url(start_url)
    
    if is_valid_url:
        break
    
    print "Please enter a VALID starting URL."

# URLs that have yet to be crawled.
unvisited_urls = []

# URLs that have already been crawled.
visited_urls = []

# Add the starting URL to a list of unvisited URLs.
unvisited_urls.append(start_url)

# While there are still unvisited URLs:
while unvisited_urls:
    # Get the first unvisited URL and remove it from the list.
    page_url = unvisited_urls[0]
    unvisited_urls = unvisited_urls[1:]

    # Add this URL to the list of visited URLs.
    visited_urls.append(page_url)

    # Fetch the HTML found at this URL.
    html = urllib.urlopen("http://" + page_url).read()

    # Extract all local site links from the HTML and "normalize" them.
    link_urls = extract_link_urls(html, page_url)

    # For each of the link URLs:
    for link_url in link_urls:
        # If this link URL hasn't already been visited and isn't in the unvisited
        # list:
        if link_url not in visited_urls and link_url not in unvisited_urls:
            # Add this link URL to the unvisited list.
            unvisited_urls.append(link_url)

    print "Found %d links in %s, %d unvisited, %d visited" % (len(link_urls),
                                                              page_url,
                                                              len(unvisited_urls),
                                                              len(visited_urls))
