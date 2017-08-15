# -----------------------------------------------------------------------------
# Substance Painter
#
# This file contains controller all Substance Painter functions, send to SP, or
# re-export an project.
# -----------------------------------------------------------------------------

import bpy

from ..models.SubstanceSoftware import *

# ------------------------------------------------------------------------
# Function to define the obj name.
# ------------------------------------------------------------------------
def objname():
    sbs_project = bpy.context.active_object
    data = bpy.data.objects[sbs_project.name]
    if data.get('substance_project') is not None:
        sbs_name = data['substance_project']
        sbs_name = sbs_name + '.obj'
    else:
        sbs_name = 'tmp.obj'

    return sbs_name


class SubstanceVariable(bpy.types.PropertyGroup):
    # Temporary Folder and obj mesh
    tmp_folder = bpy.context.user_preferences.filepaths.temporary_directory


# ------------------------------------------------------------------------
# Function to create an Obj, and export to painter
# ------------------------------------------------------------------------


class SendToPainter(bpy.types.Operator):
    """Export your mesh to Substance Painter"""
    bl_idname = "substance.painter_export"
    bl_label = "Send mesh to painter export"

    project = BoolProperty(name="It's a new project.")
    painter = StringProperty(name="Path Substance Painter")
    update = BoolProperty(
        default=False,
        name="Variable de test, update or not"
        )

    path_project = StringProperty(name="Path Substance project")

    def execute(self, context):
        obj = context.active_object

        mesh = SubstanceVariable.tmp_folder
        name_mesh = objname()
        mesh = mesh + name_mesh

        user_preferences = context.user_preferences
        addon_prefs = user_preferences.addons["SubstanceBridge"].preferences
        self.painter = str(addon_prefs.path_painter)

        print("path mesh")
        print(mesh)
        print("----------")
        print("obj file name")

        if obj.type == 'MESH':
            obj_mesh = bpy.data.objects[obj.name].data
            if obj_mesh.uv_textures:
                # Export du mesh selectionne
                bpy.ops.sbs_painter.selected_project()
                bpy.ops.export_scene.obj(filepath=mesh,
                                         use_selection=True,
                                         use_materials=True,
                                         path_mode='AUTO')

                # Verification si le soft est configuré dans le path
                if self.painter:
                    scn = context.scene
                    path_sppfile = scn.sbs_project_settings.path_spp
                    self.name_project = mesh
                    # Test If it's a new project.
                    if self.project is True:
                        self.path_project = path_sppfile

                    else:
                        self.path_project = ""

                    SbsPainterProject(self.path_project,
                                      self.name_project).start()
                else:
                    self.report({'WARNING'},
                                "No path configured, setup into User Pre.")
                    return {'CANCELLED'}

            else:
                self.report({'WARNING'},
                            "This object don't containt a UV layers.")
                return {'CANCELLED'}

        else:
            self.report({'WARNING'}, "This object is not a mesh.")
            return {'CANCELLED'}

        return {'FINISHED'}


def register():
    bpy.utils.register_class(SendToPainter)


def unregister():
    bpy.utils.unregister_class(SendToPainter)
