# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re
import subprocess
import requests


def herokuize(name):

    with open(name, 'r') as fileinput:
        for line in fileinput:
            print (line)
            m = re.search(r'https://[^ ]*', line)
            if not m:
                continue
            herokuaddr: str = m.group(0)
            print("Heroku Host is", herokuaddr)
            m = re.search(r'https://([^\.]*)', herokuaddr)
            herokuhost = m.group(1)
            cmd = f"heroku git:remote -a {herokuhost}"
            try:
                result = subprocess.run(cmd.split())
                if result.returncode:
                    print(result.stderr)
                    return result.returncode
            except FileNotFoundError as e:
                print(e)

            cmd = "git push heroku main"  # Heroku wants to build from main
            try:
                result = subprocess.run(cmd.split())
                if result.returncode:
                    print(result.stderr)
                    return result.returncode
            except FileNotFoundError as e:
                print(e)

            try:
                result = requests.get(herokuaddr)  # Initialize ntlk issue
                print(result)
                if result.ok:
                    print(result.text.find('ntlk'))
                    m = re.search("ntlk", result.text)
            except FileNotFoundError as e:
                print(e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    herokuize('create.log')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/