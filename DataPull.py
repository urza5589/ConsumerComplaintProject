import requests


# http://www.consumerfinance.gov/complaintdatabase/technical-documentation/#more_options
# View IDs
# ID	CATEGORY
# s6ew-h6mp	Consumer complaints (all categories)
# t9fg-cqmi	Bank accounts or services
# 7zpz-7ury	Credit cards
# xa48-juie	Credit reporting
# ckyu-ku28	Debt collection
# uha4-cwwn	Money transfers
# g5qz-smft	Mortgages
# b239-tvpx	Other financial services
# 6hp8-hzag	Payday loans
# 6yuf-367p	Prepaid cards
# eew7-9yf2	Student loans
# wfbn-zkat	Vehicle or other consumer loans

view_param = 's6ew-h6mp'
type_param = 'json'
row_param = 'rows'
request_url = 'http://data.consumerfinance.gov/api/views/' + view_param + '/' + row_param + '.' + type_param
r = requests.get(request_url)
print(r.status_code)
r.json()changedchangedf
print(r.json)