import os
from collections import Counter 

import pytest
from w3c_validator import validate
import bs4

DIR = "blog"
INDEX = f"{DIR}/post01.html"


@pytest.fixture
def elementos():
    return { 'p': 16, 'a': 12, 'li': 10, 'img': 8, 'strong': 6, 'code': 5,
    'header': 2, 'h3': 2, 'em': 2, 'ul': 2, 'button': 2, 'html': 1, 'head': 1,
    'meta': 1, 'link': 1, 'title': 1, 'body': 1, 'h1': 1, 'nav': 1, 'main': 1,
    'h2': 1, 'time': 1, 'ol': 1, 'aside': 1, 'h4': 1, 'footer': 1, }


@pytest.fixture
def source():
    if not os.path.exists(DIR):
        pytest.fail(f"diretório {DIR} não existe")
    if not os.path.exists(INDEX):
        pytest.fail(f"{INDEX} não existe")
    return open(INDEX).read()


@pytest.fixture
def html(source):
    return bs4.BeautifulSoup(source, 'html.parser')


def test_arquivos():
    assert os.path.exists(DIR), f"diretório {DIR} não encontrado"
    assert os.path.exists(INDEX), f"arquivo {INDEX} não encontrado"


def test_doctype(source):
    # teste baseado na especificação
    # ver: https://www.w3.org/TR/2010/WD-html-markup-20101019/syntax.html#doctype-syntax
    tokens = source.split("\n", 1)[0].lower().split()
    assert len(tokens) in [2, 3] and \
           tokens[0] == '<!doctype' and \
           tokens[1].startswith('html') and \
           tokens[-1].endswith('>'), "doctype inválido"


def test_elementos(html, elementos):
    encontados = Counter(e.name for e in html.findChildren())
    assert encontados == elementos


def test_w3c_validator():
    report = validate(INDEX)
    assert not report['messages'], "html não passa no w3c validator"
