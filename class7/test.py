from selenium import webdriver
import pandas as pd
driver = webdriver.Chrome('./chromedriver')

# https://www.youtube.com/channel/UCuDWqzSSHgHkD0zBwrIXSNQ
url =  'https://www.youtube.com/channel/UCuDWqzSSHgHkD0zBwrIXSNQ' 
driver.get(url)
videos = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')


for video in videos:
    title = video.find_element_by_xpath('//*[@id="video-title"]')

# # //*[@id="video-title"]
# video_list = []
# for video in videos: 
#     title = video.find_element_by_xpath('.//*[@="video-title"').text
#     # views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
#     # when = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text
#     video_item={
#             'title':title,
#             # 'views': views,
#             # 'posted':when
#             }
#     video_list.append(video_item)

# df = pd.DataFrame(video_list)
# print(df)


