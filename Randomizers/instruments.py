import Tools.event_tools as event_tools



def writeInstrumentEvent(flow, room, flag, getAnim):
    event_tools.addEntryPoint(flow.flowchart, room)

    event_tools.createActionChain(flow.flowchart, room, [
        ('SinkingSword', 'Destroy', {}),
        ('EventFlags', 'SetFlag', {'symbol': flag, 'value': True})
    ], getAnim)



def writeRoomData(roomData, room, modelPath, modelName, flag):
    for act in roomData.actors:
        if act.type in [157, 158, 159, 160, 161, 162, 163, 164]: # each instrument has its own type
            # store the level and location for the leveljump event since we will overwrite these parameters
            level = str(act.parameters[0], 'utf-8')
            location = str(act.parameters[1], 'utf-8')
            act.type = 0x8D # bird key
            act.parameters[0] = bytes(modelPath, 'utf-8')
            act.parameters[1] = bytes(modelName, 'utf-8')
            act.parameters[2] = bytes(room, 'utf-8') # entry point that we write to flow
            act.parameters[3] = bytes(flag, 'utf-8') # flag for if item appears
    
    return level, location



def insertInstrumentFadeEvent(flowchart, level, location):
    return event_tools.createActionChain(flowchart, None, [
        ('Audio', 'StopAllBGM', {'duration': 1.0}),
        ('Link', 'PlayInstrumentShineEffect', {}),
        # ('Timer', 'Wait', {'time': 2}),
        ('Audio', 'StopOtherThanSystemSE', {'duration': 3.0}),
        ('Audio', 'PlayOneshotSystemSE', {'label': 'SE_ENV_GET_INST_WHITEOUT2', 'pitch': 1.0, 'volume': 1.0}),
        ('Fade', 'StartPreset', {'preset': 3}),
        ('Fade', 'StartParam', {'colorB': 0.9, 'colorG': 0.9, 'colorR': 0.9, 'mode': 2, 'time': 0.75}),
        ('Timer', 'Wait', {'time': 2}),
        ('GameControl', 'RequestLevelJump', {'level': level, 'locator': location, 'offsetX': 0.0, 'offsetZ': 0.0}),
        ('GameControl', 'RequestAutoSave', {})
    ], None)
