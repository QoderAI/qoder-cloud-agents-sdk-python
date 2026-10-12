"""Use an existing SAT; the caller is responsible for replacing expired tokens.

Set QODER_ACCESS_TOKEN and QODER_SA_REGION=cn|global in the process environment.
Run: python -m examples.auth.sa_token
"""

import os

from qca import Forward, Managed


def main():
    if os.environ.get("QODER_SA_KEY"):
        raise ValueError("Unset QODER_SA_KEY before running the SAT example")
    region = os.environ.get("QODER_SA_REGION", "cn")
    if region not in ("cn", "global"):
        raise ValueError("QODER_SA_REGION must be cn or global")
    host = "https://api.qoder.com.cn" if region == "cn" else "https://api.qoder.com"
    token = os.environ["QODER_ACCESS_TOKEN"]
    with (
        Forward(auth_mode="sa", access_token=token, base_url=f"{host}/api/v1/forward", max_retries=0) as forward,
        Managed(auth_mode="sa", access_token=token, base_url=f"{host}/api/v1/cloud", max_retries=0) as managed,
    ):
        print("Forward templates:", len(forward.templates.list(limit=1).data))
        print("Managed agents:", len(managed.agents.list(limit=1).data))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"SAT example failed: {type(error).__name__}")
        raise SystemExit(1) from None
