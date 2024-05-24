# Ensure the required packages are imported
import transformers
import torch
from accelerate import Accelerator

# Print versions to verify installations
print("Transformers version:", transformers.__version__)
print("Torch version:", torch.__version__)
print("Accelerate version:", Accelerator.__version__)

from transformers import Trainer, TrainingArguments

output_dir = 'logs/bert-base-uncased-llm-classificator'

training_args = TrainingArguments(
    output_dir=output_dir, 
    do_train=True,
    do_eval=True,
    num_train_epochs=3,              
    per_device_train_batch_size=16,  
    per_device_eval_batch_size=16,
    warmup_steps=100,                
    weight_decay=0.01,
    logging_strategy='steps',            
    logging_dir=f"{output_dir}/logs",            
    logging_steps=50,
    evaluation_strategy="steps",
    eval_steps=50,
    save_strategy="steps", 
    load_best_model_at_end=True
)

def compute_metrics(pred):
    from sklearn.metrics import precision_recall_fscore_support, accuracy_score
    
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    
    micro_precision, micro_recall, micro_f1, _ = precision_recall_fscore_support(labels, preds, average='micro')
    macro_precision, macro_recall, macro_f1, _ = precision_recall_fscore_support(labels, preds, average='macro')
    acc = accuracy_score(labels, preds)
    
    metrics = {
        'Accuracy': acc,
        'Micro_F1': micro_f1,
        'Micro_Precision': micro_precision,
        'Micro_Recall': micro_recall,
        'Macro_F1': macro_f1,
        'Macro_Precision': macro_precision,
        'Macro_Recall': macro_recall
    }
    
    return metrics

trainer = Trainer(
    model=model,                     
    args=training_args,                 
    train_dataset=train_dataset,         
    eval_dataset=eval_dataset,            
    compute_metrics=compute_metrics
)

# Start training
trainer.train()
