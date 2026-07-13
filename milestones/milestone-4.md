# DLGenAI Project – Milestone 4

## Smart MCQ Solver Challenge: Multiple-Choice Classification with LoRA

## Overview

In this milestone, I reformulated the **Smart MCQ Solver Challenge** as a **multiple-choice classification** problem using Hugging Face Transformers. Each question is paired with its five answer options, allowing the model to score all choices simultaneously. I also applied **LoRA (Low-Rank Adaptation)** for parameter-efficient fine-tuning, reducing the number of trainable parameters while preserving the pretrained model.

---

## Learning Objectives

During this milestone, I learned how to:

* Encode answer labels (A–E) into numeric labels.
* Format prompt-option pairs for multiple-choice models.
* Tokenize data using `bert-base-uncased`.
* Prepare inputs with shape **(batch_size, num_choices, sequence_length)**.
* Use `AutoModelForMultipleChoice` for prediction.
* Interpret logits, loss, and softmax probabilities.
* Apply LoRA for efficient fine-tuning.
* Create Hugging Face Datasets and train using the `Trainer` API.

---

## Technologies Used

* Python
* PyTorch
* Hugging Face Transformers
* Hugging Face Datasets
* PEFT (LoRA)
* BERT (`bert-base-uncased`)
* Kaggle Notebook

---

## Workflow

1. Loaded and encoded the training dataset (A–E → 0–4).
2. Formatted each question with its five answer choices.
3. Tokenized inputs using `bert-base-uncased`.
4. Built a multiple-choice model with `AutoModelForMultipleChoice`.
5. Applied LoRA adapters for parameter-efficient fine-tuning.
6. Prepared a Hugging Face Dataset compatible with the Trainer.
7. Performed a small LoRA fine-tuning experiment.
8. Generated answer probabilities using Softmax for inference.

---

## Key Concepts Learned

* Multiple-choice classification
* Prompt-option formatting
* Transformer tokenization
* Logits and Cross-Entropy Loss
* Softmax probability prediction
* LoRA (PEFT)
* Hugging Face Trainer and Dataset

---

## Challenges Faced

During implementation, I resolved several practical issues, including:

* CPU/GPU device mismatch
* Multiple-choice tensor formatting
* Trainer dataset preparation
* Tensor shape handling
* Transformers library compatibility

These challenges strengthened my understanding of PyTorch and Hugging Face workflows.

---

## Key Takeaways

This milestone introduced a transformer-based approach for multiple-choice question answering, where the model evaluates all answer options together instead of treating the task as standard text classification. I also learned how LoRA enables efficient fine-tuning by training only lightweight adapter layers, making transformer training faster and more memory-efficient.

---

## Future Work

* Fine-tune on the complete training dataset.
* Train for more epochs and evaluate with MAP@3.
* Compare Multiple-Choice BERT with my fine-tuned RoBERTa model.
* Integrate the best-performing model into the final Smart MCQ Solver application.

---

## Milestone Outcome

This milestone provided hands-on experience with multiple-choice transformers, LoRA-based fine-tuning, Hugging Face training workflows, and efficient inference techniques. These skills will serve as the foundation for developing more accurate and scalable MCQ solving models in future milestones.

