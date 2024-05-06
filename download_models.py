from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

modelName = 'lxyuan/distilbert-base-multilingual-cased-sentiments-student'
modelPath = 'model'

model = AutoModelForSequenceClassification.from_pretrained(modelName)
model.save_pretrained(modelPath)

tokenizer = AutoTokenizer.from_pretrained(modelName)
tokenizer.save_pretrained(modelPath)
