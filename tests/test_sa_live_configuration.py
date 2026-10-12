import pytest

from tests.sa.config import sa_environment


def test_sa_env_file_and_process_precedence(tmp_path):
    path = tmp_path / "sa.env"
    path.write_text(
        "QODER_SA_CN_KEY='file-cn'\nexport QODER_SA_GLOBAL_KEY=file-global # comment\n"
        "QODER_SA_MODEL=$(do-not-execute)\n"
    )
    values = sa_environment(path, {"QODER_SA_CN_KEY": "process-cn"}, ["cn", "global"], execution=False)
    assert values["QODER_SA_CN_KEY"] == "process-cn"
    assert values["QODER_SA_GLOBAL_KEY"] == "file-global"
    assert values["QODER_SA_MODEL"] == "$(do-not-execute)"
    with pytest.raises(ValueError, match="QODER_SA_GLOBAL_KEY is required"):
        sa_environment(path, {"QODER_SA_GLOBAL_KEY": ""}, ["cn", "global"], execution=False)


@pytest.mark.parametrize("execution", [False, True])
def test_missing_global_key_fails_before_cn_runs(tmp_path, execution):
    with pytest.raises(ValueError, match="QODER_SA_GLOBAL_KEY is required"):
        sa_environment(tmp_path / "missing.env", {"QODER_SA_CN_KEY": "cn"}, ["cn", "global"], execution=execution)


@pytest.mark.parametrize("flag", ["QODER_SA_LIVE_ALLOW_WRITE", "QODER_SA_LIVE_ALLOW_EXECUTION"])
def test_sa_execution_requires_both_flags(tmp_path, flag):
    environment = {
        "QODER_SA_CN_KEY": "cn",
        "QODER_SA_GLOBAL_KEY": "global",
        "QODER_SA_LIVE_ALLOW_WRITE": "true",
        "QODER_SA_LIVE_ALLOW_EXECUTION": "true",
        flag: "false",
    }
    with pytest.raises(ValueError, match=f"{flag}=true is required"):
        sa_environment(tmp_path / "missing.env", environment, ["cn", "global"], execution=True)
    environment[flag] = "true"
    sa_environment(tmp_path / "missing.env", environment, ["cn", "global"], execution=True)


def test_filtered_cn_suite_only_requires_selected_region(tmp_path):
    sa_environment(tmp_path / "missing.env", {"QODER_SA_CN_KEY": "cn"}, ["cn"], execution=False)
