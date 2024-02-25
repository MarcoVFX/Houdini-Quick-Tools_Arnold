#name = OGL_Select
#label = OGL_Select
#icon = hicon:/SVGIcons.index?BUTTONS_grid.svg

rop = hou.node("/out")
ogl = rop.createNode("opengl","flipbook")

#set render parameter
ogl.parm("alights").set("")
ogl.parm("vobjects").set("")
ogl.parm("picture").set("$HIP/flipbook/v001/flipbook.$F4.exr")
ogl.parm("trange").set("normal")
ogl.parm("colorcorrect").set("ocio")
ogl.parm("ociocolorspace").set("ACES - ACEScg")
ogl.parm("vm_image_exr_compression").set("zips")
ogl.parm("aamode").set("aa8")
ogl.parm("usehdr").set("on")
ogl.parm("usetextures").set(0)
ogl.parm("hqlighting").set(0)
ogl.parm("shadows").set(0)
ogl.parm("transparency").set(0)
ogl.parm("tex2dformat").set("format32fp")
ogl.parm("tex3dformat").set("format32fp")

nodes = hou.selectedNodes()

for idx, node in enumerate(nodes):
    idx += 1 
    path = node.path()
    value = ogl.evalParm("vobjects")
    type = node.type().name()

    if (type != "cam"):
        if (idx > 1):
            ogl.parm("vobjects").set(value+" "+path)
        else:
            ogl.parm("vobjects").set(value+path)
    else:
        ogl.parm("camera").set(path)
