# Cloud_Computing_Project_3
git clone 

spanish_demo = https://raw.githubusercontent.com/joaquinmenendez/Cloud_Computing_Project_3/master/spanish_demo.txt
curl -o spanish_demo $spanish_demo


{"url" : "https://raw.githubusercontent.com/joaquinmenendez/Cloud_Computing_Project_3/master/spanish_demo.txt"}

export PROJECT_ID=[]
export INPUT_BUCKET_NAME=[]
export EXPORT_BUCKET_NAME=[]

gsutil mb -p $PROJECT_ID -l US-EAST1 on gs://$INPUT_BUCKET_NAME/

gsutil mb -p $PROJECT_ID -l US-EAST1 on gs://$EXPORT_BUCKET_NAME/
