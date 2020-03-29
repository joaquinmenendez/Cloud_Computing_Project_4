
def sample_analyze_sentiment(text_content):
    """
    Analyzing Sentiment in a String
    Args:
      text_content The text content to analyze
    """
    # Import libraries
    from google.cloud import language_v1
    from google.cloud.language_v1 import enums

    client = language_v1.LanguageServiceClient()
    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT
    # Language parameter is optional. If not specified, the language is automatically detected.
    # https://cloud.google.com/natural-language/docs/languages
    document = {"content": text_content, "type": type_}  # Could add `language:` if I want to be sure Google doesn't make a mistake
    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8
    response = client.analyze_sentiment(document, encoding_type=encoding_type)

    #Inform. Will dump my analysis in this variable
    inform = 'Sentiment Analysis completed\n'
    # Get overall sentiment of the input document
    inform = inform + (u"Document sentiment score: {}\n".format(response.document_sentiment.score))
    inform = inform + (u"Document sentiment magnitude: {}\n".format(response.document_sentiment.magnitude))

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    inform = inform + (u"Language of the text: {}".format(response.language))
    return inform

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
            print (file)
            inform = sample_analyze_sentiment(file)
            return inform
        except:
            return 'Reading URL failed. Please check the URL.'
    else:
        return 'Query failed.\nPlease submit a query with the following format: {"url":"[A URL ended with .txt]"}'
