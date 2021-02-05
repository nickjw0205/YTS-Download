# YTS-Download
 Download youtube search result of video!

 ## Chrome driver

 before use this code, you have to download chrome driver.
 <br>
 you can download at [here](https://chromedriver.chromium.org/downloads)

 ## How to download and use
 ### Clone git
 ```shell
 git clone https://github.com/nickjw0205/YTS-Download
 cd YTS-Download
 ```

 ### Set path of chromedriver
 before run code you have to set path.<br>
 set path in search_youtube function to location of chromedriver you downloaded above.

 ```{.python}
 # open chrome tab and scroll it to load videos
 def search_youtube(search):
     # location of chrome driver
     path = 'path'
     driver = webdriver.Chrome(executable_path=path)
     delay = 3
     driver.implicitly_wait(delay)
     driver.get(search)
     body = driver.find_element_by_tag_name('body')
     num_of_pagedowns = 10
 ```

### Run code
Now, you can download videos
```shell
python YTS_download.py
```
then you can see "search word : "
```shell
>>> python YTS_Download.py
>>> search word: ...
```
Enter what you want to download<br>
Then, the chrome tab appeared and start scrolling<br>
when scrolling ends, download will be started.
![](https://github.com/nickjw0205/YTS-Download/blob/main/result.gif){: width="50%" height="50%"}{: .center}
