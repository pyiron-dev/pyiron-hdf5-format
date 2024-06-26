from dataclasses import dataclass
from typing import Optional, List


from pyiron_io.dataclasses.generic import (
    GenericDict,
    Interactive,
    GenericInput,
    GenericOutput,
    Executable,
    Server,
    Structure,
)


@dataclass
class LammpsPotential:
    citation: Optional[str]
    config: List[str]
    filename: List[str]
    model: str
    name: str
    species: List[str]


@dataclass
class LammpsInputFiles:
    control_inp: str
    potential_inp: str


@dataclass
class LammpsInput:
    generic_dict: GenericDict
    interactive: Interactive
    generic: GenericInput
    structure: Structure
    potential: LammpsPotential
    input_files: LammpsInputFiles


@dataclass
class LammpsOutput:
    generic: GenericOutput


@dataclass
class LammpsJob:
    calculation_input: LammpsInput
    executable: Executable
    server: Server
    calculation_output: LammpsOutput
    status: str
    job_id: int
