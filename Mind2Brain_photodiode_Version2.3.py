#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################################################################
# From Mind To Brain, 2023
# Routine for silent-production Analogy study | VERSION 2.0 with photodiode accuracy implemented
# Sayantan Mandal // s.mandal@eversincechomsky.com 
# v1.0: August, 2023.
# v1.1: 12th September, 2023.
# v1.2: 25th September, 2023
# v1.3: 21st October, 2023
# v2.0: 30th November, 2023
# v2.1: 15th December, 2023
# v2.2: 18th December, 2023: Added Training Phase. Adjusted target word time.
# v2.3: 17th January, 2024: Added a recall phase. After every trial the participant gets two options to respond to the question
# "Quel était le dernier mot que vous avez dit?". They respond with "1" for the first option, "0" for the second.

###################################################################################################################
# SUMMARY OF TIMING SYNCHRONIZATION USING PHOTODIODE AND BITMAP
#
# # 1. Presentation of Bitmap Stimulus:
# The bitmap stimulus is a visual event presented on the screen at a precise point in 
# # the experiment. This event is chosen to be visually distinct and easily #identifiable.
##
# # 2. Sending Trigger Code:
# At the same time the bitmap stimulus is presented, a trigger code is sent to the EEG recording system. 
# # This trigger code is a numerical value that uniquely identifies the experimental condition, task type, or any specific event.
#
# # 3. Recording Trigger Code and Timing:
# The script records the trigger code along with the timing information (time from the start of the experiment) when the bitmap 
# # stimulus is presented. The information is then logged to the data files.
#
# # 4. EEG Data Recording:
# Simultaneously, the EEG recording system records the trigger code along with the corresponding EEG data. 
# # The trigger code serves as a marker in the EEG data stream, indicating when specific events or conditions occurred in the #experiment.
#
# # 5. Analysis and Synchronization:
# After the experiment, the recorded EEG data and the experiment data (including trigger codes and timing) need to be analyzed together. 
# # By identifying the trigger codes in the EEG data stream that correspond to the presentation of the 
# # bitmap stimulus, we can align the EEG data with specific events in the experimental timeline.
#
#
#
####################################################################################################################
###################################################################################################





from psychopy import visual, core, event
import pandas as pd
import random
import csv
from itertools import product
import json

# Read the Excel file
stimuli_df = pd.read_excel('stimuli_words.xlsx')

# Extract words for each word type
word_lists = {
    'W1': stimuli_df['Cue Words W1'].tolist(),
    'W2': stimuli_df['Cue Words W2'].tolist(),
    'W3': stimuli_df['Cue Words W3'].tolist(),
    'W4': stimuli_df['Cue Words W4'].tolist()
}

# Extract recall options for each word type
recall_options = {
    'W1': stimuli_df[['Token1_W1', 'Token2_W1']].values.tolist(),
    'W2': stimuli_df[['Token1_W2', 'Token2_W2']].values.tolist(),
    'W3': stimuli_df[['Token1_W3', 'Token2_W3']].values.tolist(),
    'W4': stimuli_df[['Token1_W4', 'Token2_W4']].values.tolist()
}

# Create a window
win = visual.Window(size=(800, 600), color='white', units='pix')

# Define stimuli
stimulus_phrases = {'Read': 'C\'est un', 'Null': 'Ce sont des', 'Overt': 'Ce sont des'}
cue_text = visual.TextStim(win, text='', color='white', height=30)
plus_sign = visual.TextStim(win, text='+', color='white', height=30)
stimulus_word = visual.TextStim(win, text='', color='black', height=30)

# Define conditions
word_types = ['W1', 'W2', 'W3', 'W4']
task_conditions = ['Read', 'Null', 'Overt']

# Mapping of task conditions and word types to numeric values for trigger codes
task_condition_numeric = {'Read': 1, 'Null': 2, 'Overt': 3}
word_type_numeric = {'W1': 4, 'W2': 5, 'W3': 6, 'W4': 7}

# Create a list to store trial data
trials = []

# Generate trial list with controlled randomization
combinations = list(product(word_types, task_conditions))
num_reps = 3  # Number of repetitions for each combination

for _ in range(num_reps):
    random.shuffle(combinations)
    for word_type, task_condition in combinations:
        trial_data = {'word_type': word_type, 'task_condition': task_condition}
        trials.append(trial_data)

# Shuffle the trial list for further randomization
random.shuffle(trials)

# Dictionary to keep track of word counts
word_counts = {word_type: {word: 0 for word in word_lists[word_type]} for word_type in word_types}

# Data logging setup
data_file_csv = 'experiment_data.csv'
fieldnames = ['Trial', 'WordType', 'TaskCondition', 'StimulusWord', 'TriggerCode', 'TimeFromStart', 'BitmapStimulusTime', 'RecallOption', 'ParticipantResponseTime']
with open(data_file_csv, mode='w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

data_file_json = 'experiment_data.json'

# Clock to measure elapsed time from the start
experiment_clock = core.Clock()

# Bitmap stimulus setup
bitmap_stimulus = visual.Rect(win, width=3, height=3, fillColor=[0.8, 0.8, 0.8])  # Light gray square

# Display training phase text
training_text = visual.TextStim(win, text='C\'EST LA PHASE DE FORMATION', color='black', height=30)
training_text.draw()
win.flip()
core.wait(2.0)  # Double the wait time

# Main experiment loop with error handling
try:
    # Display start of the experiment text
    start_text = visual.TextStim(win, text='MAINTENANT, L\'EXPERIENCE COMMENCE', color='black', height=30)
    start_text.draw()
    win.flip()
    core.wait(1.0)  # Standard wait time

    for i, trial_data in enumerate(trials):
        # Cue epoch
        cue_text.text = stimulus_phrases[trial_data['task_condition']]
        cue_text.draw()
        win.flip()
        core.wait(1.3)  # Double the wait time

        plus_sign.draw()
        win.flip()
        core.wait(2.2)  # Double the wait time

        # Response epoch
        word_type = trial_data['word_type']
        available_words = [word for word in word_lists[word_type] if word_counts[word_type][word] < 3]

        if not available_words:
            print(f"All words from {word_type} have been used 3 times. Resetting counts.")
            word_counts[word_type] = {word: 0 for word in word_lists[word_type]}
            available_words = word_lists[word_type]

        selected_word = random.choice(available_words)
        word_counts[word_type][selected_word] += 1

        stimulus_word.text = selected_word
        stimulus_word.draw()
        win.flip()
        core.wait(1.0)  # Double the wait time

        plus_sign.draw()
        win.flip()
        core.wait(3.0)  # Double the wait time

        # Present bitmap stimulus for synchronization
        bitmap_stimulus.draw()
        win.flip()

        # Record timestamp for the bitmap stimulus
        bitmap_stimulus_timestamp = experiment_clock.getTime()
        print(f'Timestamp for Bitmap Stimulus: {bitmap_stimulus_timestamp}')

        # Record triggers and timing
        trigger_code = f'{task_condition_numeric[trial_data["task_condition"]] * 10 + word_type_numeric[trial_data["word_type"]]}'
        time_from_start = experiment_clock.getTime()
        print(f'Trigger Code: {trigger_code}, Time from start: {time_from_start}')

        # Log data to CSV
        with open(data_file_csv, mode='a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({
                'Trial': i + 1,
                'WordType': word_type,
                'TaskCondition': trial_data['task_condition'],
                'StimulusWord': selected_word,
                'TriggerCode': trigger_code,
                'TimeFromStart': time_from_start,
                'BitmapStimulusTime': bitmap_stimulus_timestamp
            })

        # Log data to JSON
        with open(data_file_json, mode='a') as jsonfile:
            data_to_log = {
                'Trial': i + 1,
                'WordType': word_type,
                'TaskCondition': trial_data['task_condition'],
                'StimulusWord': selected_word,
                'TriggerCode': trigger_code,
                'TimeFromStart': time_from_start,
                'BitmapStimulusTime': bitmap_stimulus_timestamp
            }
            json.dump(data_to_log, jsonfile)
            jsonfile.write('\n')

        # Recall phase
        recall_options_text = visual.TextStim(win, text=f'Quel était le dernier mot que vous avez dit?\n'
                                                        f'a. {recall_options[word_type][0]}\n'
                                                        f'b. {recall_options[word_type][1]}',
                                              color='black', height=30)
        recall_options_text.draw()
        win.flip()

        # Record participant response time and option
        keys = event.waitKeys(keyList=['1', '0'], timeStamped=experiment_clock)
        if keys:
            participant_response_time = keys[0][1]
            participant_option = keys[0][0]
            print(f"Participant response time: {participant_response_time} seconds, Option chosen: {participant_option}")

        # Log recall phase data to CSV
        with open(data_file_csv, mode='a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({
                'RecallOption': participant_option,
                'ParticipantResponseTime': participant_response_time
            })

        # Clear the screen
        win.flip()

except Exception as e:
    print(f"An error occurred: {e}")
    # Add specific error-handling actions here if needed

finally:
    # Close the window at the end of the experiment
    win.close()

