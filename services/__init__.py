#!/usr/bin/env python3
# Copyright 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
# This code borrowed from https://github.com/facebookresearch/DrQA.git

import torch
import os

from drqa import pipeline
from drqa.retriever import utils
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
fmt = logging.Formatter('%(asctime)s: [ %(message)s ]', '%m/%d/%Y %I:%M:%S %p')
console = logging.StreamHandler()
console.setFormatter(fmt)
logger.addHandler(console)

drqa_data_directory = '../DrQA/data'

config = {
    'reader-model': os.path.join(drqa_data_directory, 'reader', 'multitask.mdl'),
    'retriever-model': os.path.join(drqa_data_directory, 'wikipedia', 'docs-tfidf-ngram=2-hash=16777216-tokenizer=simple.npz'),
    'doc-db': os.path.join(drqa_data_directory, 'wikipedia', 'docs.db'),
    'embedding-file': None,
    'tokenizer': 'spacy',
    'no-cuda': True,
    'gpu': 0
}

cuda = torch.cuda.is_available() and not config.get('no-cuda', False)
if cuda:
    torch.cuda.set_device(config.get('gpu', 0))
    logger.info('CUDA enabled (GPU %d)' % config.get('gpu', 0))
else:
    logger.info('Running on CPU only.')

logger.info('Initializing pipeline...')
DrQA = pipeline.DrQA(
    cuda=cuda,
    reader_model=config['reader-model'],
    ranker_config={'options': {'tfidf_path': config['retriever-model']}},
    db_config={'options': {'db_path': config['doc-db']}},
    tokenizer=config['tokenizer'],
    embedding_file=config['embedding-file'],
)


def process(question, candidates=None, top_n=1, n_docs=5):
    predictions = DrQA.process(
        question, candidates, top_n, n_docs, return_context=True
    )
    answers = []
    for i, p in enumerate(predictions, 1):
        answers.append({
            'index': i,
            'span': p['span'],
            'doc_id': p['doc_id'],
            'span_score': '%.5g' % p['span_score'],
            'doc_score': '%.5g' % p['doc_score'],
            'text': p['context']['text'],
            'start': p['context']['start'],
            'end': p['context']['end']
        })
    return answers

