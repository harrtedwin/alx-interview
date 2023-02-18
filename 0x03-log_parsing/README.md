<p>
<img width="260" height="170" src="https://www.flaticon.com/free-icon/log_2125009?term=logs&page=1&position=3" align="right" >
</p>

# :colombia: 0x06. Log Parsing

- Write a script that reads stdin line by line and computes metrics:

  - Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
  - After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
    - Total file size: File size: <total size>
    - where <total size> is the sum of all previous <file size> (see input format above)
    - Number of lines by status code:
      - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
      - if a status code doesn’t appear, don’t print anything for this status code
      - format: <status code>: <number>
      - status codes should be printed in ascending order

## Prerequisites

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

## Built With

- Emacs
- Ubuntu 14.04 LTS

#### Compile

    `./0-generator.py | ./0-stats.py`

## Contributing

--Santiago Yanguas <br> - Holberton Student

## Versioning

For my learning of Interviews in Holberton School

## Authors

---Santiago Yanguas 946@holbertonshcool.com

## Files

| File               | Description       |
| ------------------ | ----------------- |
| **0-generator.py** | Generator of I.P  |
| **0-stats.py**     | Status of the I.P |
