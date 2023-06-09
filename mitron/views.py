from django.shortcuts import render

import pyttsx3 

import en_core_web_sm

import speech_recognition as sr
import shutil

import spacy

nlp = spacy.load("en_core_web_sm")

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# def takeCommand():
     
#     r = sr.Recognizer()
#     with sr.Microphone() as source: 
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)
#     try:
#         print("Recognizing...")   
#         query = r.recognize_google(audio, language ='en-in')
#         print(f"User said: {query}\n")
  
#     except Exception as e:
#         print(e)   
#         print("Unable to Recognize your voice.") 
#         return "None"
     
#     return query
# Create your views here.
from django.http import JsonResponse
import chatterbot 
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('Voice Chatbot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

trainerl =  ListTrainer(chatbot)

trainerl.train([

            " 1  " ," Title and extent of operation of the Code ",
            " 2  " ," Punishment of offences committed within India ",
            " 3  " ," Punishment of offences committed beyond, but which by law may be tried within, India ",
            " 4  " ," Extension of Code to extra  : territorial offences ",
            " 5  " ,  " Certain laws not to be affected by this Act ",
            " 6  " ,  " Definitions in the Code to be understood subject to exceptions ",
            " 7  " ,  " Sense of expression once explained ",
            " 8  " ,  " Gender ",
            " 9  " ,  " Number ",
            " 10  " ,  " Man,Woman ",
            " 11  " ,  " Person ",
            " 12  " ,  " Public ",
            " 13  " ,  "  Queen[Repealed] ",
            " 14  " ,  "  Servant of Government ",
            " 15  " ,  "  British India  [Repealed] ",
            " 16  " ,  "  Government of India  [Repealed] ",
            " 17  " ,  "  Government ",
            " 18  " ,  "  India ",
            " 19  " ,  "  Judge ",
            " 20  " ,  "  Court of Justice ",
            " 21  " ,  "  Public Servant ",
            " 22  " ,  "  Movable property ",
            " 23  " ,  "  Wrongful gain ",
            " 24  " ,  "  Dishonestly ",
            " 25  " ,  "  Fraudulently ",
            " 26  " ,  "  Reason to believe ",
            " 27  " ,  " Property in possession of wife, clerk or servant ",
            " 28  " ,  "  Counterfeit ",
            " 29  " ,  "  Document ",
            " 30  " ,  "  Valuable security ",
            " 31  " ,  "  A will",
            " 32  " ,  " Words referring to acts include illegal omissions",
            " 33  " ,  "  Act ,  Omission ",
            " 34  " ,  " Acts done by several persons in furtherance of common intention",
            " 35  " ,  " When such an act is criminal by reason of its being done with a criminal knowledge or intention",
            " 36  " ,  " Effect caused partly by act and partly by omission",
            " 37  " ,  " Co : operation by doing one of several acts constituting an offence",
            " 38  " ,  " Persons concerned in criminal act may be guilty of different offences",
            " 39  " ,  "  Voluntarily",
            " 40  " ,  "  Offence",
            " 41  " ,  "  Special law", 
            " 42  " ,  "  Local law ",
            " 43  " ,  "  Illegal , Legally bound to do", 
            " 44  " ,  "  Injury ",
            " 45  " ,  "  Life ",
            " 46  " ,  "  Death ",
            " 47  " ,  "  Animal ",
            " 48  " ,  "  Vessel ",
            " 49  " ,  "  Year ,  Month ",
            " 50  " ,  "   ",
            " 51  " ,  "  Oath ",
            " 52  " ,  "  Good faith ", 
            " 53  " ,  " Punishments ",
            " 54  " ,  " Commutation of sentence of death ",
            " 55  " ,  " Commutation of sentence of imprisonment for life ",
            " 56  " ,  " Sentence of Europeans and Americans to penal servitude. Proviso as to sentence for term exceeding ten years but not for life [Repealed]",
            " 57  " ,  " Fractions of terms of punishment ",
            " 58  " ,  " Offenders sentenced to transportation how dealt with until transported [Repealed] ",
            " 59  " ,  " Transportation instead of imprisonment [Repealed] ",
            " 60  " ,  " Sentence may be (in certain cases of imprisonment) wholly or partly rigorous or simple ",
            " 61  " ,  " Sentence of forfeiture of property [Repealed] ",
            " 62  " ,  " Forfeiture of property in respect of offenders punishable with death, transportation or imprisonment [Repealed] ",
            " 63  " ,  " Amount of fine ",
            " 64  " ,  " Sentence of imprisonment for non  : payment of fine",
            " 65  " ,  " Limit to imprisonment for non  : payment of fine, when imprisonment and fine awardable",
            " 66  " ,  " Description of imprisonment for non payment of fine",
            " 67  " ,  " Imprisonment for non : payment of fine, when offence punishable with fine only",
            " 68  " ,  " Imprisonment to terminate on payment of fine",
            " 69  " ,  " Termination of imprisonment on payment of proportional part of fine",
            " 70  " ,  " Fine leviable within six years, or during imprisonment– Death not to discharge property from liability",
            " 71  " ,  " Limit of punishment of offence made up of several offences",
            " 72  " ,  " Punishment of person guilty of one of several offences, the judgment stating that it is doubtful of which",
            " 73  " ,  " Solitary confinement",
            " 74  " ,  " Limit of solitary confinement",
            " 75  " ,  " Enhanced punishment for certain offences under Chapter XII or Chapter XVII after previous conviction",
            " 76  " ,  " Act done by a person bound, or by mistake of fact believing himself bound, by law",
            " 77  " ,  " Act of Judge when acting judicially",
            " 78  " ,  " Act done pursuant to the judgment or order of Court",
            " 79  " ,  " Act done by a person justified, or by mistake of fact believing himself justified, by law",
            " 80  " ,  " Accident in doing a lawful act",
            " 81  " ,  " Act likely to cause harm, but done without criminal intent, and to prevent other harm",
            " 82  " ,  " Act of a child under seven years of age",
            " 83  " ,  " Act of a child above seven and under twelve of immature understanding",
            " 84  " ,  " Act of a person of unsound mind",
            " 85  " ,  " Act of a person incapable of judgment by reason of intoxication caused against his will",
            " 86  " ,  " Offence requiring a particular intent or knowledge committed by one who is intoxicated",
            " 87  " ,  " Act not intended and not known to be likely to cause death or grievous hurt, done by consent",
            " 88  " ,  " Act not intended to cause death, done by consent in good faith for person’s benefit",
            " 89  " ,  " Act done in good faith for benefit of child or insane person, by or by consent of guardian",
            " 90  " ,  " Consent known to be given under fear or misconception",
            " 91  " ,  " Exclusion of acts which are offences independently of harm caused",
            " 92  " ,  " Act done in good faith for benefit of a person without consent",
            " 93  " ,  " Communication made in good faith",
            " 94  " ,  " Act to which a person is compelled by threats",
            " 95  " ,  " Act causing slight harm",
            " 96 to 106  " ,  " Of the Right of Private Defence",
            " 96  " ,  " Things done in private defence",
            " 97  " ,  " Right of private defence of the body and of property",
            " 98  " ,  " Right of private defence against the act of a person of unsound mind, etc.",
            " 99  " ,  " Acts against which there is no right of private defence",
            " 100  " ,  " When the right of private defence of the body extends to causing death",
            " 101  " ,  " When such right extends to causing any harm other than death",
            " 102  " ,  " Commencement and continuance of the right of private defence of the body",
            " 103  " ,  " When the right of private defence of property extends to causing death",
            " 104  " ,  " When such right extends to causing any harm other than death",
            " 105  " ,  " Commencement and continuance of the right of private defence of property",
            " 106  " ,  " Right of private defence against deadly assault when there is risk of harm to innocent person",
            " 107  " ,  " Abetment of a thing",
            " 108  " ,  " Abettor",
            " 109  " ,  " Punishment of abetment if the act abetted is committed in consequence, and where no express provision is made for its punishment",
            " 110  " ,  " Punishment of abetment if person abetted does act with different intention from that of abettor",
            " 111  " ,  " Liability of abettor when one act abetted and different act done",
            " 112  " ,  " Abettor when liable to cumulative punishment for act abetted and for act done",
            " 113  " ,  " Liability of abettor for an effect caused by the act abetted different from that intended by the abettor",
            " 114  " ,  " Abettor present when offence is committed",
            " 115  " ,  " Abetment of offence punishable with death or imprisonment for life–if offence not committed",
            " 116  " ,  " Abetment of offence punishable with imprisonment–if offence be not committed",
            " 117  " ,  " Abetting commission of offence by the public or by more than ten persons",
            " 118  " ,  " Concealing design to commit offence punishable with death or imprisonment for life",
            " 119  " ,  " Public servant concealing design to commit offence which it is his duty to prevent",
            " 120  " ,  " Concealing design to commit offence punishable with imprisonment.",
            " 122  " ,  " Collecting arms, etc., with intention of waging war against the Government of India",
            " 123  " ,  " Concealing with intent to facilitate design to wage war",
            " 124  " ,  " Assaulting President, Governor, etc., with intent to compel or restrain the exercise of any lawful power",
            " 125  " ,  " Waging war against any Asiatic Power in alliance with the Government of India",
            " 126  " ,  " Committing depredation on territories of Power at peace with the Government of India",
            " 127  " ,  " Receiving property taken by war on depredation mentioned in IPC Sections 125 and 126",
            " 128  " ,  " Public servant voluntarily allowing prisoner of State or war to escape",
            " 129  " ,  " Public servant negligently suffering such prisoner to escape",
            " 130  " ,  " Aiding escape of, rescuing or harbouring such prisoner",
            " 131  " ,  " Abetting mutiny, or attempting to seduce a soldier, sailor or airman from his duty",
            " 132  " ,  " Abetment of mutiny, if mutiny is committed in consequence thereof",
            " 133  " ,  " Abetment of assault by soldier, sailor or airman on his superior officer, when in execution of his office",
            " 134  " ,  " Abetment of such assault, if the assault is committed",
            " 135  " ,  " Abetment of desertion of soldier, sailor or airman",
            " 136  " ,  " Harbouring deserter",
            " 137  " ,  " Deserter concealed on board merchant vessel through negligence of master",
            " 138  " ,  " Abetment of act of insubordination by soldier, sailor or airman",
            " 139  " ,  " Persons subject to certain Acts",
            " 140  " ,  " Wearing garb or carrying token used by soldier, sailor or airman",
            " 141  " ,  " Unlawful assembly",
            " 142  " ,  " Being member of unlawful assembly",
            " 143  " ,  " Punishment",
            " 144  " ,  " Joining unlawful assembly armed with deadly weapon",
            " 145  " ,  " Joining or continuing in unlawful assembly, knowing it has been commanded to disperse",
            " 146  " ,  " Rioting",
            " 147  " ,  " Punishment for rioting",
            " 148  " ,  " Rioting, armed with deadly weapon",
            " 149  " ,  " Every member of unlawful assembly guilty of offence committed in prosecution of common object",
            " 150  " ,  " Hiring, or conniving at hiring, of persons to join unlawful assembly",
            " 151  " ,  " Knowingly joining or continuing in assembly of five or more persons after it has been commanded to disperse",
            " 152  " ,  " Assaulting or obstructing public servant when suppressing riot, etc.",
            " 153  " ,  " Wantonly giving provocation with intent to cause riot–if rioting be committed–if not committed",
            " 154  " ,  " Owner or occupier of land on which an unlawful assembly is held",
            " 155  " ,  " Liability of person for whose benefit riot is committed",
            " 156  " ,  " Liability of agent of owner or occupier for whose benefit riot is committed",
            " 157  " ,  " Harbouring persons hired for an unlawful assembly",
            " 158  " ,  " Being hired to take part in an unlawful assembly or riot",
            " 159  " ,  " Affray",
            " 160  " ,  " Punishment for committing affray.",
            " 161  " ,  " [Repealed]",
            " 162  " ,  " [Repealed]",
            " 163  " ,  " [Repealed]",
            " 164  " ,  " [Repealed]",
            " 165  " ,  " [Repealed]",
            " 167  " ,  " Public servant framing an incorrect document with intent to cause injury",
            " 168  " ,  " Public servant unlawfully engaging in trade",
            " 169  " ,  " Public servant unlawfully buying or bidding for property",
            " 170  " ,  " Personating a public servant",
            " 171  " ,  " Wearing garb or carrying token used by public servant with fraudulent intent" ])

lawdict= {
            "IPC Section 1  " :  " Title and extent of operation of the Code ",
            "IPC Section 2  " :  " Punishment of offences committed within India ",
            "IPC Section 3  " :  " Punishment of offences committed beyond, but which by law may be tried within, India ",
            "IPC Section 4  " :  " Extension of Code to extra  : territorial offences ",
            "IPC Section 5  " :  " Certain laws not to be affected by this Act ",
            "IPC Section 6  " :  " Definitions in the Code to be understood subject to exceptions ",
            "IPC Section 7  " :  " Sense of expression once explained ",
            "IPC Section 8  " :  " Gender ",
            "IPC Section 9  " :  " Number ",
            "IPC Section 10  " :  " Man,Woman ",
            "IPC Section 11  " :  " Person ",
            "IPC Section 12  " :  " Public ",
            "IPC Section 13  " :  "  Queen[Repealed] ",
            "IPC Section 14  " :  "  Servant of Government ",
            "IPC Section 15  " :  "  British India  [Repealed] ",
            "IPC Section 16  " :  "  Government of India  [Repealed] ",

            "IPC Section 17  " :  "  Government ",
            "IPC Section 18  " :  "  India ",
            "IPC Section 19  " :  "  Judge ",
            "IPC Section 20  " :  "  Court of Justice ",
            "IPC Section 21  " :  "  Public Servant ",
            "IPC Section 22  " :  "  Movable property ",
            "IPC Section 23  " :  "  Wrongful gain ",
            "IPC Section 24  " :  "  Dishonestly ",
            "IPC Section 25  " :  "  Fraudulently ",
            "IPC Section 26  " :  "  Reason to believe ",
            "IPC Section 27  " :  " Property in possession of wife, clerk or servant ",
            "IPC Section 28  " :  "  Counterfeit ",
            "IPC Section 29  " :  "  Document ",
            "IPC Section 30  " :  "  Valuable security ",
            "IPC Section 31  " :  "  A will",
            "IPC Section 32  " :  " Words referring to acts include illegal omissions",
            "IPC Section 33  " :  "  Act ,  Omission ",
            "IPC Section 34  " :  " Acts done by several persons in furtherance of common intention",
            "IPC Section 35  " :  " When such an act is criminal by reason of its being done with a criminal knowledge or intention",
            "IPC Section 36  " :  " Effect caused partly by act and partly by omission",
            "IPC Section 37  " :  " Co : operation by doing one of several acts constituting an offence",
            "IPC Section 38  " :  " Persons concerned in criminal act may be guilty of different offences",
            "IPC Section 39  " :  "  Voluntarily",
            "IPC Section 40  " :  "  Offence",
            "IPC Section 41  " :  "  Special law", 
            "IPC Section 42  " :  "  Local law ",
            "IPC Section 43  " :  "  Illegal , Legally bound to do", 
            "IPC Section 44  " :  "  Injury ",
            "IPC Section 45  " :  "  Life ",
            "IPC Section 46  " :  "  Death ",
            "IPC Section 47  " :  "  Animal ",
            "IPC Section 48  " :  "  Vessel ",
            "IPC Section 49  " :  "  Year ,  Month ",
            "IPC Section 50  " :  "  IPC Section ",
            "IPC Section 51  " :  "  Oath ",
            "IPC Section 52  " :  "  Good faith ", 
            "IPC Section 53  " :  " Punishments ",
            "IPC Section 54  " :  " Commutation of sentence of death ",
            "IPC Section 55  " :  " Commutation of sentence of imprisonment for life ",
            "IPC Section 56  " :  " Sentence of Europeans and Americans to penal servitude. Proviso as to sentence for term exceeding ten years but not for life [Repealed]",
            "IPC Section 57  " :  " Fractions of terms of punishment ",
            "IPC Section 58  " :  " Offenders sentenced to transportation how dealt with until transported [Repealed] ",
            "IPC Section 59  " :  " Transportation instead of imprisonment [Repealed] ",
            "IPC Section 60  " :  " Sentence may be (in certain cases of imprisonment) wholly or partly rigorous or simple ",
            "IPC Section 61  " :  " Sentence of forfeiture of property [Repealed] ",
            "IPC Section 62  " :  " Forfeiture of property in respect of offenders punishable with death, transportation or imprisonment [Repealed] ",
            "IPC Section 63  " :  " Amount of fine ",
            "IPC Section 64  " :  " Sentence of imprisonment for non  : payment of fine",
            "IPC Section 65  " :  " Limit to imprisonment for non  : payment of fine, when imprisonment and fine awardable",
            "IPC Section 66  " :  " Description of imprisonment for non payment of fine",
            "IPC Section 67  " :  " Imprisonment for non : payment of fine, when offence punishable with fine only",
            "IPC Section 68  " :  " Imprisonment to terminate on payment of fine",
            "IPC Section 69  " :  " Termination of imprisonment on payment of proportional part of fine",
            "IPC Section 70  " :  " Fine leviable within six years, or during imprisonment– Death not to discharge property from liability",
            "IPC Section 71  " :  " Limit of punishment of offence made up of several offences",
            "IPC Section 72  " :  " Punishment of person guilty of one of several offences, the judgment stating that it is doubtful of which",
            "IPC Section 73  " :  " Solitary confinement",
            "IPC Section 74  " :  " Limit of solitary confinement",
            "IPC Section 75  " :  " Enhanced punishment for certain offences under Chapter XII or Chapter XVII after previous conviction",
            "IPC Section 76  " :  " Act done by a person bound, or by mistake of fact believing himself bound, by law",
            "IPC Section 77  " :  " Act of Judge when acting judicially",
            "IPC Section 78  " :  " Act done pursuant to the judgment or order of Court",
            "IPC Section 79  " :  " Act done by a person justified, or by mistake of fact believing himself justified, by law",
            "IPC Section 80  " :  " Accident in doing a lawful act",
            "IPC Section 81  " :  " Act likely to cause harm, but done without criminal intent, and to prevent other harm",
            "IPC Section 82  " :  " Act of a child under seven years of age",
            "IPC Section 83  " :  " Act of a child above seven and under twelve of immature understanding",
            "IPC Section 84  " :  " Act of a person of unsound mind",
            "IPC Section 85  " :  " Act of a person incapable of judgment by reason of intoxication caused against his will",
            "IPC Section 86  " :  " Offence requiring a particular intent or knowledge committed by one who is intoxicated",
            "IPC Section 87  " :  " Act not intended and not known to be likely to cause death or grievous hurt, done by consent",
            "IPC Section 88  " :  " Act not intended to cause death, done by consent in good faith for person’s benefit",
            "IPC Section 89  " :  " Act done in good faith for benefit of child or insane person, by or by consent of guardian",
            "IPC Section 90  " :  " Consent known to be given under fear or misconception",
            "IPC Section 91  " :  " Exclusion of acts which are offences independently of harm caused",
            "IPC Section 92  " :  " Act done in good faith for benefit of a person without consent",
            "IPC Section 93  " :  " Communication made in good faith",
            "IPC Section 94  " :  " Act to which a person is compelled by threats",
            "IPC Section 95  " :  " Act causing slight harm",
            "IPC Section 96 to 106  " :  " Of the Right of Private Defence",
            "IPC Section 96  " :  " Things done in private defence",
            "IPC Section 97  " :  " Right of private defence of the body and of property",
            "IPC Section 98  " :  " Right of private defence against the act of a person of unsound mind, etc.",
            "IPC Section 99  " :  " Acts against which there is no right of private defence",
            "IPC Section 100  " :  " When the right of private defence of the body extends to causing death",
            "IPC Section 101  " :  " When such right extends to causing any harm other than death",
            "IPC Section 102  " :  " Commencement and continuance of the right of private defence of the body",
            "IPC Section 103  " :  " When the right of private defence of property extends to causing death",
            "IPC Section 104  " :  " When such right extends to causing any harm other than death",
            "IPC Section 105  " :  " Commencement and continuance of the right of private defence of property",
            "IPC Section 106  " :  " Right of private defence against deadly assault when there is risk of harm to innocent person",
            "IPC Section 107  " :  " Abetment of a thing",
            "IPC Section 108  " :  " Abettor",
            "IPC Section 109  " :  " Punishment of abetment if the act abetted is committed in consequence, and where no express provision is made for its punishment",
            "IPC Section 110  " :  " Punishment of abetment if person abetted does act with different intention from that of abettor",
            "IPC Section 111  " :  " Liability of abettor when one act abetted and different act done",
            "IPC Section 112  " :  " Abettor when liable to cumulative punishment for act abetted and for act done",
            "IPC Section 113  " :  " Liability of abettor for an effect caused by the act abetted different from that intended by the abettor",
            "IPC Section 114  " :  " Abettor present when offence is committed",
            "IPC Section 115  " :  " Abetment of offence punishable with death or imprisonment for life–if offence not committed",
            "IPC Section 116  " :  " Abetment of offence punishable with imprisonment–if offence be not committed",
            "IPC Section 117  " :  " Abetting commission of offence by the public or by more than ten persons",
            "IPC Section 118  " :  " Concealing design to commit offence punishable with death or imprisonment for life",
            "IPC Section 119  " :  " Public servant concealing design to commit offence which it is his duty to prevent",
            "IPC Section 120  " :  " Concealing design to commit offence punishable with imprisonment.",
            "IPC Section 122  " :  " Collecting arms, etc., with intention of waging war against the Government of India",
            "IPC Section 123  " :  " Concealing with intent to facilitate design to wage war",
            "IPC Section 124  " :  " Assaulting President, Governor, etc., with intent to compel or restrain the exercise of any lawful power",
            "IPC Section 125  " :  " Waging war against any Asiatic Power in alliance with the Government of India",
            "IPC Section 126  " :  " Committing depredation on territories of Power at peace with the Government of India",
            "IPC Section 127  " :  " Receiving property taken by war on depredation mentioned in IPC Sections 125 and 126",
            "IPC Section 128  " :  " Public servant voluntarily allowing prisoner of State or war to escape",
            "IPC Section 129  " :  " Public servant negligently suffering such prisoner to escape",
            "IPC Section 130  " :  " Aiding escape of, rescuing or harbouring such prisoner",
            "IPC Section 131  " :  " Abetting mutiny, or attempting to seduce a soldier, sailor or airman from his duty",
            "IPC Section 132  " :  " Abetment of mutiny, if mutiny is committed in consequence thereof",
            "IPC Section 133  " :  " Abetment of assault by soldier, sailor or airman on his superior officer, when in execution of his office",
            "IPC Section 134  " :  " Abetment of such assault, if the assault is committed",
            "IPC Section 135  " :  " Abetment of desertion of soldier, sailor or airman",
            "IPC Section 136  " :  " Harbouring deserter",
            "IPC Section 137  " :  " Deserter concealed on board merchant vessel through negligence of master",
            "IPC Section 138  " :  " Abetment of act of insubordination by soldier, sailor or airman",
            "IPC Section 139  " :  " Persons subject to certain Acts",
            "IPC Section 140  " :  " Wearing garb or carrying token used by soldier, sailor or airman",
            "IPC Section 141  " :  " Unlawful assembly",
            "IPC Section 142  " :  " Being member of unlawful assembly",
            "IPC Section 143  " :  " Punishment",
            "IPC Section 144  " :  " Joining unlawful assembly armed with deadly weapon",
            "IPC Section 145  " :  " Joining or continuing in unlawful assembly, knowing it has been commanded to disperse",
            "IPC Section 146  " :  " Rioting",
            "IPC Section 147  " :  " Punishment for rioting",
            "IPC Section 148  " :  " Rioting, armed with deadly weapon",
            "IPC Section 149  " :  " Every member of unlawful assembly guilty of offence committed in prosecution of common object",
            "IPC Section 150  " :  " Hiring, or conniving at hiring, of persons to join unlawful assembly",
            "IPC Section 151  " :  " Knowingly joining or continuing in assembly of five or more persons after it has been commanded to disperse",
            "IPC Section 152  " :  " Assaulting or obstructing public servant when suppressing riot, etc.",
            "IPC Section 153  " :  " Wantonly giving provocation with intent to cause riot–if rioting be committed–if not committed",
            "IPC Section 154  " :  " Owner or occupier of land on which an unlawful assembly is held",
            "IPC Section 155  " :  " Liability of person for whose benefit riot is committed",
            "IPC Section 156  " :  " Liability of agent of owner or occupier for whose benefit riot is committed",
            "IPC Section 157  " :  " Harbouring persons hired for an unlawful assembly",
            "IPC Section 158  " :  " Being hired to take part in an unlawful assembly or riot",
            "IPC Section 159  " :  " Affray",
            "IPC Section 160  " :  " Punishment for committing affray.",
            "IPC Section 161  " :  " [Repealed]",
            "IPC Section 162  " :  " [Repealed]",
            "IPC Section 163  " :  " [Repealed]",
            "IPC Section 164  " :  " [Repealed]",
            "IPC Section 165  " :  " [Repealed]",
            "IPC Section 167  " :  " Public servant framing an incorrect document with intent to cause injury",
            "IPC Section 168  " :  " Public servant unlawfully engaging in trade",
            "IPC Section 169  " :  " Public servant unlawfully buying or bidding for property",
            "IPC Section 170  " :  " Personating a public servant",
            "IPC Section 171  " :  " Wearing garb or carrying token used by public servant with fraudulent intent"}

def index(request):
    return render(request,'index.html')

def get_response(request):
    
    
    while(True):

        answ=""
        user_message = request.GET.get('message')

        if user_message.isdigit():
            x=int(user_message)    

            if 1<=x<=5:
                resp="Chapter1 : Introduction"
            elif 6<=x<=52:
                resp="Chapter2 : General Explanations"
            elif 53<=x<=75:
                resp="Chapter3 : Punishments"
            elif 76<=x<=106:
                resp="Chapter4 : General Exceptions of the Right of Private Defense" 
            elif 107<=x<=120:  
                resp="Chapter5 : Abetment"
            elif 121<=x<=130: 
                resp="Chapter6 : Offences against the State"
            elif 131<=x<=140: 
                resp="Chapter7 : Offences relating to the Army, Navy and Air Force"
            elif 141<=x<=160:  
                resp="Chapter8 : Offences against the Public Tranquility"
            elif 161<=x<=171:  
                resp="Chapter9 : Offences by or relating to Public Servants"
            
            bot_response =resp+"  "+str(chatbot.get_response(user_message))

        else:
            res = [key for key, val in lawdict.items() if user_message in val]
            for law in res:
                answ+=law+","
            bot_response ="Section number of IPC law your query relates to "+answ+" If you would like to more about these sections enter section number of article"

        return JsonResponse({'message': bot_response})
