# jsonl
A simple extension of the Python `json` module to allow for quick jsonl reading/writing

## Usage
Import `jsonl` instead of the standard `json` module
```python
import jsonl
```

## Loading 

### Load file
```python
  jsonl.load_jsonl(filename)
```

### Load from string
```python
  jsonl.loads_jsonl(jsonl_string)
```

## Dumping 

### Dump to file
```python
  jsonl.dump_jsonl(object, filename)
```

### Dump to string
```python
  jsonl.dumps_jsonl(object)
```

## Regular json usage
All other methods in the standard `json` module are imported by jsonl, so you can still use:

- `jsonl.load(fp)`
- `jsonl.dump(obj,fp)`

etc.
