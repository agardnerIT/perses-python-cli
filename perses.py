import argparse
import json

PERSES_DASHBOARD_CREATOR = "0.0.1"

parser = argparse.ArgumentParser()
parser.add_argument('-op', '--operation', required=False, default="create", help="create")
parser.add_argument('-d','--dashboard-name', required=True, help="name of the dashboard")
parser.add_argument('-p','--project-name', required=False, default="proj1", help="project name. defaults to 'proj1'")
parser.add_argument('-path', '--dashboard-path', required=False, default=".", help="path to save dashboard. defaults to current directory.")
parser.add_argument('-dv', '--dashboard-version', required=False, default=0, help="dashboard version. defaults to 0")
parser.add_argument('-dur', '--duration', required=False, default="1h", help="dashboard duration. defaults to '1h'")
parser.add_argument('-refresh', '--refresh-interval', required=False, default="0s", help="dashboard refresh interval. defaults to '0s' (no auto refresh)")
parser.add_argument('-dr','--dry-run','--dry', required=False, default="False", help="run tool in dry mode only?")
parser.add_argument('-x', '--debug', required=False, default="False", help="run in debug mode to get extra output")
parser.add_argument('-v', '--version', action="version", version=PERSES_DASHBOARD_CREATOR)

args = parser.parse_args()

operation = args.operation
dashboard_name = args.dashboard_name
project_name = args.project_name
dashboard_path = args.dashboard_path
dashboard_version = args.dashboard_version
dashboard_duration = args.duration
dashboard_refresh_interval = args.refresh_interval
dry_run = args.dry_run
debug_mode = args.debug

print(f"Will perform op: {operation} on dashboard: {dashboard_name} at location: {dashboard_path} for project: {project_name} with duration: {dashboard_duration} and refresh interval: {dashboard_refresh_interval}")

dashboard_obj = {
    "kind": "Dashboard",
    "metadata": {
        "name": dashboard_name,
        "project": project_name,
        "version": 0
    },
    "spec": {
        "display": {
            "name": dashboard_name
        },
        "panels": {},
        "layouts": [],
        "variables": [],
        "duration": dashboard_duration,
        "refreshInterval": dashboard_refresh_interval
    }
}

filename = f"{dashboard_path}/{dashboard_name}.json"

with open(file=filename, mode="w") as dashboard_file:
    json.dump(dashboard_obj, dashboard_file)
