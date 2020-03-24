from covid import Covid

cv = Covid()
#print(cv.get_data())

countries = cv.list_countries()
print(countries)
#Covid_Id_data = cv.get_status_by_country_name('india')
#print(Covid_Id_data['id'])
