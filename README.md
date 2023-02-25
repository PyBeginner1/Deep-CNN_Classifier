# Building a Deep Learning CNN Classifier project

Workflow
1. Update config.yaml
2. Update secrets.yaml  (Optional)    #Any sensitive data
3. Update params.yaml
4. Update the entity
5. Update the Configuration Manager in src/deepClassifier
6. Update the components
7. Update the Pipeline
8. Test run the Pipeline
9. Run tox for testing package
10. Update the dvc.yaml
11. Run "dvc repro" for running all the stages in the pipeline 


Step 1: Set the env variable 
MLFLOW_TRACKING_URI=https://dagshub.com/PyBeginner1/Deep-CNN_Classifier.mlflow \
MLFLOW_TRACKING_USERNAME=PyBeginner1 \
MLFLOW_TRACKING_PASSWORD=<> \

Step 2: install mlflow
Step 3: Set remote URI
Step 4: Use context manager of mlflow to start run and then log metrics, params and model