# follow steps here to setup AzureML CLI: https://aka.ms/AzureML-WorkspaceHandleCLI
subscription_id="59032f82-256a-462d-a725-92fcf3858502" # "<SUBSCRIPTION_ID>"
resource_group_name="registries" #"<RESOURCE_GROUP>"
workspace_name="ContosoMLDev" #"<WORKSPACE_NAME>"
model_name="bert-base-uncased" 

az account set -s $subscription_id

# create endpoint
endpoint_name="hf-ep-"$(date +%s)
az ml online-endpoint create --name $endpoint_name --workspace-name $workspace_name --resource-group $resource_group_name

# create deployment
cat <<EOF > ./deploy.yml
name: demo
model: azureml://registries/HuggingFaceHub/models/$model_name/labels/latest
endpoint_name: $endpoint_name
instance_type: Standard_DS3_v2
instance_count: 1
EOF
az ml online-deployment create --file ./deploy.yml --workspace-name $workspace_name --resource-group $resource_group_name