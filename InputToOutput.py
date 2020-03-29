def InputToOutput(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    print(f"Processing file: {event['name']}.")
    from google.cloud import storage
    client = storage.Client()
    bucket = client.get_bucket('input_serverless')  # name of my bucket
    blob = bucket.get_blob(event['name'])
    print(blob.download_as_string())

    # writing in the output bucket
    bucket_out = client.get_bucket('output_serverless')  # name of the bucket where I am going to save my files
    blob_out = bucket_out.blob(f'{event["name"][:-4]}_to_english.txt')  # removing the .txt  to the original file
    inform = sample_analyze_sentiment(f'gs://input_serverless/{event["name"]}')
    inform = inform + f'\nOriginal text:\n{blob.download_as_string()}\n'
    blob_out.upload_from_string(inform)
    print('Sentiment Analysis Complete!')


def sample_analyze_sentiment(gcs_content_uri):
    """
    Analyzing Sentiment in a .txt file in a bucket
    Args:
      gcs_content_uri Google Cloud Storage URI where the file content is located.
      e.g. gs://[Your Bucket]/[Path to File]
    """
    # Import libraries
    from google.cloud import language_v1
    from google.cloud.language_v1 import enums

    client = language_v1.LanguageServiceClient()
    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT
    # Language parameter is optional. If not specified, the language is automatically detected.
    # https://cloud.google.com/natural-language/docs/languages
    document = {"gcs_content_uri": gcs_content_uri, "type": type_}  # Could add `language:` if I want to be sure Google doesn't make a mistake
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