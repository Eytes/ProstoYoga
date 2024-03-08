from typing import Annotated
from uuid import UUID

# EntryId = str
EntryId = Annotated[str, UUID.hex]
