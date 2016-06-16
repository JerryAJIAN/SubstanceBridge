# ##### Substance Bridge #####
# A simple bridge between painter and blender.
#
# Thx Jerem.

# ------------------------------------------------------------------------
# Import all Package addon
# ------------------------------------------------------------------------
import bpy
import sys

from SubstanceBridge.settings import SubstanceSettings
from SubstanceBridge.CommandPainter import PainterProject
from SubstanceBridge.GUI import PainterPanel

# ------------------------------------------------------------------------
# MetaData Add-On Blender
# ------------------------------------------------------------------------
bl_info = {
    "name": "Substance Bridge",
    "author": "stilobique",
    "version": (0, 3),
    "blender": (2, 77, 0),
    "location": "Tool Shelf > Substance Panel",
    "description": "A simple way to export into substance painter.",
    "warning": "",
    "wiki_url": "",
    "category": "3D View",
    }

# ------------------------------------------------------------------------
# Settings for this addons
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# Mise dans le registre des différentes functions pour l'addon.
# ------------------------------------------------------------------------
def register():
    bpy.utils.register_class(PainterProject)
    bpy.utils.register_class(PainterPanel)
    bpy.utils.register_class(SubstanceSettings)
    
    # Project Path.
    bpy.types.Scene.sppfile = bpy.props.StringProperty \
        (
        name = "Project Path",
        default = "",
        description = "Field project path",
        subtype = 'FILE_PATH'
        )

def unregister():
    bpy.utils.unregister_class(PainterProject)
    bpy.utils.unregister_class(PainterPanel)
    bpy.utils.unregister_class(SubstanceSettings)

if __name__ == "__main__":
    register()