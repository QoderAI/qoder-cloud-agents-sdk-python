from importlib.metadata import PackageNotFoundError, version

try:
    # 分发名是 qca-sdk，导入名是 qca，元数据只认前者。
    __version__ = version("qca-sdk")
except PackageNotFoundError:
    # 直接从源码树导入（未安装）时没有包元数据可读。
    __version__ = "0.0.0.dev0"
