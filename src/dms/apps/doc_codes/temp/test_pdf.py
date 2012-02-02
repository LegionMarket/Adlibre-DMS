"""
Module: Example DocCodes for Adlibre DMS
Project: Adlibre DMS
Copyright: Adlibre Pty Ltd 2012
License: See LICENSE for license information
"""

import re

from doc_codes import Doccode

class TestPDFDoccode(Doccode):
    title = 'Test PDFs'
    description = '[a-z]{5}[0-9]{3}'
    active = True
    doccode_id = 1

    def validate(self, document_name):
        if re.match("^[a-z]{5}[0-9]{3}$", document_name):
            return True
        return False

    def split(self, document_name):
        d = [ document_name[0:5], document_name[5:8], document_name]
        return d