#!/usr/bin/env python3
import json

import eda_common as eda
import utils.schema as s
from common.metadata import Y_METADATA, Y_NAME
from bottom_toolbar.api.v1alpha1.pysrc.bottomtoolbar import BottomToolbar


class EdaBaseConfigHandler:
    def handle_cr(self, cr_obj: BottomToolbar):
        # implement this
        pass
