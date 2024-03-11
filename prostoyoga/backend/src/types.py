from typing import Annotated, TypeAlias
from uuid import UUID

EntryId: TypeAlias = Annotated[str, UUID.hex]
