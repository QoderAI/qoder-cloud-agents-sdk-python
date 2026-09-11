from datetime import datetime
from typing import Any, Dict, List, Literal, Optional, Union

from qca.common._models import BaseModel as _BaseModel
from qca.common._types import FileTypes

from .batch import Batch as Batch
from .batch_cancel_params import BatchCancelParams as BatchCancelParams
from .batch_create_params import BatchCreateParams as BatchCreateParams
from .batch_file import BatchFile as BatchFile
from .batch_list_params import BatchListParams as BatchListParams
from .batch_request_counts import BatchRequestCounts as BatchRequestCounts
from .batch_task import BatchTask as BatchTask
from .batch_task_artifacts_item import BatchTaskArtifactsItem as BatchTaskArtifactsItem
from .batch_task_error import BatchTaskError as BatchTaskError
from .batch_task_list_params import BatchTaskListParams as BatchTaskListParams
from .batch_task_usage import BatchTaskUsage as BatchTaskUsage
from .batch_usage import BatchUsage as BatchUsage
from .channel import Channel as Channel
from .channel_channel_config import ChannelChannelConfig as ChannelChannelConfig
from .channel_channel_config_response_options import (
    ChannelChannelConfigResponseOptions as ChannelChannelConfigResponseOptions,
)
from .channel_create_params import ChannelCreateParams as ChannelCreateParams
from .channel_identity_resolution import ChannelIdentityResolution as ChannelIdentityResolution
from .channel_list_params import ChannelListParams as ChannelListParams
from .channel_pairing import ChannelPairing as ChannelPairing
from .channel_pairing_create_params import ChannelPairingCreateParams as ChannelPairingCreateParams
from .channel_qr_session import ChannelQRSession as ChannelQRSession
from .channel_qr_session_create_params import ChannelQRSessionCreateParams as ChannelQRSessionCreateParams
from .channel_update_params import ChannelUpdateParams as ChannelUpdateParams
from .content_block_param import ContentBlockParam as ContentBlockParam
from .deleted_channel import DeletedChannel as DeletedChannel
from .deleted_channel_pairing import DeletedChannelPairing as DeletedChannelPairing
from .deleted_identity import DeletedIdentity as DeletedIdentity
from .deleted_memory import DeletedMemory as DeletedMemory
from .deleted_memory_store import DeletedMemoryStore as DeletedMemoryStore
from .deleted_memory_store_mount import DeletedMemoryStoreMount as DeletedMemoryStoreMount
from .deleted_skill_version import DeletedSkillVersion as DeletedSkillVersion
from .effective_config import EffectiveConfig as EffectiveConfig
from .effective_config_agent import EffectiveConfigAgent as EffectiveConfigAgent
from .effective_config_agent_tools_item import EffectiveConfigAgentToolsItem as EffectiveConfigAgentToolsItem
from .effective_config_agent_tools_item_configs_item import (
    EffectiveConfigAgentToolsItemConfigsItem as EffectiveConfigAgentToolsItemConfigsItem,
)
from .effective_config_session import EffectiveConfigSession as EffectiveConfigSession
from .effective_config_session_resources_item import (
    EffectiveConfigSessionResourcesItem as EffectiveConfigSessionResourcesItem,
)
from .environment import Environment as Environment
from .environment_config import EnvironmentConfig as EnvironmentConfig
from .environment_config_packages import EnvironmentConfigPackages as EnvironmentConfigPackages
from .environment_create_params import EnvironmentCreateParams as EnvironmentCreateParams
from .environment_list_params import EnvironmentListParams as EnvironmentListParams
from .environment_update_params import EnvironmentUpdateParams as EnvironmentUpdateParams
from .environment_variable_override import EnvironmentVariableOverride as EnvironmentVariableOverride
from .environment_variable_override_param import EnvironmentVariableOverrideParam as EnvironmentVariableOverrideParam
from .file_list_params import FileListParams as FileListParams
from .file_metadata import FileMetadata as FileMetadata
from .file_upload_params import FileUploadParams as FileUploadParams
from .git_hub_repository import GitHubRepository as GitHubRepository
from .git_hub_repository_param import GitHubRepositoryParam as GitHubRepositoryParam
from .identity import Identity as Identity
from .identity_clear_params import IdentityClearParams as IdentityClearParams
from .identity_clear_response import IdentityClearResponse as IdentityClearResponse
from .identity_clear_response_summary import IdentityClearResponseSummary as IdentityClearResponseSummary
from .identity_config import IdentityConfig as IdentityConfig
from .identity_config_list_params import IdentityConfigListParams as IdentityConfigListParams
from .identity_config_spec import IdentityConfigSpec as IdentityConfigSpec
from .identity_config_spec_param import IdentityConfigSpecParam as IdentityConfigSpecParam
from .identity_config_upsert_params import IdentityConfigUpsertParams as IdentityConfigUpsertParams
from .identity_create_params import IdentityCreateParams as IdentityCreateParams
from .identity_list_params import IdentityListParams as IdentityListParams
from .identity_list_templates_response import IdentityListTemplatesResponse as IdentityListTemplatesResponse
from .identity_memory_store_list_response import IdentityMemoryStoreListResponse as IdentityMemoryStoreListResponse
from .identity_memory_store_mount_params import IdentityMemoryStoreMountParams as IdentityMemoryStoreMountParams
from .identity_stats import IdentityStats as IdentityStats
from .identity_template import IdentityTemplate as IdentityTemplate
from .identity_update_params import IdentityUpdateParams as IdentityUpdateParams
from .image_source_param import ImageSourceParam as ImageSourceParam
from .mcp_server import MCPServer as MCPServer
from .mcp_server_override import MCPServerOverride as MCPServerOverride
from .mcp_server_override_param import MCPServerOverrideParam as MCPServerOverrideParam
from .mcp_server_param import MCPServerParam as MCPServerParam
from .memory import Memory as Memory
from .memory_store import MemoryStore as MemoryStore
from .memory_store_create_params import MemoryStoreCreateParams as MemoryStoreCreateParams
from .memory_store_list_params import MemoryStoreListParams as MemoryStoreListParams
from .memory_store_memory_create_params import MemoryStoreMemoryCreateParams as MemoryStoreMemoryCreateParams
from .memory_store_memory_list_params import MemoryStoreMemoryListParams as MemoryStoreMemoryListParams
from .memory_store_memory_update_params import MemoryStoreMemoryUpdateParams as MemoryStoreMemoryUpdateParams
from .memory_store_memory_version_list_params import (
    MemoryStoreMemoryVersionListParams as MemoryStoreMemoryVersionListParams,
)
from .memory_store_mount import MemoryStoreMount as MemoryStoreMount
from .memory_store_update_params import MemoryStoreUpdateParams as MemoryStoreUpdateParams
from .memory_version import MemoryVersion as MemoryVersion
from .model import Model as Model
from .model_config import ModelConfig as ModelConfig
from .model_config_param import ModelConfigParam as ModelConfigParam
from .model_list_response import ModelListResponse as ModelListResponse
from .multiagent_config import MultiagentConfig as MultiagentConfig
from .multiagent_config_param import MultiagentConfigParam as MultiagentConfigParam
from .multiagent_entry import MultiagentEntry as MultiagentEntry
from .multiagent_entry_param import MultiagentEntryParam as MultiagentEntryParam
from .permission_policy import PermissionPolicy as PermissionPolicy
from .permission_policy_param import PermissionPolicyParam as PermissionPolicyParam
from .resource_binding import ResourceBinding as ResourceBinding
from .resource_binding_param import ResourceBindingParam as ResourceBindingParam
from .schedule import Schedule as Schedule
from .schedule_archive_many_params import ScheduleArchiveManyParams as ScheduleArchiveManyParams
from .schedule_archive_many_response import ScheduleArchiveManyResponse as ScheduleArchiveManyResponse
from .schedule_archive_params import ScheduleArchiveParams as ScheduleArchiveParams
from .schedule_create_params import ScheduleCreateParams as ScheduleCreateParams
from .schedule_execution import ScheduleExecution as ScheduleExecution
from .schedule_initial_events_item import ScheduleInitialEventsItem as ScheduleInitialEventsItem
from .schedule_list_params import ScheduleListParams as ScheduleListParams
from .schedule_pause_params import SchedulePauseParams as SchedulePauseParams
from .schedule_paused_reason import SchedulePausedReason as SchedulePausedReason
from .schedule_run import ScheduleRun as ScheduleRun
from .schedule_run_list_params import ScheduleRunListParams as ScheduleRunListParams
from .schedule_run_params import ScheduleRunParams as ScheduleRunParams
from .schedule_run_retrieve_params import ScheduleRunRetrieveParams as ScheduleRunRetrieveParams
from .schedule_run_trigger_context import ScheduleRunTriggerContext as ScheduleRunTriggerContext
from .schedule_sinks_item import ScheduleSinksItem as ScheduleSinksItem
from .schedule_sinks_item_target import ScheduleSinksItemTarget as ScheduleSinksItemTarget
from .schedule_trigger_policy import ScheduleTriggerPolicy as ScheduleTriggerPolicy
from .schedule_unpause_params import ScheduleUnpauseParams as ScheduleUnpauseParams
from .schedule_update_params import ScheduleUpdateParams as ScheduleUpdateParams
from .session import Session as Session
from .session_archive_params import SessionArchiveParams as SessionArchiveParams
from .session_cancel_params import SessionCancelParams as SessionCancelParams
from .session_config import SessionConfig as SessionConfig
from .session_create_params import SessionCreateParams as SessionCreateParams
from .session_create_params_config_param import SessionCreateParamsConfigParam as SessionCreateParamsConfigParam
from .session_event import SessionEvent as SessionEvent
from .session_event_list_params import SessionEventListParams as SessionEventListParams
from .session_event_param import SessionEventParam as SessionEventParam
from .session_event_send_params import SessionEventSendParams as SessionEventSendParams
from .session_event_send_response import SessionEventSendResponse as SessionEventSendResponse
from .session_event_stream_params import SessionEventStreamParams as SessionEventStreamParams
from .session_list_params import SessionListParams as SessionListParams
from .session_resource import SessionResource as SessionResource
from .session_resource_add_params import SessionResourceAddParams as SessionResourceAddParams
from .session_resource_spec_param import SessionResourceSpecParam as SessionResourceSpecParam
from .session_stats import SessionStats as SessionStats
from .session_template import SessionTemplate as SessionTemplate
from .session_thread import SessionThread as SessionThread
from .session_thread_archive_params import SessionThreadArchiveParams as SessionThreadArchiveParams
from .session_thread_event_list_params import SessionThreadEventListParams as SessionThreadEventListParams
from .session_thread_event_stream_params import SessionThreadEventStreamParams as SessionThreadEventStreamParams
from .session_thread_list_params import SessionThreadListParams as SessionThreadListParams
from .session_thread_stop_reason import SessionThreadStopReason as SessionThreadStopReason
from .session_update_params import SessionUpdateParams as SessionUpdateParams
from .session_update_params_config_param import SessionUpdateParamsConfigParam as SessionUpdateParamsConfigParam
from .session_usage import SessionUsage as SessionUsage
from .skill import Skill as Skill
from .skill_binding import SkillBinding as SkillBinding
from .skill_binding_param import SkillBindingParam as SkillBindingParam
from .skill_create_params import SkillCreateParams as SkillCreateParams
from .skill_list_params import SkillListParams as SkillListParams
from .skill_override import SkillOverride as SkillOverride
from .skill_override_param import SkillOverrideParam as SkillOverrideParam
from .skill_retrieve_params import SkillRetrieveParams as SkillRetrieveParams
from .skill_update_params import SkillUpdateParams as SkillUpdateParams
from .skill_version import SkillVersion as SkillVersion
from .skill_version_create_params import SkillVersionCreateParams as SkillVersionCreateParams
from .skill_version_list_params import SkillVersionListParams as SkillVersionListParams
from .system_override import SystemOverride as SystemOverride
from .system_override_param import SystemOverrideParam as SystemOverrideParam
from .template import Template as Template
from .template_archive_params import TemplateArchiveParams as TemplateArchiveParams
from .template_clone_params import TemplateCloneParams as TemplateCloneParams
from .template_create_params import TemplateCreateParams as TemplateCreateParams
from .template_list_params import TemplateListParams as TemplateListParams
from .template_update_params import TemplateUpdateParams as TemplateUpdateParams
from .tool import Tool as Tool
from .tool_config import ToolConfig as ToolConfig
from .tool_config_param import ToolConfigParam as ToolConfigParam
from .tool_override import ToolOverride as ToolOverride
from .tool_override_param import ToolOverrideParam as ToolOverrideParam
from .tool_param import ToolParam as ToolParam
from .vault import Vault as Vault
from .vault_create_params import VaultCreateParams as VaultCreateParams
from .vault_credential import VaultCredential as VaultCredential
from .vault_credential_auth import VaultCredentialAuth as VaultCredentialAuth
from .vault_credential_create_params import VaultCredentialCreateParams as VaultCredentialCreateParams
from .vault_credential_list_params import VaultCredentialListParams as VaultCredentialListParams
from .vault_list_params import VaultListParams as VaultListParams

_namespace = dict(
    globals(),
    datetime=datetime,
    Any=Any,
    Dict=Dict,
    List=List,
    Literal=Literal,
    Optional=Optional,
    Union=Union,
    FileTypes=FileTypes,
)
for _model in list(_namespace.values()):
    if isinstance(_model, type) and issubclass(_model, _BaseModel) and _model is not _BaseModel:
        _model.model_rebuild(_types_namespace=_namespace)
del _namespace, _model
