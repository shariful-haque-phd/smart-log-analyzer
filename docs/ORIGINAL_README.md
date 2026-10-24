# Smart Log Analyzer

Groups recurring application errors by normalized message template and reports frequency, severity, and examples.

## Usage
```bash
python src/analyze_logs.py sample/app.log --top 20
```

The normalizer replaces timestamps, UUIDs, IP addresses, and numbers so repeated failures with different IDs are grouped together.
