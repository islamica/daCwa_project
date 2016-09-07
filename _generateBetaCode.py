#!/usr/bin/env python3

import os, re
import betaCode, betaCodeTables

def translitFile(input_file):
    with open(input_file, "r", encoding="utf8") as f:
        text = f.read()
        for i in re.finditer(r"@@.*?@@", text):
            # print(i.group())
            iNew = betaCode.betacodeToTranslit(i.group())
            iNewAr = betaCode.betaCodeToArSimple(iNew)
            text = text.replace(i.group(), "%s [[%s]]" % (iNew[2:-2], iNewAr[2:-2]))
        text = text.replace("ﭐ", "ا")
        output_file = input_file.replace("profiles", "profiles_output")
        with open(output_file, "w", encoding="utf8") as f:
            f.write(text)
            # print(output_file)
        print("To Translit: {} has been processed as {}.".format(input_file, output_file))

def processArabicQuotes(input_file):
    with open(input_file, "r", encoding="utf8") as f:
        text = f.read()
        for i in re.finditer(r"(<!--@@.*?-->\n)(<p class=\"arabic\">.*?</p>)?", text):
            # print(i.group(1)[6:-4])
            iNew = betaCode.betacodeToArabic(i.group(1)[6:-4])
            text = text.replace(i.group(), "%s<p class=\"arabic\">%s</p>" % (i.group(1), iNew))
        output_file = input_file
        with open(output_file, "w", encoding="utf8") as f:
            f.write(text)
            # print(output_file)
        print("To Translit: {} has been processed as {}.".format(input_file, output_file))

def processProfiles(mainFolder, methodToCall):
    for path, subdirs, files in os.walk(mainFolder):
       for file in files:
           if file.endswith(tuple([".md", ".rec", ".txt", ".html"])):
               file_with_full_path = os.path.join(path, file)
               globals()[methodToCall](file_with_full_path)

def folderTest(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

processProfiles("./profiles/", "translitFile")
processProfiles("./profiles_output/", "processArabicQuotes")
