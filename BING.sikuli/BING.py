import random
import org.sikuli.basics.FileManager as FM
html = FM.downloadURLtoString("https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain")
#print "html:", len(html)
#uprint( html)
WORD=random.choice(html.split())
WAIT=random.choice(range(5,27))

sleep(5)

for x in range(35):
    WORD=random.choice(html.split())    
    try:
        type("l", KEY_CTRL)
        type(WORD+Key.ENTER)
        click(Pattern("1618074518523.png").targetOffset(56,-4))
        sleep(WAIT)
        #click(Pattern("1546456063425.png").similar(0.51))
        for y in range(3):
            click(Pattern("1618074549972.png").similar(0.38).targetOffset(-108,4))
        
    except:
        pass
        
    sleep(WAIT)

type("l", KeyModifier.WIN)
run('rundll32.exe user32.dll,LockWorkStation')