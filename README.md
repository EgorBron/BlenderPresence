# BlenderPresence - a fork of JabkaPresence for adding Rich Presence to Blender
### Blender 3.0 presence with customizable info

## How to use:

#### Clone repository to Blender libraries folder:
```batch
cd %blender path%/3.0/python/lib/site-packages
git clone https://https://github.com/EgorBron/BlenderPresence.git
```

### Install dependencies
```
"%blender path%/3.0/python/bin/python.exe" -m pip install pypresence
```

## Quick examples
### Open "Scripting" layout and create new file in "Text editor".
#### If you want standart RPC:
```python
import blenderpresence
import bpy # blender python api

rpc = blenderpresence.BlenderPresence(bpy)

rpc.run()

# Next, run this script
```

#### Adding configuration:
```python
import blenderpresence
import bpy

rpc = blenderpresence.BlenderPresence(bpy)

rpc.config(
    details = "Working at {project} project", 
    state = "Size: {projectSize}, {objectCount} objects", 
    large_image="{modeCode}", 
    large_image_text="{mode}"
)

rpc.run()
```

#### Custom app and art assets:
```python
import blenderpresence
import bpy

rpc = blenderpresence.BlenderPresence(bpy, app_id = 0) # your app id from Discord Develepers website

def my_codes(mode: str):
    if mode == 'OBJECT':
        return 'objmode' # name of your picture in "Art Assets" tab
    else:
        return 'none'

rpc.config(
    mode_code_processor = my_codes, # will be added in future, sorry :(
    logo_code = 'blender_logo' # name of blender logo picture in "Art Assets" tab
)

rpc.run()
```
