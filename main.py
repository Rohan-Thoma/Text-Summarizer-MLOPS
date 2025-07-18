from src.text_summarizer.logging import logger 
from src.text_summarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.text_summarizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationTrainingPipeline
from src.text_summarizer.pipeline.stage_3_model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.text_summarizer.pipeline.stage_4_model_evaluation_pipeline import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")

    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()

    logger.info(f"stage {STAGE_NAME} is completed")

except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = "Data Transformation Stage"

try:
   logger.info(f"stage {STAGE_NAME} initiated")

   data_transformation_pipeline = DataTransformationTrainingPipeline()
   data_transformation_pipeline.initiate_data_transformation()

   logger.info(f"stage {STAGE_NAME} is completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Stage"

try:
   logger.info(f"stage {STAGE_NAME} initiated")

   model_trainer_pipeline = ModelTrainerTrainingPipeline()
   model_trainer_pipeline.initiate_model_trainer()

   logger.info(f"stage {STAGE_NAME} is completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"

try:
   logger.info(f"stage {STAGE_NAME} initiated")

   model_evaluation_pipeline = ModelEvaluationPipeline()
   model_evaluation_pipeline.initiate_model_evaluation()

   logger.info(f"stage {STAGE_NAME} is completed")
except Exception as e:
    logger.exception(e)
    raise e