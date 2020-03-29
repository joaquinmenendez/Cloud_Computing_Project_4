# Cloud_Computing_Project_4
[Youtube link](https://youtu.be/4PwVkW0_wB8)

git clone 

spanish_demo = https://raw.githubusercontent.com/joaquinmenendez/Cloud_Computing_Project_4/master/spanish_demo.txt
curl -o spanish_demo $spanish_demo


{"url" : "https://raw.githubusercontent.com/joaquinmenendez/Cloud_Computing_Project_4/master/spanish_demo.txt"}

```bash
export PROJECT_ID=[]
export INPUT_BUCKET_NAME=[]
export EXPORT_BUCKET_NAME=[]
```
```bash
#Input
gsutil mb -p $PROJECT_ID -b on gs://$INPUT_BUCKET_NAME/
#Output
gsutil mb -p $PROJECT_ID -b on gs://$EXPORT_BUCKET_NAME/
```

```bash
requirements.txt
goocle-cloud-storage
google-cloud-language
```

```bash
curl -H "Content-Type: application/json" -X POST -d '
{"url" : "https://raw.githubusercontent.com/joaquinmenendez/Cloud_Computing_Project_4/master/spanish_demo.txt"}' https://us-central1-project3-serverless.cloudfunctions.net/DownloadPrint
```
