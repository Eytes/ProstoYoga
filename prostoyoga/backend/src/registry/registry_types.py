from typing import TypeAlias

RegistryValue: TypeAlias = str | int | bool
RegistryData: TypeAlias = dict[str, RegistryValue]
RegistryQuery: TypeAlias = dict[str, RegistryValue]
