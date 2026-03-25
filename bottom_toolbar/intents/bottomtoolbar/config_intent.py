#!/usr/bin/env python3
import eda_common as eda
import utils.node_utils as nutils
import utils.exceptions as e
import bottom_toolbar.api.v1alpha1.pysrc.constants as c

from common.constants import PLATFORM_SRL, PLATFORM_SROS
from utils.log import log_msg

from bottom_toolbar.api.v1alpha1.pysrc.bottomtoolbar import BottomToolbar
from bottom_toolbar.intents.bottomtoolbar.handlers import get_config_handler
from bottom_toolbar.intents.bottomtoolbar.init import init_globals_defaults, validate

def process_cr(cr):
    """Process BottomToolbar CR."""
    log_msg("BottomToolbar CR:", dict=cr)
    cr_obj = BottomToolbar.from_input(cr)
    if cr_obj is None:
        return

    cr_name = cr_obj.metadata.name
    validate(cr_obj)
    init_globals_defaults(cr_obj)
