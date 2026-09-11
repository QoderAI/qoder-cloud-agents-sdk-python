from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("qca")
except PackageNotFoundError:
    # 直接从源码树导入（未安装）时没有包元数据可读。
    __version__ = "0.0.0.dev0"
