from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .system_message_event_params import SystemMessageEventParams
    from .user_custom_tool_result_event_params import UserCustomToolResultEventParams
    from .user_define_outcome_event_params import UserDefineOutcomeEventParams
    from .user_interrupt_event_params import UserInterruptEventParams
    from .user_message_event_params import UserMessageEventParams
    from .user_tool_confirmation_event_params import UserToolConfirmationEventParams
    from .user_tool_result_event_params import UserToolResultEventParams

__all__ = ["SessionEventSendParams"]


class SessionEventSendParams(TypedDict, total=False):
    events: Required[
        List[
            Union[
                UserMessageEventParams,
                UserInterruptEventParams,
                UserToolConfirmationEventParams,
                UserCustomToolResultEventParams,
                UserDefineOutcomeEventParams,
                UserToolResultEventParams,
                SystemMessageEventParams,
            ]
        ]
    ]
    workspace_id: Optional[str]
    betas: List[str]
