# Bottom-toolbar Application

-{{% import 'icons.html' as icons %}}-

| <nbsp> {: .hide-th } |                                         |
| -------------------- |-----------------------------------------|
| **Group/Version**    | -{{ app_group }}-/-{{ app_api_version }}-   |
| **Supported OS**     | -{{ supported_os_versions() }}-  |
| **Catalog**          | [eda-labs/catalog/bottom-toolbar][manifest] |
| **Source Code**      | <small>coming soon</small>              |

[manifest]: https://github.com/eda-labs/catalog/blob/apps/bottom-toolbar.eda.labs/v0.0.0/apps/bottom-toolbar.eda.labs/manifest.yaml

An app to set the bottom toolbar of the SR Linux nodes to a user-provided message.

## Install

Add the `eda-labs` catalog to your EDA instance:

```yaml
apiVersion: appstore.eda.nokia.com/v1
kind: Catalog
metadata:
  name: eda-labs-catalog
  namespace: eda-system
spec:
  remoteType: git
  remoteURL: https://github.com/eda-labs/catalog.git
  skipTLSVerify: false
  title: EDA Labs Catalog
```

And install the Bootom Toolbar app from it. The **Bottom Toolbars** resource group will be available in the **Management** category.
