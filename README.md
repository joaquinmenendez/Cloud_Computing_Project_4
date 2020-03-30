# Using Google Cloud Services to develop a Serverless Data Engineering Pipeline
## Data Analysis in the Cloud at Scale (ECE 590.24) - Project 4

This is a tutorial of how to use Google Cloud Services to develop a Serverless Data Engineering Pipeline.<br> You can see a quick demostration [here](https://youtu.be/4PwVkW0_wB8).

**Previous projects**<br>
[Docker containerization](https://github.com/joaquinmenendez/Cloud_Computing_Project_2)<br>
[Continuous Delivery of Flask Application on GCP](https://github.com/joaquinmenendez/Cloud_Computing_Project_1)<br>

### Steps
**1)** Create a new project on GCS<br>
**2)** Clone this repository if you want to use the sames scripts and demo files<br>
```bash
#HTTP
git clone https://github.com/joaquinmenendez/Cloud_Computing_Project_4.git
#SSH
git clone git@github.com:joaquinmenendez/Cloud_Computing_Project_4.git
```

In this tutorial I will be using 2 different Cloud Functions.<br>
`DownloadPrint` Accepts a POST request without the need to be in the GCS enviroment. In other words, other user could use this function in an API-like way. <br>
`InputToOutput` This function is trigger when a file is added into a bucket (`input_serverless`). The Cloud Function read this file (PLAIN TEXT), performs a Sentiment Analysis and save the output into a different bucket (`output_serverless`). I choose to do this despite the fact that storing the output into a Database is a better practice. This could be modified. Feel free to use this only as an example.<br>

**3)** Enable APIs

### DownloadPrint

This function takes an POST request with the format `{"url":"[A link to .txt file]"}`. The function would return a brief inform with several metrics: 
- Document sentiment score
- Document sentiment magnitude
- Language of the text
- Original text

**4)** Go to Console/Cloud Functions a click on 'CREATE FUNCTION'
![Cloud Function](https://user-images.githubusercontent.com/43391630/77852144-f9f23300-71aa-11ea-936b-9c811145e740.png) <!-- .element height="50%" width="50%" -->

**5)** Example of `DownloadPrint`
![DonloadPrint](https://user-images.githubusercontent.com/43391630/77869995-40c54480-720e-11ea-8211-97903d5d37dc.png) <!-- .element height="50%" width="50%" -->

On **MAIN.PY** copy and paste the content from `DownloadPrint.py`.<br>
**REQUIREMENTS.TXT** should look like this:<br>
```python
# Function dependencies, for example:
# package>=version
google-cloud-language
```
Once we complete all we click on 'DEPLOY'.

**6**) Testing `DownloadPrint`<br>
After the Function has been deployed we could test if is working correctly. In this case I will test the function with the following request
```bash
{"url" : "https://raw.githubusercontent.com/joaquinmenendez/Cloud_Computing_Project_4/master/spanish_demo.txt"}<!-- .element height="50%" width="50%" -->
```
*Example of how it should look*
![Testing DownloadPrint](https://user-images.githubusercontent.com/43391630/77870494-8fbfa980-720f-11ea-8c96-9d52cf6b228c.png)<!-- .element height="50%" width="50%" -->

**7)** Using `DowloadPrint` in a API-like way.

```bash
curl -H "Content-Type: application/json" -X POST -d '
{"url" : "https://raw.githubusercontent.com/joaquinmenendez/Cloud_Computing_Project_4/master/spanish_demo.txt"}' https://us-central1-project3-serverless.cloudfunctions.net/DownloadPrint
```

### InputToOutput

We should start creating the buckets where we are going to dump the .txt files and the output of our analysis.

```bash
export PROJECT_ID=[]
export INPUT_BUCKET_NAME=[]
export EXPORT_BUCKET_NAME=[]
#Input
gsutil mb -p $PROJECT_ID -b on gs://$INPUT_BUCKET_NAME/
#Output
gsutil mb -p $PROJECT_ID -b on gs://$EXPORT_BUCKET_NAME/
```

*An example of how it should look*
![Example storage](https://user-images.githubusercontent.com/43391630/77868878-add6db00-720a-11ea-902f-a9c3ae40dd19.png)<!-- .element height="50%" width="50%" -->

On **MAIN.PY** copy and paste the content from `InputToOutput.py`.<br>
**REQUIREMENTS.TXT** should look like this:<br>
```bash
requirements.txt
goocle-cloud-storage
google-cloud-language
```


