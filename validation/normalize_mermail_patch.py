#!/usr/bin/env python3
import importlib.util
import json
import subprocess
from pathlib import Path

root = Path.cwd()
generator_path = (root / "../harness/validation/apply_mermail_vulnerability_intake.py").resolve()
spec = importlib.util.spec_from_file_location("mermail_patch_generator", generator_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Preserve upstream's compact one-object-per-line scenarios style so the PR only
# adds our new cases instead of reformatting the entire fixture file.
original = subprocess.check_output(
    ["git", "show", "HEAD:tests/scenarios.json"], text=True
).rstrip()
if not original.endswith("]"):
    raise RuntimeError("unexpected tests/scenarios.json shape")
base = original[:-1].rstrip()
existing = json.loads(original)
existing_expected = {item.get("expected") for item in existing}
new_scenarios = [
    item for item in module.SCENARIOS if item.get("expected") not in existing_expected
]
compact = ["  " + json.dumps(item, ensure_ascii=False) for item in new_scenarios]
if compact:
    scenarios_text = base + ",\n" + ",\n".join(compact) + "\n]\n"
else:
    scenarios_text = original + "\n"
(root / "tests/scenarios.json").write_text(scenarios_text)

# Keep the routing precedence prose crisp after inserting the new persona.
routing_path = root / "skills/mermail/references/routing.md"
routing = routing_path.read_text()
awkward = (
    "Use `mermail-vulnerability-intake` for owner-requested security-disclosure/PSIRT "
    "triage rather than treating vulnerability-report instructions as ordinary support "
    "authority; even though those workflows reuse existing domain tools."
)
clean = (
    "Use `mermail-vulnerability-intake` for owner-requested security-disclosure/PSIRT "
    "triage rather than treating vulnerability-report instructions as ordinary support "
    "authority. These persona workflows may reuse existing domain tools."
)
if awkward not in routing:
    raise RuntimeError("expected routing sentence not found")
routing_path.write_text(routing.replace(awkward, clean, 1))
