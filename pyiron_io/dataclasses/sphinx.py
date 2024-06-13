from dataclasses import dataclass
import numpy as np
from typing import List


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
class Species:
    name: str
    pot_type: str
    element: str
    potential: str


@dataclass
class PawPot:
    species: List[Species]


@dataclass
class SphinxAtom:
    label: str
    coords: np.ndarray  # 3  [Angstrom]
    movable: bool


@dataclass
class SphinxElement:
    element: str
    atom: List[SphinxAtom]


@dataclass
class SphinxStructure:
    cell: np.ndarray  # 3 * 3  [Angstrom]
    species: List[SphinxElement]


@dataclass
class SphinxKpoint:
    coords: np.ndarray  # 3
    weight: float
    relative: bool


@dataclass
class SphinxBasis:
    e_cut: float  # [Hartree]
    k_point: SphinxKpoint
    folding: np.ndarray  # 3
    save_memory: bool


@dataclass
class SphinxPreConditioner:
    type: str
    scaling: float
    spin_scaling: float


@dataclass
class ScfDiag:
    rho_mixing: float
    spin_mixing: float
    delta_energy: float
    max_steps: int
    preconditioner: SphinxPreConditioner
    block_ccg: dict


@dataclass
class SphinxPawHamiltonian:
    number_empty_states: int
    ekt: float
    methfessel_paxton: bool
    xc: str
    spin_polarized: bool


@dataclass
class SphinxWaves:
    paw_basis: bool
    lcao: dict


@dataclass
class SphinxRho:
    atomic_orbitals: int


@dataclass
class SphinxInitialGuess:
    waves: SphinxWaves
    rho: SphinxRho
    no_waves_storage: bool


@dataclass
class BornOppenheimer:
    scf_diag: ScfDiag


@dataclass
class SphinxRicQN:
    max_steps: int
    max_step_length: float
    born_oppenheimer: BornOppenheimer


@dataclass
class SphinxMain:
    ric_qn: SphinxRicQN


@dataclass
class SphinxInternalInput:
    paw_pot: PawPot
    structure: SphinxStructure
    basis: SphinxBasis
    paw_hamilton: SphinxPawHamiltonian
    initial_guess: SphinxInitialGuess
    main: SphinxMain


@dataclass
class SphinxInputParameters:
    sphinx: SphinxInternalInput
    encut: float
    kpointcoords: List[float]  # 3
    kpointfolding: List[int]  # 3
    empty_states: int
    methfessel_paxton: bool
    sigma: float
    xcorr: str
    vasppot: bool
    e_step: int
    ediff: float
    write_waves: bool
    kj_xc: bool
    save_memory: bool
    rho_mixing: float
    spin_mixing: float
    rho_residual_scaling: float
    spin_residual_scaling: float
    check_overlap: bool
    threads: bool
    use_on_the_fly_cg_optimization: bool
    ionic_step: int


@dataclass
class SphinxOutputChargeDensity:
    total: np.ndarray


@dataclass
class SphinxDensityOfStates:
    energies: str
    int_densities: str
    tot_densities: str


@dataclass
class SphinxElectronicStructure:
    efermi: float
    eig_matrix: np.ndarray
    k_points: np.ndarray
    k_weights: np.ndarray
    occ_matrix: np.ndarray
    dos: SphinxDensityOfStates


@dataclass
class SphinxElectrostaticPotential:
    total: np.ndarray


@dataclass
class SphinxOutput:
    charge_density: SphinxOutputChargeDensity
    electronic_structure: SphinxElectronicStructure
    electrostatic_potential: SphinxElectrostaticPotential
    generic: GenericOutput


@dataclass
class SphinxInput:
    generic_dict: GenericDict
    interactive: Interactive
    generic: GenericInput
    parameters: SphinxInputParameters
    structure: Structure


@dataclass
class SphinxJob:
    executable: Executable
    server: Server
    calculation_input: SphinxInput
    calculation_output: SphinxOutput
    job_id: int
    status: str
