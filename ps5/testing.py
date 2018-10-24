
import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        assert len([punc for punc in string.punctuation if punc in phrase]) == 0, "Punctuation mark(s) present in " \
                                                                                  "phrase."
        assert len([char for char in phrase.strip().split(" ") if char == ""]) == 0, "Phrase contains multiple " \
                                                                                    "spaces between words."
        self.phrase = phrase.strip().lower()

    # def is_phrase_in(self, text):
    #     newtext = text.lower().split(" ")
    #     output = []
    #     for word in newtext:
    #         if word == '':
    #             continue
    #         elif sum([punc in word for punc in string.punctuation]) > 0:
    #             newword = str()
    #             for char in word:
    #                 if char in string.punctuation:
    #                     continue
    #                 else:
    #                     newword += char
    #             output.append(newword)
    #         else:
    #             output.append(word)
    #     text1 = ' '.join(output)
    #
    #     if self.phrase in text1:
    #         return True
    #     else:
    #         return False

    def is_phrase_in(self, text):

        newtext = str()
        for char in text:
            if char in string.punctuation:
                newtext += " "
            else:
                newtext += char

        newtext1 = newtext.lower().split(" ")
        output = []
        for word in newtext1:
            if word == '':
                continue
            else:
                output.append(word)
        text1 = ' '.join(output)

        if self.phrase in text1:
            if self.phrase.split(" ") == [word for word in self.phrase.split(" ") if word in text1.split(" ")]:
                return True
            else:
                return False
        else:
            return False

# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        title = story.get_title()
        if self.is_phrase_in(title):
            return True
        else:
            return False


# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        desc = story.get_description()
        if self.is_phrase_in(desc):
            return True
        else:
            return False

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, timestring):
        assert isinstance(timestring, str), "Value entered was not a string."
        format = "%d %b %Y %H:%M:%S"
        try:
            dtobj = datetime.strptime(timestring, format)
            dtobj_est = dtobj.replace(tzinfo = pytz.timezone("EST"))
            self.datetime = dtobj_est
        except ValueError as e:
            print("ValueError:", e)

# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def __init__(self, timestring):
        TimeTrigger.__init__(self, timestring)

    def evaluate(self, story):
        if self.datetime > story.get_pubdate():
            return True
        else:
            return False

class AfterTrigger(TimeTrigger):
    def __init__(self, timestring):
        TimeTrigger.__init__(self, timestring)

    def evaluate(self, story):
        if self.datetime < story.get_pubdate():
            return True
        else:
            return False

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, trig):
        self.trig = trig

    def evaluate(self, story):
        trig_eva = self.trig.evaluate(story)
        return not trig_eva

# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trig1, trig2):
        self.trig1 = trig1
        self.trig2 = trig2

    def evaluate(self, story):
        trig_eva = self.trig1.evaluate(story) & self.trig2.evaluate(story)
        return trig_eva

# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trig1, trig2):
        self.trig1 = trig1
        self.trig2 = trig2

    def evaluate(self, story):
        trig_eva = self.trig1.evaluate(story) | self.trig2.evaluate(story)
        return trig_eva


def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    sel_stories = []
    for story in stories:
        for trig in triggerlist:
            if trig.evaluate(story):
                sel_stories.append(story)
                break
            else:
                continue
    return sel_stories

def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    print(lines) # for now, print it so you see what it contains!

    # Running through lines to single out the "ADD" commands, put them into adds = [].
    # Construct a trig_lib with the following structure: trig_lib = {'t1':TitleTrigger("something"), 't2':...} by
    # running through lines.
    # Running through the adds list to add triggers to sel_trigs = []. Return sel_trigs.

    trigger_type1 = ["DESCRIPTION", "TITLE", "AFTER", "BEFORE"]
    trigger_type2 = ["NOT"]
    adds = []
    trig_lib = {}
    for block in lines:
        block_unit = block.split(",")
        if block_unit[0] == "ADD":
            adds.append(block_unit)
        else:
            if block_unit[1] in trigger_type1:
                trig_lib[block_unit[0]] = eval(block_unit[1].title() + "Trigger" + "('" + block_unit[2] + "')")
            elif block_unit[1] in trigger_type2:
                trig_lib[block_unit[0]] = eval(block_unit[1].title() + "Trigger" + "(trig_lib['" + block_unit[2] +
                                               + "'])")
            else:
                trig_lib[block_unit[0]] = eval(block_unit[1].title() + "Trigger" + "(trig_lib['" + block_unit[2] + "']"
                                               + "," + "trig_lib['" + block_unit[3] + "'])")

    print(trig_lib)
    print(adds)
    sel_trigs = []
    for add in adds:
        for i in range(1, len(add)):
            sel_trigs.append(trig_lib[add[i]])
    return sel_trigs

triggerlist = read_trigger_config('triggers.txt')
print(triggerlist)

SLEEPTIME = 120  # seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("medal")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Saudi")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line
        triggerlist = read_trigger_config('triggers.txt')

        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica", 14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []

        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title() + "\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:
            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)

            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e, "something broke")


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()