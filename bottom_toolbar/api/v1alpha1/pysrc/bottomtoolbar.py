#!/usr/bin/env python3
# Auto-generated classes based on your _types.go file (with special logic for CRDs that embed metav1.ObjectMeta)
# The change on this file will be overwritten by running edabuilder create or generate.
import eda_common as eda

from . import Metadata, Y_NAME

from .constants import *
Y_FOO = 'foo'
Y_RESULT = 'result'
# Package objects (GVK Schemas)
BOTTOMTOOLBAR_SCHEMA = eda.Schema(group='bottom-toolbar.eda.labs', version='v1alpha1', kind='BottomToolbar')


class BottomToolbarSpec:
    def __init__(
        self,
        foo: str,
    ):
        self.foo = foo

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.foo is not None:
            _rval[Y_FOO] = self.foo
        return _rval

    @staticmethod
    def from_input(obj) -> 'BottomToolbarSpec | None':
        if obj:
            _foo = obj.get(Y_FOO)
            return BottomToolbarSpec(
                foo=_foo,
            )
        return None  # pragma: no cover


class BottomToolbarStatus:
    def __init__(
        self,
        result: str | None = None,
    ):
        self.result = result

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.result is not None:
            _rval[Y_RESULT] = self.result
        return _rval

    @staticmethod
    def from_input(obj) -> 'BottomToolbarStatus | None':
        if obj:
            _result = obj.get(Y_RESULT)
            return BottomToolbarStatus(
                result=_result,
            )
        return None  # pragma: no cover


class BottomToolbar:
    def __init__(
        self,
        metadata: Metadata | None = None,
        spec: BottomToolbarSpec | None = None,
        status: BottomToolbarStatus | None = None
    ):
        self.metadata = metadata
        self.spec = spec
        self.status = status

    def to_input(self):  # pragma: no cover
        _rval = {}
        _rval[Y_SCHEMA_KEY] = BOTTOMTOOLBAR_SCHEMA
        if self.metadata is not None:
            _rval[Y_NAME] = self.metadata.name
        if self.spec is not None:
            _rval[Y_SPEC] = self.spec.to_input()
        if self.status is not None:
            _rval[Y_STATUS] = self.status.to_input()
        return _rval

    @staticmethod
    def from_input(obj) -> 'BottomToolbar | None':
        if obj:
            _metadata = (
                Metadata.from_input(obj.get(Y_METADATA))
                if obj.get(Y_METADATA, None)
                else Metadata.from_name(obj.get(Y_NAME))
            )
            _spec = BottomToolbarSpec.from_input(obj.get(Y_SPEC, None))
            _status = BottomToolbarStatus.from_input(obj.get(Y_STATUS))
            return BottomToolbar(
                metadata=_metadata,
                spec=_spec,
                status=_status,
            )
        return None  # pragma: no cover


class BottomToolbarList:
    def __init__(
        self,
        items: list[BottomToolbar],
        listMeta: object | None = None
    ):
        self.items = items
        self.listMeta = listMeta

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.items is not None:
            _rval[Y_ITEMS] = self.items
        if self.listMeta is not None:
            _rval[Y_METADATA] = self.listMeta
        return _rval

    @staticmethod
    def from_input(obj) -> 'BottomToolbarList | None':
        if obj:
            _items = obj.get(Y_ITEMS, [])
            _listMeta = obj.get(Y_METADATA, None)
            return BottomToolbarList(
                items=_items,
                listMeta=_listMeta,
            )
        return None  # pragma: no cover
