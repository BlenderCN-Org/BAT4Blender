import bpy

from .GUI import *

bl_info = {
    "name": "BAT4Blender",
    "category": "Render",
    "blender": (2, 79, 0),
    "author": "vrtxt",
    "version": (0, 0, 2),
}


# note: registering is order dependent! i.e. registering layout before vars will throw errors
def register():
    bpy.utils.register_class(InterfaceVars)
    bpy.types.WindowManager.interface_vars = bpy.props.PointerProperty(type=InterfaceVars)
    bpy.types.Scene.group_id = bpy.props.StringProperty(
            name="Group Id",
            description="the GID as provided by gmax",
            default="default"
        )

    bpy.utils.register_class(MainPanel)
    bpy.utils.register_class(B4BPreview)
    bpy.utils.register_class(B4BRender)
    bpy.utils.register_class(B4BLODExport)
    bpy.utils.register_class(B4BLODAdd)
    bpy.utils.register_class(B4BLODDelete)
    bpy.utils.register_class(B4BSunAdd)
    bpy.utils.register_class(B4BSunDelete)
    bpy.utils.register_class(B4BCamAdd)
    bpy.utils.register_class(B4BCamDelete)


def unregister():
    bpy.utils.unregister_class(InterfaceVars)
    del bpy.types.WindowManager.interface_vars
    del bpy.types.Scene.my_string_prop

    bpy.utils.unregister_class(MainPanel)
    bpy.utils.unregister_class(B4BPreview)
    bpy.utils.unregister_class(B4BRender)
    bpy.utils.unregister_class(B4BLODExport)
    bpy.utils.unregister_class(B4BLODAdd)
    bpy.utils.unregister_class(B4BLODDelete)
    bpy.utils.unregister_class(B4BSunAdd)
    bpy.utils.unregister_class(B4BSunDelete)
    bpy.utils.unregister_class(B4BCamAdd)
    bpy.utils.unregister_class(B4BCamDelete)
