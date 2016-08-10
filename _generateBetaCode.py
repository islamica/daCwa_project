import os, re
import betaCode, betaCodeTables

def translitFile(file):
    with open(file, "r", encoding="utf8") as f:
        text = f.read()
        for i in re.finditer(r"@@.*?@@", text):
            print(i.group())
            iNew = betaCode.betacodeToTranslit(i.group())
            iNewAr = betaCode.betaCodeToArSimple(iNew)
            text = text.replace(i.group(), "%s [[%s]]" % (iNew[2:-2], iNewAr[2:-2]))
        text = text.replace("ﭐ", "ا")
        with open(file, "w", encoding="utf8") as f:
            f.write(text)
        print("To Translit: %s has been processed..." % file)

def processArabicQuotes(file):
    with open(file, "r", encoding="utf8") as f:
        text = f.read()
        for i in re.finditer(r"(<!--@@.*?-->\n)(<p class=\"arabic\">.*?</p>)?", text):
            print(i.group(1)[6:-4])
            iNew = betaCode.betacodeToArabic(i.group(1)[6:-4])
            text = text.replace(i.group(), "%s<p class=\"arabic\">%s</p>" % (i.group(1), iNew))
        with open(file, "w", encoding="utf8") as f:
            f.write(text)
        print("To Arabic: %s has been processed..." % file)

def processRelevant(mainFolder):
    for path, subdirs, files in os.walk(mainFolder):
       for file in files:
           if file.endswith(tuple([".md", ".rec", ".txt", ".html"])):
               print(file)
               f = os.path.join(path, file)
               translitFile(f)
               processArabicQuotes(f)


def folderTest(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


processRelevant("./profiles/")

