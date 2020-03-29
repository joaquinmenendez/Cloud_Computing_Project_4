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
    blob = bucket_out.blob(f'{event["name"][:-4]}to_english.txt')  # removing the .txt  to the original file
    blob.upload_from_string('Here I will add some data transformation')