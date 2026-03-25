#!/usr/bin/env python3
import eda_common as eda

import bottom_toolbar.api.v1alpha1.pysrc.constants as c
import utils.exceptions as e
import utils.node_utils as nutils
from bottom_toolbar.api.v1alpha1.pysrc.bottomtoolbar import BottomToolbar
from bottom_toolbar.intents.bottomtoolbar.handlers import get_config_handler
from bottom_toolbar.intents.bottomtoolbar.init import init_globals_defaults, validate
from common.constants import PLATFORM_SRL, PLATFORM_SROS
from common.metadata import Y_METADATA, Y_NAME
from utils.log import log_msg


def process_cr(cr):
    """Process BottomToolbar CR."""
    log_msg("BottomToolbar CR:", dict=cr)
    cr_obj = BottomToolbar.from_input(cr)
    if cr_obj is None:
        return

    validate(cr_obj)
    init_globals_defaults(cr_obj)

    for node in nutils.list_nodes(filter=[], label_filter=[], ns=cr_obj.metadata.namespace):
        log_msg(f"Node: {node[Y_METADATA][Y_NAME]}")

        if node.get("spec", None) is not None and node["spec"].get("operatingSystem", None) is not None:
            if node["spec"]["operatingSystem"] == PLATFORM_SRL:
                srl_handler = get_config_handler(PLATFORM_SRL)
                srl_handler.handle_cr(cr_obj, node_cr=node)
            else:
                log_msg(f"Node OS not supported: {node['spec']['operatingSystem']}")
                continue
