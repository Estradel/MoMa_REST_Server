from abc import ABC, abstractmethod
from typing import Dict, Any

class AnimatorInterface(ABC):
    @abstractmethod
    def initialize(self, source_path: str):
        pass

    @abstractmethod
    def get_skeleton(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_memory_size(self) -> int:
        """
        Retourne la taille exacte en octets d'une frame.
        Nécessaire pour allouer la mémoire partagée.
        Ex: 10 os * 16 floats * 4 bytes = 640 bytes.
        """
        pass

    @abstractmethod
    def write_frame_to_buffer(self, buffer_view: memoryview, offset: int, dt: float):
        """
        Écrit les données de la frame directement dans le buffer mémoire fourni.
        'buffer_view' est une vue sur la mémoire partagée globale.
        'offset' est l'endroit où commencer à écrire.
        'dt' est le temps écoulé (delta time) ou le pas de temps cible pour cette frame (en secondes).
        """
        pass