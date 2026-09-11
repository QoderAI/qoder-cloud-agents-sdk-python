from __future__ import annotations

from functools import cached_property

from qca.common._base_client import AsyncAPIClient, SyncAPIClient

from .resources.agents.agents import Agents, AsyncAgents
from .resources.deployment_runs import AsyncDeploymentRuns, DeploymentRuns
from .resources.deployments import AsyncDeployments, Deployments
from .resources.dreams import AsyncDreams, Dreams
from .resources.environments.environments import AsyncEnvironments, Environments
from .resources.files import AsyncFiles, Files
from .resources.memory_stores.memory_stores import AsyncMemoryStores, MemoryStores
from .resources.models import AsyncModels, Models
from .resources.sessions.sessions import AsyncSessions, Sessions
from .resources.skills.skills import AsyncSkills, Skills
from .resources.vaults.vaults import AsyncVaults, Vaults


class Managed(SyncAPIClient):
    _default_base_url = "https://api.qoder.com/api/v1/cloud/"
    _base_url_env = "QODER_BASE_URL"

    @cached_property
    def agents(self) -> Agents:
        return Agents(self)

    @cached_property
    def sessions(self) -> Sessions:
        return Sessions(self)

    @cached_property
    def deployments(self) -> Deployments:
        return Deployments(self)

    @cached_property
    def deployment_runs(self) -> DeploymentRuns:
        return DeploymentRuns(self)

    @cached_property
    def dreams(self) -> Dreams:
        return Dreams(self)

    @cached_property
    def environments(self) -> Environments:
        return Environments(self)

    @cached_property
    def skills(self) -> Skills:
        return Skills(self)

    @cached_property
    def vaults(self) -> Vaults:
        return Vaults(self)

    @cached_property
    def files(self) -> Files:
        return Files(self)

    @cached_property
    def memory_stores(self) -> MemoryStores:
        return MemoryStores(self)

    @cached_property
    def models(self) -> Models:
        return Models(self)


class AsyncManaged(AsyncAPIClient):
    _default_base_url = "https://api.qoder.com/api/v1/cloud/"
    _base_url_env = "QODER_BASE_URL"

    @cached_property
    def agents(self) -> AsyncAgents:
        return AsyncAgents(self)

    @cached_property
    def sessions(self) -> AsyncSessions:
        return AsyncSessions(self)

    @cached_property
    def deployments(self) -> AsyncDeployments:
        return AsyncDeployments(self)

    @cached_property
    def deployment_runs(self) -> AsyncDeploymentRuns:
        return AsyncDeploymentRuns(self)

    @cached_property
    def dreams(self) -> AsyncDreams:
        return AsyncDreams(self)

    @cached_property
    def environments(self) -> AsyncEnvironments:
        return AsyncEnvironments(self)

    @cached_property
    def skills(self) -> AsyncSkills:
        return AsyncSkills(self)

    @cached_property
    def vaults(self) -> AsyncVaults:
        return AsyncVaults(self)

    @cached_property
    def files(self) -> AsyncFiles:
        return AsyncFiles(self)

    @cached_property
    def memory_stores(self) -> AsyncMemoryStores:
        return AsyncMemoryStores(self)

    @cached_property
    def models(self) -> AsyncModels:
        return AsyncModels(self)
