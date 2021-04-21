# jsonl
A simple extension of the Python `json` module to allow for quick reading/writing of the JSONL file format.

# What is JSONL?
JSONL (or JSON Lines) is a text format that uses newline-delimited JSON.
>  ... the JSON Lines text format, also called newline-delimited JSON. JSON Lines is a convenient format for storing structured data that may be processed one record at a time. It works well with unix-style text processing tools and shell pipelines. It's a great format for log files. It's also a flexible format for passing messages between cooperating processes.
>  
from [JSONLines.org](https://jsonlines.org/)

JSONL files have three properties:
1. UTF-8 encoding
2. Each line is valid JSON
3. The line separator is `\n`

The standard python `json` module does not have any convenience methods for reading/writing JSONL files, so this module is a simple extension of it to include just that.


# Methods
The `jsonl` module adds four methods that have direct counterparts in the `json` package.

||json|jsonl
|--|--|--|
|Load file|`json.load`  |`jsonl.load_jsonl`|
|Dump file|`json.dump`  |`jsonl.dump_jsonl`|
|Load string|`json.loads`  |`jsonl.loads_jsonl`|
|Dump string|`json.dumps`  |`jsonl.dumps_jsonl`|


# Usage
The `jsonl` module imports everything from the `json` module, so that all methods can be accessed from one source (so for example you can call `jsonl.loads` to access the `json.loads` method). As a result of this,  the `jsonl` module can be imported in place of the standard `json` module for convenienvce
```python
import jsonl as json
```
All of the regular `json` module methods will still be accessible, as well as the additional methods for JSONL. 

**Note: All of the examples below assume that `jsonl` has been imported as `json`.**



## Loading a JSONL file
A JSONL file can be loaded using the `load_jsonl` method in the same way a JSON file is loaded using the `load` method. 

Take the example file `/examples/people.jsonl`:
```json
{"name": "John Doe", "age": 45}
{"name": "Jane Doe", "age": 43, "contact":{"email": {"jane@example.com"} }
```
This file can be loaded as follows:
```python
with open('examples/people.jsonl') as rfile:
    people= json.load_jsonl(rfile)
```
This will create  `people` , a list of dictionaries, as below:
```python 
>>> people
>>> [{'name': 'John Doe', 'age': 41, 'active': False},
 {'name': 'Jane Doe',
  'age': 39,
  'active': True,
  'contact': {'email': 'jane@example.com'}}
  ]
```

## Writing a JSONL file
A list of JSON-serializable python objects can be written to a JSONL file using the `jsonl_dump` method in a similar way to how a single JSON-serializable python object can be written to a JSON file using the `dump` method.

Suppose you have the same list as before:
```python
people= [{'name': 'John Doe', 'age': 41, 'active': False},
 {'name': 'Jane Doe',
  'age': 39,
  'active': True,
  'contact': {'email': 'jane@example.com'}}]
```
This can be output to `people_output.jsonl` as follows:

```python
with open('people_output.jsonl','w') as wfile:
    json.dump_jsonl(people, wfile)
```
This will write out a file that is identical to `example.jsonl`.

## JSONL Strings
JSONL strings can also be loaded and created. JSONL strings  are simply JSON-formatted strings that are delimited by the newline character `\n`

For example, take the following list of dictionaries:
```python
states = [
  {"name": "New York", "code":"NY"},
  {"name": "Illinois", "code":"IL"},
  {"name": "Texas", "code":"TX"}
]
```
This list of objects can be converted to newline-delimited JSON-formatted strings using `dumps_jsonl` in the same way a single object can be converted to a JSON-formatted string using `dumps`

```python
>>> json.dumps_jsonl(states)
>>> '{"name": "New York", "code": "NY"}\n{"name": "Illinois", "code": "IL"}\n{"name": "Texas", "code": "TX"}'
```
Similarly, a JSONL string can be read back in as an object using the `loads_jsonl` method:

```python
>>> jsonl_string = '{"name": "New York", "code": "NY"}\n{"name": "Illinois", "code": "IL"}\n{"name": "Texas", "code": "TX"}'
>>> json.loads_jsonl(jsonl_string)
>>> [
  {'name': 'New York', 'code': 'NY'},
  {'name': 'Illinois', 'code': 'IL'},
  {'name': 'Texas', 'code': 'TX'}
]
```

## Regular JSON usage
All other methods in the standard `json` module are imported by `jsonl`. If you have imported `jsonl` as `json` then you can directly call `json.dump`, `json.load` as normal.


## References
- [JSONL specification](https://jsonlines.org/)
