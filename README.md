# perses-python-cli

Python CLI to create and manage Perses dashboards

## Available Parameters

- `--dashboard-name`
- `--dashboard-path` (optional. defaults to current directory)
- `--project-name` (optional. defaults to `proj1`)
- `--dashboard-version` (optional. defaults to `0`)
- `--duration` (optional. defaults to `1h`)
- `--refresh-interval` (optional. defaults to `0s`)
- `--dry-run` (optional. defaults to `False`)
- `--debug` (optional. defaults to `False`)
- `--version` (prints version of this CLI and exits)

## Create a dashboard

This is the minimal working example. Relies on above defaults.

Create a dashboard called `foo` and save it as `./foo.json`

```sh {"id":"01J5FPD49C4A85T452HRPY5DVC"}
python perses.py --dashboard-name foo
```
