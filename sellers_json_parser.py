import requests
import pandas as pd

urls = ["https://www.inmobi.com/sellers.json","https://cdn.pubmatic.com/sellers/data/sellers.json"]

sellers_json_domain_list = []
for url in urls:
	print("inside")
	r = requests.get(url)
	print("Fetched")
	print(r)
	sellers_json = r.json()
	for i in range(0,len(sellers_json["sellers"])):
		try:
			sellers_json_domain_list.append([url,str(sellers_json["sellers"][i]['seller_id']),str(sellers_json["sellers"][i]['name']),str(sellers_json["sellers"][i]['domain']),str(sellers_json["sellers"][i]['seller_type'])])
		except:
			continue
sellers_json_df = pd.DataFrame(sellers_json_domain_list,columns=["Demand URL","Seller ID","Publisher Name","Domain","Seller Type"])
print(sellers_json_df.head())

sellers_json_df.to_excel("sellers_json_report.xlsx",index=False)