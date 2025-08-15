# pyoxidizer.bzl — minimal working config for operator_update_map.py

def make_exe():
    dist = default_python_distribution()          # Python 3.8–3.10
    policy = dist.make_python_packaging_policy()
    policy.resources_location = "in-memory"       # true single-binary behavior
    policy.resources_location_fallback = "filesystem-relative:lib"

    config = dist.make_python_interpreter_config()
    # Run your script's main() on start
    config.run_command = r'''
import operator_update_map as app
import sys
sys.exit(app.main())
'''

    exe = dist.to_python_executable(
        name = "operator_update_map",
        packaging_policy = policy,
        config = config,
    )

    # Package your script in-memory
    for res in exe.read_python_resources_from(directory = CWD):
        res.add_location = "in-memory"
        exe.add_python_resource(res)

    # Third-party deps
    for res in exe.pip_install(["requests", "urllib3"]):
        res.add_location = "in-memory"
        exe.add_python_resource(res)

    # If you will use --verify-ssl and want cert validation ON, also add certifi:
    # for res in exe.pip_install(["certifi"]):
    #     if res.is_file and res.target_path.endswith("certifi/cacert.pem"):
    #         res.add_location = "filesystem-relative:certifi"  # write real PEM next to EXE
    #     else:
    #         res.add_location = "in-memory"
    #     exe.add_python_resource(res)

    return exe

# ***** IMPORTANT: register a build target *****
# Newer PyOxidizer:
def resolve_targets():
    return {"exe": make_exe()}

# Older PyOxidizer (uncomment this block instead if your version expects it):
# def register_targets(context):
#     context.targets["exe"] = make_exe()
