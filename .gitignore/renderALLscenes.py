import bpy

tmpSceneName = bpy.context.screen.scene.name;

for s in bpy.data.scenes :
    bpy.context.screen.scene = s   #set as the active scene
    #bpy.ops.render.render(animation = True) #render animation
    f= bpy.data.filepath; 
    fp = f.split( bpy.path.basename(bpy.data.filepath))[0]; 
    fp = fp + "Rendered_Scenes\\" + bpy.context.scene.name + ".jpg";
    bpy.context.scene.render.filepath = fp;
    bpy.ops.render.render( write_still=True )  # for still render
    
bpy.context.screen.scene = bpy.data.scenes[tmpSceneName]   