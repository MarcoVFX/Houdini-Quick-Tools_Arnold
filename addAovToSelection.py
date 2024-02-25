#name = addAovToSelection
#label = Add AOV to Selection
#icon = hicon:/SVGIcons.index?BUTTONS_aovs.svg

nodes = hou.selectedNodes()
iteration = 0;
nodeCollection = []

for node in nodes:
    #create AOV nodes
    parent = node.parent()
    parentPath = parent.path()
    name = node.name()
    aovwrite = parent.createNode("arnold::aov_write_rgb",name+"__",force_valid_node_name=True)
    
    #set parm and input
    aovwrite.parm("aov_name").set(name)
    aovwrite.setInput(1,node,0)
    aovwrite.setSelected(True)
    
    #add node into collection for layout
    nodeCollection.append(node)
    nodeCollection.append(aovwrite)
      
    #set input
    if (iteration>0):
        lastNode.setInput(0,aovwrite,0)
            
    #create last node
    lastNode = aovwrite
    iteration += 1;

#layout    
parent.layoutChildren(items=(nodeCollection))

