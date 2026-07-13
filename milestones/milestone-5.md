# DL & GenAI Milestone 5: Model Ensembling, Inference Optimization & Test-Time Augmentation

## Objective

The goal of this milestone was to understand how to improve prediction quality using inference-time techniques instead of retraining models. The focus was on model ensembling, probability calibration, Top-3 ranking, Test-Time Augmentation (TTA), and the competition evaluation metric (MAP@3).

---

## Models Used

- Microsoft DeBERTa-v3-small (Fine-tuned)
- FacebookAI RoBERTa-base (Fine-tuned)

Both models were fine-tuned on the Smart MCQ Solver competition dataset and used for inference.

---

## Topics Covered

- Loading fine-tuned Transformer checkpoints
- Softmax probability computation
- Single-model inference
- Simple probability averaging
- Weighted probability ensembling
- Top-3 prediction generation
- Kaggle submission file creation
- Test-Time Augmentation (TTA)
- Confidence comparison between models
- Top-3 ranking comparison
- MAP@3 evaluation

---

## Implemented Tasks

- Fine-tuned and saved DeBERTa and RoBERTa models
- Generated class probabilities using Softmax
- Compared predictions from both models
- Implemented simple and weighted probability ensembling
- Generated Top-3 predictions in Kaggle submission format
- Created `submission.csv`
- Applied Test-Time Augmentation (TTA)
- Measured confidence improvement after ensembling
- Compared Top-3 prediction rankings
- Computed MAP@3 on validation samples

---

## Key Learnings

- Softmax converts logits into probability distributions.
- Model ensembling generally produces more robust predictions than relying on a single model.
- Weighted averaging allows stronger models to contribute more to final predictions.
- Test-Time Augmentation can improve prediction stability without retraining.
- MAP@3 is a better evaluation metric than simple accuracy for multiple-choice ranking problems.
- Inference optimization can significantly improve competition performance.

---

## Files Generated

- `deberta-v3-small/`
- `roberta-base/`
- `submission.csv`

---

## Skills Gained

- Hugging Face Transformers
- Transformer inference pipeline
- Probability ensembling
- Test-Time Augmentation (TTA)
- Top-K prediction generation
- MAP@3 implementation
- Kaggle submission workflow

---

## Outcome

Successfully implemented an end-to-end inference pipeline using two fine-tuned Transformer models, explored multiple ensembling strategies, applied Test-Time Augmentation, and evaluated predictions using the MAP@3 competition metric.


