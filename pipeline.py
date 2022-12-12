import keys
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
import pandas as pd
from gspread_pandas import Spread, Client, conf

app_id = keys.app_id
app_secret = keys.app_secret
access_token = keys.access_token
FacebookAdsApi.init(app_id, app_secret, access_token)
my_account = AdAccount('act_' + str(keys.my_account_id))
campaigns = my_account.get_campaigns()


campaign = Campaign(keys.campaign_id)
params = {
    'date_preset': 'yesterday',
    'fields': ['campaign_name', 'ad_name', 'impressions', 'inline_link_clicks', 'spend']}

response = campaign.get_insights(params=params)

for i in response:
    df = pd.DataFrame({})
    for col in i:
        df1 = pd.DataFrame({col: [i[col]]})
        df = pd.concat([df, df1], axis=1, sort=True)
df.style

c = conf.get_config("credentials",
                    "google_secret.json")

spread = Spread("Ge_Report", config=c)
spread.df_to_sheet(
    df, index=False, sheet="report", start='A1', replace=True)
