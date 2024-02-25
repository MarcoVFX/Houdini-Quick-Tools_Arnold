#name = addRefAovRop
#label = Add reference AOV ROP
#icon = hicon:/SVGIcons.index?BUTTONS_attribute.svg

import hou

#Delete AOV ROP if it's already exist
exist = 0
root = hou.node("/obj")
for rootnode in root.glob("*AOV*"):
    exist = 1

if (exist == 1):
    legacyNode = hou.node("/obj/AOV")
    legacyNode.destroy()
    
#Create ROP Net   
ROP = root.createNode("ropnet","AOV",force_valid_node_name=False)
Arnold = ROP.createNode("arnold","AOV_list",force_valid_node_name=False)

#Create AOV parameter
nodes = hou.selectedNodes()
count = 0
for node in nodes:
    nodetype = node.type().name()
    if (nodetype != "arnold_materialbuilder"):
        print ("Error: Please select shader node instead!")
        hou.ui.displayMessage("Failed: Please select a shader instead!", title="You selected the wrong node!")
        ROP.destroy()
        quit()

    childs = node.children()
    
    for child in childs:
        type = child.type().name()
        
        if (type == "arnold::aov_write_rgb" or type == "arnold::aov_write_float"):
            count += 1
            countstr = str(count)
            aovname = child.parm("aov_name").eval()
            print ("'" + aovname + "'" + " AOV Added!")
            Arnold.parm("ar_aovs").set(count)
            Arnold.parm("ar_aov_label"+countstr).set(aovname)
                  
print("Total count="+countstr)
print("****Create AOV reference ROP success****")
hou.ui.displayMessage("Create AOV reference ROP success!, total AOV count ="+ countstr, title="Yeah!")

        
        



    
