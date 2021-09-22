#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on September 23, 2021, at 00:19
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'Causality'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='\\\\nask.man.ac.uk\\home$\\Desktop\\Causality\\Causality_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "intro"
introClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Please evaluate the following sequences.\n\nIf you consider there is a causal relationship between the objects in the scene (i.e. the first object is causing the stationary one to move) please press the "Y" key.\n\nIf you consider the event does not have a causal nature press the "N".\n\nPress any key to start.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()


initStep = 0.2
upperBound = 400 
#noOfMiniScenes  = 3
noOfMiniScenes = 1

reversals = 0
trialCounter = 1

reversalsSharp = 0
reversalsFlat =  0



levList = [0] * 2
respList = [0] * 2
kestList = [0] * 2
reverseList = [0] * 2
localTrialNo = [0] * 2
staircaseTrialNo = [1] * 2

for i in range(2):
    levList[i] = [0] * (noOfMiniScenes + 2)
    respList[i] = [0] * (noOfMiniScenes + 2)
    kestList[i] = [0] * (noOfMiniScenes + 2)
    reverseList[i] = [0] * (noOfMiniScenes + 2)
    localTrialNo[i] = [0] * (noOfMiniScenes + 2)
    for j in range(noOfMiniScenes + 2):
        levList[i][j] = [0] * 100
        respList[i][j] = [0] * 100
        kestList[i][j] = [0] * 100
        reverseList[i][j] = [0] * 100
        localTrialNo[i][j] = 1
        
globalTrialNo = 60
maxNoFlat = globalTrialNo/(noOfMiniScenes * 2)



# Initialize components for Routine "trial"
trialClock = core.Clock()
upperBound = 0.4
endTime = 0
pause = 0
endTimeSet = 0
A = visual.Rect(
    win=win, name='A',units='cm', 
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
B = visual.Rect(
    win=win, name='B',units='cm', 
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
resp = keyboard.Keyboard()
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
introComponents = [text, key_resp]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=None, waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=60, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    x1 = -20
    x2 = 0
    pauseCalculated = 0 
    endTimeSet = 0
    endTime = 0
    startPos = -20
    rectangleSize = 1
    speedCmS = 40
    
    currentScene = 1
    staircase = round(random()) 
    
    if staircase == 0 and staircaseTrialNo[staircase] > globalTrialNo/2:
        staircase = 1
    if staircase == 1 and staircaseTrialNo[staircase] > globalTrialNo/2:
        staircase = 0
    
    if trialCounter <= globalTrialNo:
        if staircase == 0:
                phi = 0.25
                initN = upperBound
                staircaseTrialNo[staircase] += 1
                if localTrialNo[staircase][currentScene] > maxNoFlat:
                    i = 1 
                    while (i <= noOfMiniScenes): 
                        if localTrialNo[staircase][i] <= maxNoFlat:
                            currentScene = i
                        i = i + 1
        else:
                phi = 0.75
                initN = 0
                staircaseTrialNo[staircase] += 1
                if localTrialNo[staircase][currentScene] > maxNoFlat:
                    i = 1 
                    while (i <= noOfMiniScenes):  
                        if localTrialNo[staircase][i] <= maxNoFlat:              
                            currentScene = i
                        i = i + 1
    
    trial = localTrialNo[staircase][currentScene]
    
    if trial == 1:
       levList[staircase][currentScene][trial] = initN
    elif trial == 2:
        levList[staircase][currentScene][trial] = initN-(initStep/2)*(kestList[staircase][currentScene][trial-1]-phi)
    else:
        levList[staircase][currentScene][trial] = levList[staircase][currentScene][trial-1]-(initStep/(reversals+2))*(kestList[staircase][currentScene][trial-1]-phi)
    
    print("Before quality level is: " + str(levList[staircase][currentScene][trial]))
    # bound range
    if staircase ==  0:
        if levList[staircase][currentScene][trial] > initN:
            levList[staircase][currentScene][trial] = initN
        if levList[staircase][currentScene][trial] < 0:
            levList[staircase][currentScene][trial] = 0
    elif staircase == 1:
        if levList[staircase][currentScene][trial] < initN:
            levList[staircase][currentScene][trial] = initN
        if levList[staircase][currentScene][trial] < 0:
            levList[staircase][currentScene][trial] = 0
    
    pause = levList[staircase][currentScene][trial]
    pauseCalculated = 1
    print("Current pause level is: " + str(pause))
    
    
    
    
    resp.keys = []
    resp.rt = []
    _resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [A, B, resp, ISI]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if pauseCalculated == 1:
            if(x1 < -1):
                x1 = startPos + speedCmS*t
            elif endTimeSet == 0:
                print("Pause is: " + str(pause))
                endTime = t + pause
                endTimeSet = 1
            if (endTime) < t and endTimeSet == 1 and x2 < (-1) * startPos:
                x2 = speedCmS * (t-(endTime))
            print("End time " + str(endTime))
            print("Time " + str(t))
            print("x2 " + str(x2))
            #print(t)
        
        # *A* updates
        if A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            A.frameNStart = frameN  # exact frame index
            A.tStart = t  # local t and not account for scr refresh
            A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A, 'tStartRefresh')  # time at next scr refresh
            A.setAutoDraw(True)
        if A.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > A.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                A.tStop = t  # not accounting for scr refresh
                A.frameNStop = frameN  # exact frame index
                win.timeOnFlip(A, 'tStopRefresh')  # time at next scr refresh
                A.setAutoDraw(False)
        if A.status == STARTED:  # only update if drawing
            A.setPos((x1, 0))
        
        # *B* updates
        if B.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            B.frameNStart = frameN  # exact frame index
            B.tStart = t  # local t and not account for scr refresh
            B.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B, 'tStartRefresh')  # time at next scr refresh
            B.setAutoDraw(True)
        if B.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > B.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                B.tStop = t  # not accounting for scr refresh
                B.frameNStop = frameN  # exact frame index
                win.timeOnFlip(B, 'tStopRefresh')  # time at next scr refresh
                B.setAutoDraw(False)
        if B.status == STARTED:  # only update if drawing
            B.setPos((x2, 0))
        
        # *resp* updates
        waitOnFlip = False
        if resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=['y', 'n'], waitRelease=False)
            _resp_allKeys.extend(theseKeys)
            if len(_resp_allKeys):
                resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                resp.rt = _resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # *ISI* period
        if ISI.status == NOT_STARTED and t >= 2-frameTolerance:
            # keep track of start time/frame for later
            ISI.frameNStart = frameN  # exact frame index
            ISI.tStart = t  # local t and not account for scr refresh
            ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            ISI.start(0.3)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
            ISI.tStop = ISI.tStart + 0.3  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store level and response
    #respList.append(response)
    thisExp.addData('Trial No.', localTrialNo[staircase][currentScene])
    #thisExp.addData('Comp Side', refSide * -1)
    #thisExp.addData('Ref Num', nRefImage)
    thisExp.addData('Level List', levList[staircase][currentScene][trial])
    thisExp.addData('Puase Time', pause)
    thisExp.addData('Staircase', staircase)
    thisExp.addData('Scene No', currentScene)
    
    kestResp = 1
    if resp.keys == 'y':
        kestResp = 0 # causal relation
    
    
    
    kestList[staircase][currentScene][trial] = kestResp
    thisExp.addData('causal?', 'yes' if kestResp == 0 else 'no')
    
    # count reversals
    if localTrialNo[staircase][currentScene] > 1:
        if kestList[staircase][currentScene][trial] != kestList[staircase][currentScene][trial-1]:
            reversals += 1
            reverseList[staircase][currentScene][reversals] = levList[staircase][currentScene][trial-1]
    
    # increment trials
    localTrialNo[staircase][currentScene] += 1
    trialCounter = trialCounter + 1 
    
    
    trials.addData('A.started', A.tStartRefresh)
    trials.addData('A.stopped', A.tStopRefresh)
    trials.addData('B.started', B.tStartRefresh)
    trials.addData('B.stopped', B.tStopRefresh)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
    trials.addData('resp.keys',resp.keys)
    if resp.keys != None:  # we had a response
        trials.addData('resp.rt', resp.rt)
    trials.addData('resp.started', resp.tStartRefresh)
    trials.addData('resp.stopped', resp.tStopRefresh)
    trials.addData('ISI.started', ISI.tStart)
    trials.addData('ISI.stopped', ISI.tStop)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 60 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
