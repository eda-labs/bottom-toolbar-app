---
resource_name: BottomToolbar
resource_name_plural: bottomtoolbars
resource_name_plural_title: Bottom Toolbars
resource_name_acronym: BT
---

# Bottom Toolbar

-{{% import 'icons.html' as icons %}}-

-{{ category(resource_name_plural ) }}- → -{{ icons.circle(letter=resource_name_acronym, text=resource_name_plural_title) }}-

A description of this resource should go here.

## Dependencies

..

## Referenced resources

..

## Examples

/// tab | YAML

```yaml
-{{ include_snippet(resource_name) }}-
```

///

/// tab | `kubectl`

```bash
cat << 'EOF' | kubectl apply -f -
-{{ include_snippet(resource_name) }}-
EOF
```

///

## Custom Resource Definition

To browse the Custom Resource Definition go to [crd.eda.dev](https://crd.eda.dev/-{{ resource_name_plural }}-.-{{ app_group }}-/-{{ app_api_version }}-).

/// details | Custom Resource Definition YAML
    type: subtle-note

```{.yaml .code-scroll-lg}
-{{ include_crd(resource_name_plural) }}-
```

///
