#!/usr/bin/env python3
# Auto-generated classes based on your _types.go file (with special logic for CRDs that embed metav1.ObjectMeta)
# The change on this file will be overwritten by running edabuilder create or generate.
import eda_common as eda

from . import Metadata, Y_NAME

from .constants import *

ENUM_HTTPPROXYSPECAUTHTYPE_ATDESTINATION = 'atDestination'
ENUM_HTTPPROXYSPECAUTHTYPE_INAPISERVER = 'inApiServer'
Y_ROOTURL = 'rootUrl'
Y_AUTHTYPE = 'authType'
# Package objects (GVK Schemas)
HTTPPROXY_SCHEMA = eda.Schema(group='core.eda.nokia.com', version='v1', kind='HttpProxy')


class HttpProxySpec:
    def __init__(
        self,
        rootUrl: str,
        authType: str,
    ):
        self.rootUrl = rootUrl
        self.authType = authType

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.rootUrl is not None:
            _rval[Y_ROOTURL] = self.rootUrl
        if self.authType is not None:
            _rval[Y_AUTHTYPE] = self.authType
        return _rval

    @staticmethod
    def from_input(obj) -> 'HttpProxySpec | None':
        if obj:
            _rootUrl = obj.get(Y_ROOTURL)
            _authType = obj.get(Y_AUTHTYPE)
            return HttpProxySpec(
                rootUrl=_rootUrl,
                authType=_authType,
            )
        return None  # pragma: no cover


class HttpProxyStatus:
    def __init__(
        self,
    ):
        pass

    def to_input(self):  # pragma: no cover
        _rval = {}
        return _rval

    @staticmethod
    def from_input(obj) -> 'HttpProxyStatus | None':
        if obj:
            return HttpProxyStatus(
            )
        return None  # pragma: no cover


class HttpProxy:
    def __init__(
        self,
        metadata: Metadata | None = None,
        spec: HttpProxySpec | None = None,
        status: HttpProxyStatus | None = None
    ):
        self.metadata = metadata
        self.spec = spec
        self.status = status

    def to_input(self):  # pragma: no cover
        _rval = {}
        _rval[Y_SCHEMA_KEY] = HTTPPROXY_SCHEMA
        if self.metadata is not None:
            _rval[Y_NAME] = self.metadata.name
        if self.spec is not None:
            _rval[Y_SPEC] = self.spec.to_input()
        if self.status is not None:
            _rval[Y_STATUS] = self.status.to_input()
        return _rval

    @staticmethod
    def from_input(obj) -> 'HttpProxy | None':
        if obj:
            _metadata = (
                Metadata.from_input(obj.get(Y_METADATA))
                if obj.get(Y_METADATA, None)
                else Metadata.from_name(obj.get(Y_NAME))
            )
            _spec = HttpProxySpec.from_input(obj.get(Y_SPEC, None))
            _status = HttpProxyStatus.from_input(obj.get(Y_STATUS))
            return HttpProxy(
                metadata=_metadata,
                spec=_spec,
                status=_status,
            )
        return None  # pragma: no cover


class HttpProxyList:
    def __init__(
        self,
        items: list[HttpProxy],
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
    def from_input(obj) -> 'HttpProxyList | None':
        if obj:
            _items = obj.get(Y_ITEMS, [])
            _listMeta = obj.get(Y_METADATA, None)
            return HttpProxyList(
                items=_items,
                listMeta=_listMeta,
            )
        return None  # pragma: no cover
