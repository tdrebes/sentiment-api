# Embeddings Generation API

```bash
conda create -n sentiment-api python=3.12
conda activate sentiment-api
pip install -r requirements.txt
python download_models.py
```

# Build
```bash
docker image build -t sentiment-api .
```

# Run

```bash
docker run -p 5001:5001 sentiment-api
```
