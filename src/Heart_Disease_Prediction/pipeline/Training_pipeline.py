from src.Heart_Disease_Prediction.components.Data_ingestion import DataIngestion
from src.Heart_Disease_Prediction.components.Data_transformation import DataTransformation
from src.Heart_Disease_Prediction.components.Model_trainer import ModelTrainer


#Data ingestion Pipeline
obj=DataIngestion()
train_data_path,test_data_path=obj.initiate_data_ingestion()

# Data Transformation Pipeline
data_transformation=DataTransformation()
train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path,test_data_path)

# Model Training Pipeline
model_trainer_obj=ModelTrainer()
model_trainer_obj.initate_model_training(train_arr,test_arr)

