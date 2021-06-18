from bs4 import BeautifulSoup
from selenium import webdriver
import re
import os 
from os import sep

import numpy as np
import pandas as pd
import time
import random

from datetime import datetime

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("window-size=1280,800")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")


######################################################################################################


'''Best Seller Rank lists to be scraped'''

url_list = ['https://www.amazon.co.uk/Best-Sellers-Toys-Games/zgbs/kids/ref=zg_bs_pg_1?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/Best-Sellers-Toys-Games/zgbs/kids/ref=zg_bs_pg_2?_encoding=UTF8&pg=2',
            'https://www.amazon.co.uk/Best-Sellers-Sports-Outdoors/zgbs/sports/ref=zg_bs_pg_1?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/Best-Sellers-Sports-Outdoors/zgbs/sports/ref=zg_bs_pg_2?_encoding=UTF8&pg=2',
            'https://www.amazon.co.uk/Best-Sellers-Garden-Outdoors/zgbs/outdoors/ref=zg_bs_pg_2?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/Best-Sellers-Garden-Outdoors/zgbs/outdoors/ref=zg_bs_pg_1?_encoding=UTF8&pg=2',
            'https://www.amazon.co.uk/Best-Sellers-Office-Products/zgbs/officeproduct/ref=zg_bs_pg_2?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/Best-Sellers-Office-Products/zgbs/officeproduct/ref=zg_bs_pg_1?_encoding=UTF8&pg=2',
            'https://www.amazon.co.uk/Best-Sellers-Amazon-Launchpad/zgbs/boost/ref=zg_bs_pg_2?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/Best-Sellers-Amazon-Launchpad/zgbs/boost/ref=zg_bs_pg_1?_encoding=UTF8&pg=2',
            'https://www.amazon.co.uk/Best-Sellers-Car-Motorbike/zgbs/automotive/ref=zg_bs_pg_2?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/Best-Sellers-Car-Motorbike/zgbs/automotive/ref=zg_bs_pg_2?_encoding=UTF8&pg=2',
            'https://www.amazon.co.uk/Best-Sellers-Baby/zgbs/baby/ref=zg_bs_pg_2?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/Best-Sellers-Baby/zgbs/baby/ref=zg_bs_pg_1?_encoding=UTF8&pg=2',
            'https://www.amazon.co.uk/Best-Sellers-Beauty/zgbs/beauty/ref=zg_bs_pg_2?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/Best-Sellers-Beauty/zgbs/beauty/ref=zg_bs_pg_1?_encoding=UTF8&pg=2',
            'https://www.amazon.co.uk/Best-Sellers-Computers-Accessories/zgbs/computers/ref=zg_bs_pg_2?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/Best-Sellers-Computers-Accessories/zgbs/computers/ref=zg_bs_pg_1?_encoding=UTF8&pg=2',
            'https://www.amazon.co.uk/Best-Sellers-DIY-Tools/zgbs/diy/ref=zg_bs_pg_2?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/Best-Sellers-DIY-Tools/zgbs/diy/ref=zg_bs_pg_1?_encoding=UTF8&pg=2',
            'https://www.amazon.co.uk/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_pg_2?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_pg_1?_encoding=UTF8&pg=2',
            'https://www.amazon.co.uk/Best-Sellers-Grocery/zgbs/grocery/ref=zg_bs_pg_2?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/Best-Sellers-Grocery/zgbs/grocery/ref=zg_bs_pg_1?_encoding=UTF8&pg=2',
            'https://www.amazon.co.uk/Best-Sellers-Health-Personal-Care/zgbs/drugstore/ref=zg_bs_pg_2?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/Best-Sellers-Health-Personal-Care/zgbs/drugstore/ref=zg_bs_pg_1?_encoding=UTF8&pg=2',
            'https://www.amazon.co.uk/Best-Sellers-Kitchen-Home/zgbs/kitchen/ref=zg_bs_pg_2?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/Best-Sellers-Kitchen-Home/zgbs/kitchen/ref=zg_bs_pg_1?_encoding=UTF8&pg=2',
            'https://www.amazon.co.uk/Best-Sellers-Jewellery/zgbs/jewelry/ref=zg_bs_pg_2?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/Best-Sellers-Jewellery/zgbs/jewelry/ref=zg_bs_pg_1?_encoding=UTF8&pg=2',
            'https://www.amazon.co.uk/Best-Sellers-Large-Appliances/zgbs/appliances/ref=zg_bs_pg_2?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/Best-Sellers-Large-Appliances/zgbs/appliances/ref=zg_bs_pg_1?_encoding=UTF8&pg=2',
            'https://www.amazon.co.uk/Best-Sellers-Lighting/zgbs/lighting/ref=zg_bs_pg_2?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/Best-Sellers-Lighting/zgbs/lighting/ref=zg_bs_pg_1?_encoding=UTF8&pg=2',
            'https://www.amazon.co.uk/Best-Sellers-Musical-Instruments/zgbs/musical-instruments/ref=zg_bs_pg_2?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/Best-Sellers-Musical-Instruments/zgbs/musical-instruments/ref=zg_bs_pg_1?_encoding=UTF8&pg=2',
            'https://www.amazon.co.uk/Best-Sellers-Pet-Supplies/zgbs/pet-supplies/ref=zg_bs_pg_2?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/Best-Sellers-Pet-Supplies/zgbs/pet-supplies/ref=zg_bs_pg_1?_encoding=UTF8&pg=2',
            'https://www.amazon.co.uk/Best-Sellers-Watches/zgbs/watch/ref=zg_bs_pg_2?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/Best-Sellers-Watches/zgbs/watch/ref=zg_bs_pg_1?_encoding=UTF8&pg=2']


######################################################################################################


'''Extract the Best Seller Rank list'''

def extract_record(item):
    '''This function extracts the description, url, bsr, category and timestamp of a product'''
    
    # Extracting Description, URL, and Best Seller Rank
    try:
        description = item.a.text.strip()
        url = 'https://www.amazon.co.uk' + item.a.get('href')
        best_seller_rank = item.div.span.span.text
    except:
        description = np.nan
        url = np.nan
        best_seller_rank = np.nan
    
    # Extracting Product Category from URL
    try:
        url_string = url.split('/')[6]
        regular = re.compile("[a-z]{4,}")
        category = regular.findall(url_string)
    except:
        category = np.nan

    # Adding timestamp to Product
    timestamp = datetime.now().strftime("%s")
    
    return timestamp, category, description, url, best_seller_rank


######################################################################################################


'''Extract information from every single product on the Best Seller Rank list
and their respecitve recommended products'''

def get_fbt_parent(item):

    '''This function extracts the body of the frequently bought together recommendations
    for a given focal product'''

    fbt_body = item.find_all('ul',{'class':'a-unordered-list a-nostyle a-vertical'})
    fbt_parent = fbt_body[0].find_all('li')
    return fbt_parent
    
def get_fbt_description(fbt):

    '''This function extracts the product description of a recommended product from the
    fbt parent'''

    try:
        fbt_description = fbt.a.text
    except:
        fbt_description = np.nan
    return fbt_description
    
def get_fbt_url(fbt):

    '''This function extracts the url of the recommended product from the fbt parent'''

    try:
        fbt_url = 'https://www.amazon.co.uk' + fbt.a.get('href')
    except:
        fbt_url = np.nan
    return fbt_url
    
def get_seller_status(fbt):

    '''This function extracts the seller status of a recommended producr from the
    fbt parent'''

    try:
        fbt = fbt.text.split('.')
        for status in fbt:
            if 'sent' in status.lower():
                fbt_seller_status = status
                break
            elif 'sold' in status.lower():
                fbt_seller_status = status
                break
            else:
                fbt_seller_status = 'unknown'
    except:
        fbt_seller_status = np.nan
    return fbt_seller_status

def get_asin(fbt_url):

    '''This function etract the product identification number for focal and recommended
    products from the fbt parent'''

    split = str(fbt_url).split('/')
    for i in split:
        if i.isalnum():
            if len(i) == 10:
                fbt_asin = i
                break
            else:
                fbt_asin = 'unknown'
        else:
            fbt_asin = 'unknown'
    return fbt_asin

def product_info(item,page):   

    '''This function initiates information extraction for focal and recommended
    products from a products main html-parsed body and focal product url'''

    # try to get the fbt parent body, if such body exists, i.e., if the product
    # features frequently bought together recommendations
    try:
        fbt_parent = get_fbt_parent(item)
    except:
        return "No Parent", "No Parent", "No Parent", "No Parent", "No Parent", "No Parent", "No Parent", "No Parent", "No Parent", "No Parent", "No Parent", "No Parent", "No Parent"
    
    # extracting information about focal product
    fbt_1 = fbt_parent[0]
    fbt1_asin = get_asin(page)
    fbt1_seller_status = get_seller_status(fbt_1)
        
    # extracting information about first fbt recommended product
    fbt_2 = fbt_parent[1]
    fbt2_description = get_fbt_description(fbt_2)
    fbt2_url = get_fbt_url(fbt_2)
    fbt2_asin = get_asin(fbt2_url)    
    fbt2_seller_status = get_seller_status(fbt_2)
    
    # checking whether a second fbt recommended product exists
    try:
        fbt_3 = fbt_parent[2]
    except:
        return fbt_1, fbt1_asin, fbt1_seller_status, fbt_2, fbt2_description, fbt2_url, fbt2_asin, fbt2_seller_status, "No FBT_3", "No FBT_3", "No FBT_3", "No FBT_3", "No FBT_3"
        
    # extracting ifnormation on second fbt product
    fbt3_description = get_fbt_description(fbt_3)
    fbt3_url = get_fbt_url(fbt_3)
    fbt3_asin = get_asin(fbt3_url)
    fbt3_seller_status = get_seller_status(fbt_3)
    
    return fbt_1, fbt1_asin, fbt1_seller_status, fbt_2, fbt2_description, fbt2_url, fbt2_asin, fbt2_seller_status, fbt_3, fbt3_description, fbt3_url, fbt3_asin, fbt3_seller_status

def get_bsr_1(item):

    '''This function extracts the bsr for the first recommended product'''

    bsr = item.find_all('div', {'id':'productDetails_db_sections'})[0]
    return bsr

def get_bsr_2(item):

    '''This function extracts the bsr for the second recommended product'''

    bsr = item.find_all('div', {'id':'detailBulletsWrapper_feature_div'})[0]
    return bsr

def get_bsr(item):

    '''This function initiates the bsr extraction for the fbt recommended product'''

    try:
        try:
            bsr = get_bsr_1(item)
        except:
            bsr = get_bsr_2(item)
    except:
        return "No BSR"
    
    return bsr


######################################################################################################


"""The below function generate dataframes of product urls for bsr scraping"""

def generate_bsr_url_df(final_df):
    frames = [final_df[['fbt1_url','fbt1_asin','fbt1_bsr']],
              final_df[['fbt2_url','fbt2_asin','fbt2_bsr']],
              final_df[['fbt3_url','fbt3_asin','fbt3_bsr']]]
    
    for i in frames:
        i.columns = ['fbt_url','fbt_asin','fbt_bsr']

    temp_bsr_url_df = pd.concat(frames,axis=0)
    temp_bsr_url_df = temp_bsr_url_df.drop_duplicates(subset = "fbt_asin", keep='first', ignore_index=True)
    
    return temp_bsr_url_df

def find_bsr_url_subset(full_bsr_url_df, temp_bsr_url_df):
    frames = [full_bsr_url_df[['fbt_url','fbt_asin']], 
              temp_bsr_url_df[['fbt_url','fbt_asin']]]
    
    for i in frames:
        i.columns = ['fbt_url','fbt_asin']
        
    temp_df = pd.concat(frames,axis=0)
    add_bsr_url_df = temp_df.drop_duplicates(subset = "fbt_asin", keep=False, ignore_index=True)
        
    return add_bsr_url_df


######################################################################################################


"""Run main program routine"""

def scrape(url_list):
    
    timestamp = datetime.now().strftime("%s")
    save_path = "{}Users{}mads{}Desktop{}SDS{}GitHub{}Thesis{}".format(sep,sep,sep,sep,sep,sep,sep)
        
    # scraping the best seller rank list
    list_list = []
    for num,page in enumerate(url_list):
        driver.get(page)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('li', {'class':'zg-item-immersion'})
    
        for item in results:
            list_list.append(extract_record(item)) 
            
        time.sleep(random.uniform(2,5))

    list_df = pd.DataFrame(list_list, columns=["timestamp", "category", "fbt1_description", "fbt1_url", "fbt1_bsr"])
    del list_list

    list_name = "list_df.csv"
    list_completeName = os.path.join(save_path, list_name)
    list_df.to_csv(list_completeName,index=False)

    t1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('BSR List Scraped ' + t1)


    
    # scraping the focal products
    url_product_list = list_df['fbt1_url'].to_list()
    
    products = []
    count = 0
    for num, page in enumerate(url_product_list):
        try:
            driver.get(page)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            results = soup.find_all('div', {'role':'main'})
            item = results[0]
        except:
            products.append(tuple(["No FBT", "No FBT", "No FBT", "No FBT", "No FBT", "No FBT", "No FBT", "No FBT", "No FBT", "No FBT", "No FBT", "No FBT", "No FBT"]))
            t_temp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            count += 1
            print(f"Product URL not reached. Number of product not reached: {count} at time {t_temp}")
            
        product = product_info(item, page)
        product = product + (page,)
            
        products.append(product)

        if num % 100 == 0:
            time.sleep(random.uniform(50,100))
        
        time.sleep(random.uniform(2,5))
  
    product_df = pd.DataFrame(products, columns=['fbt_1', 'fbt1_asin', 'fbt1_seller_status', 
                                                'fbt_2', 'fbt2_description', 'fbt2_url', 'fbt2_asin', 'fbt2_seller_status',
                                                'fbt_3', 'fbt3_description', 'fbt3_url', 'fbt3_asin', 'fbt3_seller_status',
                                                'fbt1_url'])
    
    del products
    del url_product_list
                
    t2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Focal Products BSR Scraped " + t2)
        


    # scraping the recommended products
    url_recommended_list_1 = [np.nan] * len(product_df)
    for i in range(len(product_df)):
        try:
            url_recommended_list_1[i] = product_df['fbt2_url'][i]
        except:
            url_recommended_list_1[i] = 'No FBT'
    
    url_recommended_list_2 = [np.nan] * len(product_df)
    for i in range(len(product_df)):
        try:
            url_recommended_list_2[i] = product_df['fbt3_url'][i]
        except:
            url_recommended_list_2[i] = 'No FBT3'
        
    bsr_1 = []
    count = 0
    for num, page in enumerate(url_recommended_list_1):
        if page == 'No FBT':
            bsr_1.append(page)
        else:
            try:
                driver.get(page)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                results = soup.find_all('div', {'role':'main'})
                item = results[0]
                bsr_1.append(get_bsr(item))
            except:
                bsr_1.append(page)
                t_temp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                count += 1
                print(f"Product URL not reached. Number of product not reached: {count} at time {t_temp}")


        if num % 100 == 0:
            time.sleep(random.uniform(50,100))
        
        time.sleep(random.uniform(2,5))
    
    del url_recommended_list_1

    bsr_2 = []
    count = 0
    for num,page in enumerate(url_recommended_list_2):
        if page == 'No FBT3':
            bsr_2.append(page)
        else:
            try:
                driver.get(page)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                results = soup.find_all('div', {'role':'main'})
                item = results[0]
                bsr_2.append(get_bsr(item))
            except:
                bsr_2.append(page)
                t_temp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                count += 1
                print(f"Product URL not reached. Number of product not reached: {count} at time {t_temp}")

        if num % 100 == 0:
            time.sleep(random.uniform(50,100))
        
        time.sleep(random.uniform(1,4))
    
    del url_recommended_list_2
     
    t3 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('Recommended Products BSR Scraped ' + t3)
                

    
    # creating final product dataframe to be saved
    product_df = pd.concat([product_df,pd.Series(bsr_1),pd.Series(bsr_2)],axis=1).rename(columns={0:"fbt2_bsr",1:"fbt3_bsr"})
    
    del bsr_1
    del bsr_2

    final_df = pd.merge(list_df, product_df, how="inner", on="fbt1_url")
    final_df = final_df[final_df['fbt1_bsr'].notna()]
    products_name = "{}_products_full.csv".format(timestamp)
    products_completeName = os.path.join(save_path, products_name)

    del list_df
    del product_df

    final_df.to_csv(products_completeName, index=False)
    


    # creating bsr_url_df
    full_bsr_url_df = pd.read_csv(f"{sep}Users{sep}mads{sep}Desktop{sep}SDS{sep}GitHub{sep}Thesis{sep}bsr_url_total.csv") # dataframe that will have all url and asin
    temp_bsr_url_df = generate_bsr_url_df(final_df)
    del final_df
    


    # Creating subset of products for which best seller rank needs to be scraped
    add_bsr_url_df = find_bsr_url_subset(full_bsr_url_df, temp_bsr_url_df)
    add_bsr_url_df = add_bsr_url_df[add_bsr_url_df['fbt_asin'] != 'No FBT_3']
    add_bsr_url_df = add_bsr_url_df[add_bsr_url_df['fbt_asin'] != 'No FBT']
        
    add_rank = []
    count = 0
    for num,i in enumerate(add_bsr_url_df['fbt_url'].to_list()):
        try:
            driver.get(i)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            results = soup.find_all('div', {'role':'main'})
            item = results[0]
            add_rank.append(get_bsr(item))
        except:
            add_rank.append('No BSR')
            t_temp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            count += 1
            print(f"Product URL not reached. Number of product not reached: {count} at time {t_temp}")

        if num % 100 == 0:
            time.sleep(random.uniform(50,100))
        
        time.sleep(random.uniform(2,5))

    t4 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('Additional BSR Scraped ' + t4)
        
    add_bsr_url_df['fbt_bsr'] = add_rank
    del add_rank


        
    # Adding add_bsr_url_df and bsr_url_df together
    bsr_frames = [temp_bsr_url_df, add_bsr_url_df]
    bsr_url_df = pd.concat(bsr_frames,axis=0)
    bsr_url_df = bsr_url_df[bsr_url_df['fbt_asin'] != 'No FBT_3']
    bsr_url_df = bsr_url_df[bsr_url_df['fbt_asin'] != 'No FBT']

    bsr_name = "{}_bsr.csv".format(timestamp)
    bsr_completeName = os.path.join(save_path, bsr_name)
    bsr_url_df.to_csv(bsr_completeName,index=False)

    del add_bsr_url_df
    del temp_bsr_url_df
    


    # Updating full_bsr_url_df
    full_bsr_url_df = bsr_url_df[['fbt_url','fbt_asin']]
    full_url_name = "bsr_url_total.csv"
    full_url_completeName = os.path.join(save_path, full_url_name)
    full_bsr_url_df.to_csv(full_url_completeName,index=False)

    del bsr_url_df
    del full_bsr_url_df



if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="/Users/mads/Downloads/chromedriver", options=chrome_options)
    while True:
        t5 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print('Starting Scraper ' + t5)
        scrape(url_list)
        t6 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print('Sleeping ' + t6)
        time.sleep(random.uniform(1000,4000))