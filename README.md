# YTS-Download
 Download youtube search result of video!

 ## Chrome driver

 before use this code, you have to download chrome driver.
 <br>
 you can download at [here](https://chromedriver.chromium.org/downloads)

 ## Download
 ### Clone git
 ```shell
 >>> git clone https://github.com/nickjw0205/YTS-Download
 >>> cd YTS-Download
 ```
 ## Setting
 ### Necessary Package and folder
 ```shell
 mkdir images
 mkdir videos
 pip install selenium
 pip install beautifulsoup4
 pip install bs4
 pip install youtube_dl
 pip install opencv-python
 ```

 ### Set path of chromedriver
 before run code you have to set path.<br>
 set path in search_youtube function to location of chromedriver you downloaded above.

 ```python
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
## Use
### Run YTS_Download.py
Now, you can download videos
```shell
>>> python YTS_download.py
```
then you can see "search word : "
```shell
>>> python YTS_Download.py
>>> search word: ...
```
Enter what you want to download.<br>
Then, the chrome tab appeared and start scrolling.<br>
When scrolling ends, download will be started.<br>
The videos will be stored in videos folder.
### Run Frame_Capture.py
After downloading videos, you can capture video frame by frame.
```shell
>>> python Frame_Capture.py
```

Also you can designate frame rate.
```python
# capture video by frame_rate frame
if(int(vidcap.get(1)) % frame_rate == 0):
    print('Saved frame number : ' + str(int(vidcap.get(1))))
    cv2.imwrite("images/frame%d.jpg" % count, image)
    print('Saved frame%d.jpg' % count)
    count += 1
```
Then captured images will be stored in images folder.
