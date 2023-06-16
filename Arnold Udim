#name = Arnold Udim
#label = Arnold Udim
#icon = hicon:/SVGIcons.index?BUTTONS_aovs.svg


import re
nodes = hou.selectedNodes()

for node in nodes:

    #Rename to .tx path
    name = node.parm('filename').eval()
    
    findudim = name.find('<udim>')
    
    if findudim == -1:
        pathf = re.sub('(?=\.\d\d\d\d).*.*','',name)
        pathr = re.sub('.*(?=\.)','',name)
        path = pathf + '.<udim>' + pathr
        node.parm('filename').set(path)   
