import numpy as np
import math
from typing import Dict, Any
from ..core.interfaces import AnimatorInterface

class SimpleFKAnimator(AnimatorInterface):
    def __init__(self):
        self.t = 0.0
        self.num_bones = 50 # Augmentons un peu pour l'exemple
        # 16 floats (matrice 4x4) * 4 octets (float32)
        self.bone_size_bytes = 16 * 4
        self.total_size = self.num_bones * self.bone_size_bytes

    def initialize(self, source_path: str):
        # Simulation de chargement
        pass

    def get_skeleton(self) -> Dict[str, Any]:
        return {
            "bones": [f"bone_{i}" for i in range(self.num_bones)],
            "hierarchy": []
        }

    def get_memory_size(self) -> int:
        return self.total_size

    def write_frame_to_buffer(self, buffer_view: memoryview, offset: int):
        self.t += 0.05

        # Création d'un tableau Numpy qui pointe DIRECTEMENT sur la mémoire partagée
        # Pas d'allocation mémoire ici !
        # On définit la shape (num_bones, 16) float32
        target_array = np.ndarray(
            shape=(self.num_bones, 16),
            dtype=np.float32,
            buffer=buffer_view,
            offset=offset
        )

        # Remplissage mathématique (Simulation)
        # Idéalement, faire les calculs directement dans target_array

        cos_t = math.cos(self.t)
        sin_t = math.sin(self.t)

        # Pour l'exemple, on remplit tout avec une identité modifiée
        # C'est ici que tu mettras ton vrai algo FK

        # Reset rapide à 0
        target_array.fill(0)

        # Diagonale à 1
        # Astuce numpy pour faire une diagonale sur un array (N, 4, 4) ou (N, 16)
        target_array[:, 0] = 1
        target_array[:, 5] = 1
        target_array[:, 10] = 1
        target_array[:, 15] = 1

        # Petite animation sur X et Y
        target_array[:, 12] = cos_t + np.arange(self.num_bones) * 0.1
        target_array[:, 13] = sin_t