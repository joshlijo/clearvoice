## ClearVoice

ClearVoice is a lightweight speech enhancement tool that removes background noise from audio recordings using DeepFilterNet.
It supports single-file and batch audio enhancement, making it easy to clean noisy speech samples with a pretrained neural model.

## Features

Noise suppression using DeepFilterNet3
Batch processing for multiple .wav files
CPU-friendly inference
Clean, modular Python codebase

## Architecture

Pretrained DeepFilterNet3 model loaded once and reused
Stateless audio enhancement pipeline
Separate core logic and execution scripts for scalability

## Quick Usage
```
python -m scripts.batch_enhance
```
Input files go in:
```
samples/noisy/
```
Enhanced outputs are saved to:
```
outputs/enhanced/
```
