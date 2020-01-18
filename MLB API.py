{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Import dependencies\n",
    "import requests\n",
    "import pandas as pd\n",
    "#first URL for API call\n",
    "url = \"http://lookup-service-prod.mlb.com/json/named.team_all_season.bam?sport_code=\\\n",
    "'mlb'&all_star_sw='N'&sort_order=name_asc&season='2017'\"\n",
    "#Make the API call\n",
    "try:\n",
    "    result = requests.get(url).json()\n",
    "    result2 = result['team_all_season']['queryResults']['row']\n",
    "    baseball_response.append(result2)\n",
    "except KeyError:\n",
    "    pass\n",
    "#Keys for the JSON navigation\n",
    "# ['phone_number', 'venue_name', 'franchise_code', 'all_star_sw', 'sport_code', 'address_city', \n",
    "#  'city', 'name_display_full', 'spring_league_abbrev', 'time_zone_alt', 'sport_id', 'venue_id', \n",
    "#  'mlb_org_id', 'time_zone_generic', 'mlb_org', 'last_year_of_play', 'league_full', 'home_opener_time', \n",
    "#  'address_province', 'league_id', 'name_abbrev', 'bis_team_code', 'league', 'spring_league', 'base_url', \n",
    "#  'address_zip', 'sport_code_display', 'mlb_org_short', 'time_zone', 'address_line1', 'mlb_org_brief',\n",
    "#  'address_line2', 'season', 'address_line3', 'division_abbrev', 'name_display_short', 'team_id', 'active_sw',\n",
    "#  'address_intl', 'state', 'address_country', 'mlb_org_abbrev', 'division', 'team_code', 'name', 'website_url', \n",
    "#  'sport_code_name', 'first_year_of_play', 'league_abbrev', 'name_display_long', 'store_url', 'time_zone_text', \n",
    "#  'name_short', 'home_opener', 'address_state', 'division_full', 'time_zone_num', 'spring_league_full',\n",
    "#  'address', 'name_display_brief', 'file_code', 'division_id', 'spring_league_id', 'venue_short'\n",
    "\n",
    "#Create a Pandas Dataframe and add the year \n",
    "df1 = pd.DataFrame(result2, columns = ['venue_name','city','name_display_long'])\n",
    "df1[\"year\"]=\"2017\"\n",
    "df1\n",
    "\n",
    "#Create the second URL for 2016\n",
    "url2 = \"http://lookup-service-prod.mlb.com/json/named.team_all_season.bam?sport_code='mlb'&all_star_sw='N'\\\n",
    "&sort_order=name_asc&season='2016'\"\n",
    "try:\n",
    "    result = requests.get(url2).json()\n",
    "    result3 = result['team_all_season']['queryResults']['row']\n",
    "    baseball_response.append(result3)\n",
    "except KeyError:\n",
    "    pass\n",
    "#Create the datafram for 2016\n",
    "df2= pd.DataFrame(result3, columns = ['venue_name','city','name_display_long'])\n",
    "df2['year']=\"2016\"\n",
    "df2\n",
    "#create CSVs\n",
    "df1.to_csv(\"mlb2017.csv\", index=False, header=True)\n",
    "df2.to_csv(\"mlb2016.csv\", index=False, header=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:PythonData] *",
   "language": "python",
   "name": "conda-env-PythonData-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
