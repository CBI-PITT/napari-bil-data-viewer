
try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"



#from .reader import napari_get_reader
from .bil_data_loader_widget import napari_experimental_provide_dock_widget



