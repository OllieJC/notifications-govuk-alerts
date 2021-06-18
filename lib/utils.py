import hashlib
import re
from pathlib import Path
from shutil import copyfile
from jinja2 import Markup, escape

REPO = Path('.')
SRC = REPO / 'src'
DIST = REPO / 'dist'
ROOT = DIST / 'alerts'


def paragraphize(value, classes="govuk-body-l govuk-!-margin-bottom-4"):
    paragraphs = [
        f'<p class="{classes}">{line}</p>'
        for line in escape(value).split('\n')
        if line
    ]
    return Markup('\n\n'.join(paragraphs))


def file_fingerprint(path, root=DIST):
    fullpath = f"{root}{path}"
    contents = open(fullpath, 'rb').read()

    hash = hashlib.md5(contents).hexdigest()
    newpath = re.sub(r'^(.*)\.(.+?)$', rf'\1-{hash}.\2', path)
    copyfile(fullpath, f"{root}{newpath}")

    return newpath

