from plumbum import cli, colors, local
import os

path = "/home/mattia/.notes/"
if not os.path.exists(path):
    os.makedirs(path)
file = path + "notes.txt"

class Notes(cli.Application):
    "simple notes handler"

    PROGNAME = "Notes"
    VERSION = "0.2"

    def main(self):
        if not self.nested_command:
            print("No command given")
            return 1

@Notes.subcommand("add")
class add(cli.Application):
    "add a note given a string of character"

    priority = cli.Flag(["p","prioritize"], help = "if given, it will add a danger mark to the note")

    def main(self, *toadd: str):
        nota = " ".join(toadd)
        if not os.path.exists(file):
            f = open(file,"w+")
            f = open(file,"a")
            f.write("[ ] "  + nota +"\n")
        elif self.priority :
            f = open(file,"a")
            danger = colors.yellow | "\u26A0"
            f.write("[ ] "  + nota + " " + danger +"\n")
        else :
            f = open(file,"a")
            f.write("[ ] " + nota + "\n")

@Notes.subcommand("show")
class show(cli.Application):
    "show the notes file"

    def main(self):
        if not os.path.exists(file):
            print("no notes.txt file found, try the option 'add' to write a new one")
        else :
            a = open(file,"r").read()
            print(a,end = "")

@Notes.subcommand("find")
class find(cli.Application):
    "search on notes file for keywords"

    def main(self, *keywords: str):
        key = " ".join(keywords).lower()
        found = 0
        if not os.path.exists(file):
            print("no notes.txt file found")
        else :
            for line in open(file,"r"):
                if key in line.lower():
                    print(line)
                    found += 1
        if found is False:
            print("key not found \n")

@Notes.subcommand("done")
class done(cli.Application):
    "check the notes that has been done, ask for a keyword"

    def main(self, *keywords: str):
        key = " ".join(keywords).lower()
        found = 0
        if not os.path.exists(file):
            print("no notes.txt file found, add a note to create it")
        else :
            copy = "copynotes.txt"
            c = open(path + copy,"w+")
            f = open(file,"r")
            for line in f:
                if key in line.lower():
                    green_tick = colors.green | "\u2713"
                    line = line.replace("[ ]","["+green_tick+"]")
                    c.write(line)
                    found += 1
                else :
                    c.write(line)
            c.close()
            f.close()
            if found is False:
                print("key not found")
            else:
                mv = local["mv"]
                mv(path+copy,file)

@Notes.subcommand("clear")
class clear(cli.Application):
    """it will clear ALL the notes if no options are given,\n
    else it will clear Notes with a given keyword.\n
    Flag -d will clear ticked notes.
    """

    done_clear = cli.Flag(["d","done"], help = "it will clear ticked notes")

    def main(self, *keywords : str):
        if not os.path.exists(file):
            print("no notes.txt file found, add a note to create it")
        elif len(keywords) == 0 and not self.done_clear:
            rm = local["rm"]
            rm(file)
        elif self.done_clear:
            key = " ".join(keywords)
            found = 0
            green_tick = colors.green | "\u2713"
            copy = path + "copynotes.txt"
            c = open(copy,"w+")
            f = open(file,"r")
            for line in f:
                if green_tick in line:
                    found += 1
                else :
                    c.write(line)
            f.close()
            c.close()
            if found is 0:
                print (green_tick + " not found", end = "\n")
            else :
                mv = local["mv"]
                mv(copy, file)
        else :
            found = 0
            key = " ".join(keywords)
            key = key.lower()
            copy = path + "copynotes.txt"
            c = open(copy,"w+")
            f = open(file,"r")
            for line in f:
                if key in line.lower():
                    found += 1
                else :
                    c.write(line)
            f.close()
            c.close()
            if found is 0:
                print ("keyword not found", end = "\n")
            else :
                mv = local["mv"]
                mv(copy, file)

if __name__ == "__main__":
    Notes.run()
