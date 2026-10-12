"""Exchange an SA Key automatically; list Forward templates and Managed agents.

Set QODER_SA_KEY and QODER_SA_REGION=cn|global in the process environment.
Run: python -m examples.auth.sa_key [--async]
"""

import argparse
import asyncio
import os

from qca import (
    AsyncForward,
    AsyncManaged,
    AsyncServiceAccountCredential,
    Forward,
    Managed,
    ServiceAccountCredential,
)


def config():
    if os.environ.get("QODER_ACCESS_TOKEN"):
        raise ValueError("Unset QODER_ACCESS_TOKEN before running the SA Key example")
    region = os.environ.get("QODER_SA_REGION", "cn")
    if region not in ("cn", "global"):
        raise ValueError("QODER_SA_REGION must be cn or global")
    host = "https://api.qoder.com.cn" if region == "cn" else "https://api.qoder.com"
    return dict(sa_key=os.environ["QODER_SA_KEY"], region=region, scopes=["qca.access", "forward.access"]), host


def main():
    options, host = config()
    with ServiceAccountCredential(**options) as credential:
        with (
            Forward(credential=credential, base_url=f"{host}/api/v1/forward", max_retries=0) as forward,
            Managed(credential=credential, base_url=f"{host}/api/v1/cloud", max_retries=0) as managed,
        ):
            print("Forward templates:", len(forward.templates.list(limit=1).data))
            print("Managed agents:", len(managed.agents.list(limit=1).data))


async def async_main():
    options, host = config()
    async with AsyncServiceAccountCredential(**options) as credential:
        async with (
            AsyncForward(credential=credential, base_url=f"{host}/api/v1/forward", max_retries=0) as forward,
            AsyncManaged(credential=credential, base_url=f"{host}/api/v1/cloud", max_retries=0) as managed,
        ):
            print("Forward templates:", len((await forward.templates.list(limit=1)).data))
            print("Managed agents:", len((await managed.agents.list(limit=1)).data))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--async", dest="use_async", action="store_true")
    args = parser.parse_args()
    try:
        asyncio.run(async_main()) if args.use_async else main()
    except Exception as error:
        # Avoid dumping authentication headers from an HTTP error traceback.
        print(f"SA Key example failed: {type(error).__name__}")
        raise SystemExit(1) from None
