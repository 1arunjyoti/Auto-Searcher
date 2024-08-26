import webbrowser
import time
import pyautogui
import random
import requests
import subprocess

""" pyautogui.click(682, 746)
time.sleep(1) """

def autoSearch():
    response= requests.get(
        'https://www.mit.edu/~ecprice/wordlist.10000', timeout=10
    )
    
    random_words= response.content.decode('utf-8')
    words= random_words.splitlines()
    random_word= random.choice(words)

    url= ("https://www.bing.com/search?q=" + random_word)

    # webbrowser.open(url)

    # Use subprocess to directly open Microsoft Edge with the URL
    subprocess.Popen([r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe","--new-tab", url])

    random_value= random.randint(3, 12)
    time.sleep(random_value)

    pyautogui.hotkey('ctrl', 'w')


start= time.time()

num=int(input("Enter the number of times you want to search: "))
for i in range(num):
    autoSearch()
    print ("Total Searches done: ", i)

end= time.time()
print ("Total Time taken: ", round(end-start))