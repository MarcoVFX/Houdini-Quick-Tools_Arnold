#name = Change to tx
#label = Change to tx
#icon = hicon:/SVGIcons.index?BUTTONS_icons_medium.svg


import re
nodes = hou.selectedNodes()

for node in nodes:
    type = node.type().name()
    
    #Rename to .tx path
    name = node.parm('filename').eval()
    path = re.sub('(tx)|((png)|(jpg)|(tif)|(exr))$',"",name)
    path += 'tx'
    node.parm('filename').set(path)
    node.setColor(hou.Color(0.839,0.839,0.839))
    
    
    #Rename back to regular nodes
    nodename = re.sub('(\w\:)|(\w)*(\/)|(\w)*(\s)|(\.)|(tx)|(png)|(jpg)|(tif)|(exr)|(<udim>)','',name)
    node.setName(nodename, unique_name=True)
