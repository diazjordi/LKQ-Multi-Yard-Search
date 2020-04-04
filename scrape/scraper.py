import time
from selenium import webdriver
from data.lkqyard import LKQYard
from data.vehicleresult import VehicleResult

driver = webdriver.Chrome("C:\\Users\\death\\Desktop\\Python\\chromedriver_win32\\chromedriver.exe")
yards = []
search_results = []

class Scraper:

    # find all yards in radius
    def get_yards_in_radius(self, zip, search_radius):
        find_stores_url = "https://www.lkqpickyourpart.com/locations/?zip=" + str(
            zip) + "&range=" + search_radius.__str__()
        driver.get(find_stores_url)
        store_results = driver.find_elements_by_class_name('pypfys_store')

        # create LKQYard objects to hold yard data
        for i in range(len(store_results)):
            # find store name
            name = store_results[i].find_element_by_class_name('pypfys_storeName').text
            # print("Store Name: " + name)
            # find store address
            address_divs = store_results[i].find_element_by_class_name('pypfys_storeInfo').find_elements_by_tag_name(
                'div')
            address = address_divs[0].text + ' ' + address_divs[1].text
            # print("Store Address: " + address)
            # find store distance
            distance = store_results[i].find_element_by_class_name('pypfys_storeDistance').find_element_by_tag_name(
                'b').text.strip(" mi")
            # print("Distance: " + distance)
            # find store homepage link
            homepage = store_results[i].find_element_by_class_name('pypfys_links').find_element_by_css_selector(
                'a').get_attribute('href')
            # print("Homepage: " + homepage)
            # find store vehicle inventory link
            vehicle_inventory = homepage + 'recents/'
            # print(inventory)

            # create LKQYard object
            yard = LKQYard(name, address, distance, homepage, vehicle_inventory)
            yard.yard_info()
            yards.append(yard)

    # search all yards in radius
    def search_yards_in_radius(self, yards_in_radius, search_term):
        # loop through inventory of yards
        for yard in yards_in_radius:
            print(yard.vehicle_inventory)
            driver.get(yard.vehicle_inventory)
            # search inventory of each yard, store results
            searchbox = driver.find_element_by_class_name('pyp_input')# Find the search box
            searchbox.clear()
            searchbox.send_keys(search_term)
            time.sleep(2)
            vehicle_results = driver.find_elements_by_class_name('pypvi_resultRow')
            print(len(vehicle_results))
            for result in vehicle_results:
                print('in search results')
                #image = result.find_element_by_class_name('pypvi_image')
                #make = result.find_element_by_class_name('pypvi_make')
                model = result.find_element_by_class_name('pypvi_model').text
                year = result.find_element_by_class_name('pypvi_year').text
                date = result.find_element_by_class_name('pypvi_date').text
                #color = result.find_element_by_class_name('')
                #section = result.find_element_by_class_name('pypvi_notes').text
                #row = result.find_element_by_class_name('pypvi_notes').text
                #space = result.find_element_by_class_name('pypvi_notes').text
                vin = result.find_element_by_class_name('pypvi_notesVin').text
                #search_results.append(VehicleResult(image, make, model, year, date, color, section, row, space, vin))
                print(model)
                print(year)
                print(date)
                print(vin)

    #

    # def search_yards_in_radius(self):
