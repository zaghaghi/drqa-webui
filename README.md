# DrQA
[DrQA](https://github.com/facebookresearch/DrQA.git) is a PyTorch implementation of the DrQA system described in the ACL 2017 paper [Reading Wikipedia to Answer Open-Domain Questions](https://arxiv.org/abs/1704.00051).

# DrQA Web UI
This is another way of interacting with DrQA.

# Installing
DrQA Web UI requires Linux/OSX and Python 3.5 or higher. 

1. Install DrQA
2. Install dependencies (`pip install -r requirements`)
3. Set `drqa_data_directory` in `services\__init__.py` to data directory of DrQA
4. Run (`gunicorn --timeout 300 index:app)
5. Open [http://localhost:8000](http://localhost:8000)

# Screens

<p align="center"><img width="70%" src="screens/where-is-eiffel.png" /></p>
