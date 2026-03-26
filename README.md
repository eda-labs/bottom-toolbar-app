# bottom-toolbar

An app to set the bottom toolbar of the SR Linux nodes to a user-provided message.

To try it out - spin up a free ["Try EDA" instance](https://docs.eda.dev/25.12/getting-started/try-eda/) on your laptop or [in Codespaces](https://docs.eda.dev/25.12/getting-started/codespaces/) and install the app.

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
