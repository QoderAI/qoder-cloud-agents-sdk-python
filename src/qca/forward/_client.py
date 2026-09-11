from __future__ import annotations

from functools import cached_property

from qca.common._base_client import AsyncAPIClient, SyncAPIClient

from .resources.batches.batches import AsyncBatches, Batches
from .resources.channel_pairings import AsyncChannelPairings, ChannelPairings
from .resources.channels.channels import AsyncChannels, Channels
from .resources.environments import AsyncEnvironments, Environments
from .resources.files import AsyncFiles, Files
from .resources.identities.identities import AsyncIdentities, Identities
from .resources.memory_stores.memory_stores import AsyncMemoryStores, MemoryStores
from .resources.models import AsyncModels, Models
from .resources.schedule_runs import AsyncScheduleRuns, ScheduleRuns
from .resources.schedules import AsyncSchedules, Schedules
from .resources.sessions.sessions import AsyncSessions, Sessions
from .resources.skills.skills import AsyncSkills, Skills
from .resources.templates import AsyncTemplates, Templates
from .resources.vaults.vaults import AsyncVaults, Vaults


class Forward(SyncAPIClient):
    _default_base_url = "https://api.qoder.com/api/v1/forward/"
    _base_url_env = "QODER_FORWARD_BASE_URL"

    @cached_property
    def templates(self) -> Templates:
        return Templates(self)

    @cached_property
    def identities(self) -> Identities:
        return Identities(self)

    @cached_property
    def sessions(self) -> Sessions:
        return Sessions(self)

    @cached_property
    def schedules(self) -> Schedules:
        return Schedules(self)

    @cached_property
    def schedule_runs(self) -> ScheduleRuns:
        return ScheduleRuns(self)

    @cached_property
    def batches(self) -> Batches:
        return Batches(self)

    @cached_property
    def channels(self) -> Channels:
        return Channels(self)

    @cached_property
    def channel_pairings(self) -> ChannelPairings:
        return ChannelPairings(self)

    @cached_property
    def environments(self) -> Environments:
        return Environments(self)

    @cached_property
    def files(self) -> Files:
        return Files(self)

    @cached_property
    def skills(self) -> Skills:
        return Skills(self)

    @cached_property
    def vaults(self) -> Vaults:
        return Vaults(self)

    @cached_property
    def memory_stores(self) -> MemoryStores:
        return MemoryStores(self)

    @cached_property
    def models(self) -> Models:
        return Models(self)


class AsyncForward(AsyncAPIClient):
    _default_base_url = "https://api.qoder.com/api/v1/forward/"
    _base_url_env = "QODER_FORWARD_BASE_URL"

    @cached_property
    def templates(self) -> AsyncTemplates:
        return AsyncTemplates(self)

    @cached_property
    def identities(self) -> AsyncIdentities:
        return AsyncIdentities(self)

    @cached_property
    def sessions(self) -> AsyncSessions:
        return AsyncSessions(self)

    @cached_property
    def schedules(self) -> AsyncSchedules:
        return AsyncSchedules(self)

    @cached_property
    def schedule_runs(self) -> AsyncScheduleRuns:
        return AsyncScheduleRuns(self)

    @cached_property
    def batches(self) -> AsyncBatches:
        return AsyncBatches(self)

    @cached_property
    def channels(self) -> AsyncChannels:
        return AsyncChannels(self)

    @cached_property
    def channel_pairings(self) -> AsyncChannelPairings:
        return AsyncChannelPairings(self)

    @cached_property
    def environments(self) -> AsyncEnvironments:
        return AsyncEnvironments(self)

    @cached_property
    def files(self) -> AsyncFiles:
        return AsyncFiles(self)

    @cached_property
    def skills(self) -> AsyncSkills:
        return AsyncSkills(self)

    @cached_property
    def vaults(self) -> AsyncVaults:
        return AsyncVaults(self)

    @cached_property
    def memory_stores(self) -> AsyncMemoryStores:
        return AsyncMemoryStores(self)

    @cached_property
    def models(self) -> AsyncModels:
        return AsyncModels(self)
