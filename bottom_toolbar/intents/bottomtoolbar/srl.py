#!/usr/bin/env python3
import json

import eda_common as eda

from bottom_toolbar.api.v1alpha1.pysrc.bottomtoolbar import BottomToolbar
from common.metadata import Y_METADATA, Y_NAME
from core.pysrc import nodeconfig
from core.pysrc.nodeconfig import NodeConfig, NodeConfigTupleSpec
from utils.log import log_msg


class SrlBaseConfigHandler:
    def handle_cr(self, cr_obj: BottomToolbar, node_cr=None):
        log_msg(f"cr_obj: {cr_obj}")
        log_msg(f"node_cr: {node_cr}")

        node_name = node_cr[Y_METADATA][Y_NAME]

        configs = self._generate_config(cr_obj)

        node_config = NodeConfig(
            metadata=nodeconfig.Metadata(
                name=f"bottom-toolbar-{cr_obj.metadata.name}-{node_name}",
            ),
            spec=nodeconfig.NodeConfigSpec(
                node_endpoint=node_name,
                configs=configs,
            ),
        )

        eda.update_cr(**node_config.to_input())

    def _generate_config(self, cr_obj: BottomToolbar) -> list[NodeConfigTupleSpec]:
        configs: list[NodeConfigTupleSpec] = []
        # cli config (in .system.cli context)
        _config = {}

        if cr_obj.spec.message:
            _config.setdefault("cli", {}).setdefault("environment", {})["bottom-toolbar"] = cr_obj.spec.message

        configs.append(
            NodeConfigTupleSpec(
                path=".system",
                operation="Create",
                config=json.dumps(_config),
            ),
        )

        return configs
