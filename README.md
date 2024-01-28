

#############################################################################################


# From Mind To Brain, 2023
# Routine for silent-production Analogy study with Tobias Scheer @ CNRS, BCL Laboratory, Cote d'Azure, France | VERSION 2.0 with photodiode accuracy implemented
# Sayantan Mandal // s.mandal@eversincechomsky.com 
#############################################################################################



Construction stimuli set analogy French -al

0. word types according to their plural
a. -aux (journal) (non-ambiguous)
b. ‑als (carnaval) (non-ambiguous)
c. ambiguous: terminal (real word) plus all nonce words
d. -s (sac)

1. our goal is to record what happens when speakers don't know what to do, i.e. have no clue whether the pl is in -aux or -als. This is the case
a. in nonce words
b. in ambiguous real words (type terminal)

2. our direct controls are cases where the -als plural is unchallenged: type carnaval.
Indirect controls are words that don't end in -al and have the regular zero plural -s: type sac - sacs etc.
These two types should be produced by the same mechanism and hence show the same EEG footprint.

3. for the -aux plural type (journal), two analyses are to be considered:
a. suppletion: both sg and pl are stored
b. allomorphy: speakers have stored two allomorphs for the pl morpheme, -s and -aux. All plural forms of the language are then allomorphic, i.e. all roots are lexically marked for selecting either pl allomorph.
Suppletion appears to be more reasonable than allomorphy. Our experimental setup should be able to tell: 
– if aux plurals are produced by allomorphy, they should have the same EEG signature as regular -s plurals (type sac - sacs).
– suppletion should produce an effect at 200ms, but allomorphy at 320ms.

4. analogy occurs when i) speakers don't know what to do and ii) choose -aux.
Hence there are two production routines to arrive at surface ‑aux:
a. by suppletion / allomorphy (type journal)
b. by analogy (ambiguous type terminal, nonce words).
What makes the latter (ambiguous words (type terminal) and nonce words) different from both regular -aux (type journal) and -s (type sac) plurals is that they don't have any lexical specification for plural formation.
This is true in case -aux plurals (type journal) are instances of suppletion (no pl form recorded) as much as in case they are produced by allomorphy (root unmarked for the selection of either pl allomorph).

6. what to do when we get experimental results
a. compare type -als (carnaval) and type -s (sac), they should be the same.
b. check whether type -aux (journal) shows an effect at 320 or not (yes = allomorphy, no = suppletion).
c. compare type -aux (journal) and type -s (sac): if they are the same there is a language-wide allomorphy -s / -aux. If they are not, there is no general plural allomorphy in the language: type -s is not allomorphic (but type -aux may still be).
d. [our actual target] compare candidates for analogy for which speakers have produced -aux (ambiguous type terminal and nonce words) with 
– regular type -aux (journal): should be different
– type -als (carnaval): should be different
– type -s (sac): should be different

If different wrt to all three, we have isolated the EEG signature of analogy.

#############################################################################################

SUMMARY OF TIMING SYNCHRONIZATION USING PHOTODIODE AND BITMAP
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
