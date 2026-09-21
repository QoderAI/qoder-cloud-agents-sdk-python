"""测试专用的项目记忆夹具（ProjectMemory）。

从 examples/common/live.py 净移出——examples 侧不再保留。
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field

from tests.support.harness import marker


@dataclass
class ProjectMemory:
    project: str = field(default_factory=lambda: "青禾订单-" + marker()[:6])
    release_time: str = field(default_factory=lambda: f"{random.randrange(20, 24):02}:{random.randrange(60):02}")
    contact: str = field(default_factory=lambda: random.choice(["林岚", "陈朔", "叶澄", "苏棠"]))
    rollback_version: str = field(
        default_factory=lambda: f"v2.{random.randrange(100, 1000)}.{random.randrange(100, 1000)}"
    )
    path = "projects/release-conventions.md"

    def content(self) -> str:
        return f"---\nname: release-conventions\ndescription: {self.project} 的项目发布约定\nmetadata:\n  type: project\n---\n\n# {self.project}\n\n- 北京时间 {self.release_time} 开始发布。\n- 发布异常时联系值班负责人{self.contact}。\n- 回滚使用已验证的稳定版本 {self.rollback_version}。\n\nWhy: 在值班窗口发布，并使用验证过的版本恢复服务。\nHow to apply: 为这个项目拟定发布计划时遵循以上约定。\n"

    def index(self) -> str:
        return f"- [{self.project} 发布约定]({self.path}) — 发布窗口、异常联系人与回滚约定。\n"

    def prompt(self) -> str:
        return f"请根据你记得的项目约定，为「{self.project}」拟一份简短上线安排，涵盖开始时间、异常联系和回滚处理。不要执行发布；缺少信息时请明确说明。"

    def expected(self) -> list[str]:
        return [self.release_time, self.contact, self.rollback_version]
