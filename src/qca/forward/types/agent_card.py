from __future__ import annotations

from typing import List, Optional

from pydantic import Field

from qca.common._models import BaseModel

from .a2a_config import A2ASkill

__all__ = ["AgentCard", "AgentCardInterface"]


class AgentCardInterface(BaseModel):
    url: str
    protocol_binding: Optional[str] = Field(default=None, alias="protocolBinding")
    protocol_version: Optional[str] = Field(default=None, alias="protocolVersion")


class AgentCard(BaseModel):
    """A2A 0.3/1.0 discovery document; unknown protocol fields are retained."""

    name: str
    description: str
    version: str
    skills: List[A2ASkill]
    default_input_modes: List[str] = Field(alias="defaultInputModes")
    default_output_modes: List[str] = Field(alias="defaultOutputModes")
    url: Optional[str] = None
    supported_interfaces: Optional[List[AgentCardInterface]] = Field(default=None, alias="supportedInterfaces")
