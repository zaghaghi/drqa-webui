# DrQA
[DrQA](https://github.com/facebookresearch/DrQA.git) is a PyTorch implementation of the DrQA system described in the ACL 2017 paper [Reading Wikipedia to Answer Open-Domain Questions](https://arxiv.org/abs/1704.00051).

# DrQA Web UI
This is another way of interacting with DrQA.

# Installing
DrQA Web UI requires Linux/OSX and Python 3.5 or higher. 

1. Install DrQA
2. Install dependencies (`pip install -r requirements`)
3. Set `drqa_data_directory` in `services\__init__.py` to data directory of DrQA
4. Run (`gunicorn --timeout 300 index:app`)
5. Open [http://localhost:8000](http://localhost:8000)

# Screens

<p align="center"><img width="70%" src="screens/where-is-eiffel.png" /></p>

# HTML Template License
```
Copyright (c) 2018 by Andre Madarang (https://codepen.io/drehimself/pen/KdXwxR)


Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```