"""Issue a Forward SAT, make one read-only business call, then revoke the SAT.

Set QODER_SA_KEY and QODER_SA_REGION=cn|global. Set QODER_IDENTITY_ID for Identity mode.
Run: python -m examples.auth.forward_tokens
"""

import argparse
import os

from qca import Forward


def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    region = os.environ.get("QODER_SA_REGION", "cn")
    if region not in ("cn", "global"):
        raise ValueError("QODER_SA_REGION must be cn or global")
    host = "https://api.qoder.com.cn" if region == "cn" else "https://api.qoder.com"
    base_url = f"{host}/api/v1/forward"
    sa_key = os.environ["QODER_SA_KEY"]
    identity_id = os.environ.get("QODER_IDENTITY_ID")
    with Forward(base_url=base_url, auth_mode="sa") as issuer:
        params = {"sa_key": sa_key, "ttl_seconds": 600, "metadata": {"purpose": "sdk example"}}
        token = (
            issuer.identities.service_account_tokens.create(identity_id, **params)
            if identity_id
            else issuer.service_account_tokens.create(**params)
        )
        try:
            with Forward(base_url=base_url, auth_mode="sa", access_token=token.access_token, max_retries=0) as runtime:
                if identity_id:
                    page = runtime.sessions.list(identity_i_ds=[identity_id], limit=1)
                    print("Identity sessions:", len(page.data))
                else:
                    print("Forward templates:", len(runtime.templates.list(limit=1).data))
        finally:
            issuer.service_account_tokens.revoke(
                token.auth_token_id,
                sa_key=sa_key,
                target_credential_id=token.credential_id,
                target_expires_at=token.expires_at,
                reason="sdk example complete",
                timeout=30,
            )


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Forward token example failed: {type(error).__name__}")
        raise SystemExit(1) from None
