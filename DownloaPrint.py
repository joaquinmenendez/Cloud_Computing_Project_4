def DownloadPrint(request):
    """Responds to a HTTP request in a JSON format.
    Reads a .txt file using a URL
    Args:
        request: a request with a JSON format {"url":"[any URL.txt]"}.
    Returns:
        file : (str) The text content
    """
    import urllib.request
    request_json = request.get_json()
    if request_json and 'url' in request_json:
        try:
            file = urllib.request.urlopen(request_json['url'])
            file = file.read()
            return file
        except:
            return 'Reading URL failed. Please check the URL.'
    else:
        return 'Query failed.\nPlease submit a query with the following format: {"url":"[A URL ended with .txt]"}'
