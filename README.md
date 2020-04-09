# Using Google Cloud Services to develop a Serverless Data Engineering Pipeline
## Data Analysis in the Cloud at Scale (ECE 590.24) - Project 4

This is a tutorial of how to use Google Cloud Services to develop a Serverless Data Engineering Pipeline.<br> You can see a video demostration [here](https://youtu.be/4PwVkW0_wB8). 

**Previous projects**<br>
- [Submitting a ML and Descriptive analysis to a Spark cluster on GCP](https://github.com/joaquinmenendez/Cloud_Computing_Project_3)<br>
- [Docker containerization](https://github.com/joaquinmenendez/Cloud_Computing_Project_2)<br>
- [Continuous Delivery of Flask Application on GCP](https://github.com/joaquinmenendez/Cloud_Computing_Project_1)<br>


### General steps
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
`InputToOutput` This function is trigger when a file is added into a bucket (`input_serverless`). The Cloud Function read this file (PLAIN TEXT), performs a Sentiment Analysis and save the output into a different bucket (`output_serverless`). I choose to do this despite the fact that storing the output into a Database is a better practice. This could be modified.<br> Feel free to use this only as an example.<br>

**3)** Enable APIs:<br>
- Cloud Functions API<br>
- Cloud Natural Language API<br>
*It could be that other APIs should be enabled to run these functions. In case you experience some error check if other API should be enabled*

### DownloadPrint

This function takes an POST request with the format `{"url":"[A link to .txt file]"}`. The function would return a brief inform with several metrics: 
- Document sentiment score
- Document sentiment magnitude
- Language of the text
- Original text

**1)** Go to Console/Cloud Functions a click on 'CREATE FUNCTION'
![Cloud Function](https://user-images.githubusercontent.com/43391630/77852144-f9f23300-71aa-11ea-936b-9c811145e740.png) <!-- .element height="50%" width="50%" -->

**2)** Example of `DownloadPrint`
![DonloadPrint](https://user-images.githubusercontent.com/43391630/77869995-40c54480-720e-11ea-8211-97903d5d37dc.png) <!-- .element height="50%" width="50%" -->

It is important to check the box that says *Allow unaunthenticated invocations* if we want to use this function externally.

On **MAIN.PY** copy and paste the content from `DownloadPrint.py`.<br>
**REQUIREMENTS.TXT** should look like this:<br>
```python
# Function dependencies, for example:
# package>=version
google-cloud-language
```
Once we complete all we click on 'DEPLOY'.

**3**) Testing `DownloadPrint`<br>
After the Function has been deployed we could test if is working correctly. In this case I will test the function with the following request
```bash
{"url" : "https://raw.githubusercontent.com/joaquinmenendez/Cloud_Computing_Project_4/master/spanish_demo.txt"}
```
*Example of how it should look*
![Testing DownloadPrint](https://user-images.githubusercontent.com/43391630/77870494-8fbfa980-720f-11ea-8c96-9d52cf6b228c.png)<!-- .element height="50%" width="50%" -->

**4)** Using `DowloadPrint` in a API-like way. To check the function is properly working open your local terminal (not the CloudShell) and type:

```bash
export YOUR_PROJECT_URL = `Your project url`
curl -H "Content-Type: application/json" -X POST -d '
{"url" : "https://raw.githubusercontent.com/joaquinmenendez/Cloud_Computing_Project_4/master/spanish_demo.txt"}' $YOUR_PROJECT_URL
```
(You can find the URL of the function if you click in EDIT)

## InputToOutput

**1)** We should start creating the buckets where we are going to dump the .txt files and the output of our analysis.

```bash
export PROJECT_ID=`Your project id`
export INPUT_BUCKET_NAME=input_serverless
export OUTPUT_BUCKET_NAME=output_serverless
#Input
gsutil mb -p $PROJECT_ID -b on gs://$INPUT_BUCKET_NAME/
#Output
gsutil mb -p $PROJECT_ID -b on gs://$OUTPUT_BUCKET_NAME/
```

*An example of how it should look*
![Example storage](https://user-images.githubusercontent.com/43391630/77868878-add6db00-720a-11ea-902f-a9c3ae40dd19.png)<!-- .element height="50%" width="50%" -->

**2)** Example of `InputToOutput`<br>

![Example InputToOutput](https://user-images.githubusercontent.com/43391630/77871323-c696bf00-7211-11ea-958c-ef690e31577a.png)<!-- .element height="50%" width="50%" -->

On **MAIN.PY** copy and paste the content from `InputToOutput.py`.<br>
**REQUIREMENTS.TXT** should look like this:<br>
```bash
# Function dependencies, for example:
# package>=version
google-cloud-language
google-cloud-storage
```

**3)** Once the function has been deployed we could test it by uploading a file into the `input_serverless` bucket.<br>

![Upload file to input_serverless](https://user-images.githubusercontent.com/43391630/77871518-62c0c600-7212-11ea-8d5e-66f7492d808b.png)<!-- .element height="50%" width="50%" -->

