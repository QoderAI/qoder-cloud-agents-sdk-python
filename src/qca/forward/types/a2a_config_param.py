from __future__ import annotations

from typing import List

from typing_extensions import Required, TypedDict

__all__ = ["A2AConfigParam", "A2ASkillParam"]


class A2ASkillParam(TypedDict, total=False):
    id: Required[str]
    name: Required[str]
    description: Required[str]
    tags: List[str]
    examples: List[str]


class A2AConfigParam(TypedDict, total=False):
    """Publication settings, not a multiagent roster. Members cannot be null.

    On update, omitted members and {} preserve existing settings; skills=[]
    clears advertised skills. Set the whole a2a field to None to disable/clear.
    """

    enabled: bool
    description: str
    skills: List[A2ASkillParam]
