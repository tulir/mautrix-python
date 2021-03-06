# Copyright (c) 2020 Tulir Asokan
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from typing import Optional, Any, Dict

from mautrix.types import JSON, Serializable, SerializableEnum


class EventType(Serializable):
    class Class(SerializableEnum):
        UNKNOWN = "unknown"
        STATE = "state"
        MESSAGE = "message"
        ACCOUNT_DATA = "account_data"
        EPHEMERAL = "ephemeral"
        TO_DEVICE = "to_device"

    by_event_type: Dict[str, 'EventType']

    ROOM_CANONICAL_ALIAS: 'EventType'
    ROOM_ALIASES: 'EventType'
    ROOM_CREATE: 'EventType'
    ROOM_JOIN_RULES: 'EventType'
    ROOM_MEMBER: 'EventType'
    ROOM_POWER_LEVELS: 'EventType'
    ROOM_HISTORY_VISIBILITY: 'EventType'
    ROOM_NAME: 'EventType'
    ROOM_TOPIC: 'EventType'
    ROOM_AVATAR: 'EventType'
    ROOM_PINNED_EVENTS: 'EventType'
    ROOM_TOMBSTONE: 'EventType'
    ROOM_ENCRYPTION: 'EventType'

    ROOM_REDACTION: 'EventType'
    ROOM_MESSAGE: 'EventType'
    ROOM_ENCRYPTED: 'EventType'
    STICKER: 'EventType'
    REACTION: 'EventType'

    RECEIPT: 'EventType'
    TYPING: 'EventType'
    PRESENCE: 'EventType'

    DIRECT: 'EventType'
    PUSH_RULES: 'EventType'
    TAG: 'EventType'
    IGNORED_USER_LIST: 'EventType'

    TO_DEVICE_ENCRYPTED: 'EventType'
    ROOM_KEY: 'EventType'
    ROOM_KEY_WITHHELD: 'EventType'
    ORG_MATRIX_ROOM_KEY_WITHHELD: 'EventType'
    ROOM_KEY_REQUEST: 'EventType'
    FORWARDED_ROOM_KEY: 'EventType'

    ALL: 'EventType'

    is_message: bool
    is_state: bool
    is_ephemeral: bool
    is_account_data: bool
    is_to_device: bool

    t: str
    t_class: Class

    @classmethod
    def find(cls, t: str, t_class: Optional[Class] = None) -> 'EventType': ...

    def serialize(self) -> JSON: ...

    @classmethod
    def deserialize(cls, raw: JSON) -> Any: ...

    def with_class(self, t_class: Class) -> 'EventType': ...
