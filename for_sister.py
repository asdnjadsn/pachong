import pandas as pd
import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
urls = []
for index in range(107000000, 107267472):
    url = "http://dbpub.cnki.net/grid2008/dbpub/detail.aspx?dbcode=SCPD&dbname=SCPD2017&filename=CN" + str(
        index) + "A&uid=WEEvREcwSlJHSldRa1FhdkJkcGp4dXFrckp2ME9rdHYvVmNkbzA5YVFHRT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!"
    urls.append(url)

hold = []
try:
    count = 0
    for url in urls:
        count += 1
        if count % 5 == 0:
            pd.DataFrame(hold).to_csv("../data/mysister_dachang.csv", index=False, encoding="utf-8")
        try:
            r = http.request('GET', url)
            content = r.data.decode("utf-8")
            if content != None:
                dict = {}
                soup = BeautifulSoup(content, "html.parser")
                title = soup.find("title").get_text()
                dict["title"] = title
                table = soup.find("table", attrs={"id": "box"})
                trs = table.findAll("tr")
                for tr in trs:
                    tds = tr.findAll("td")
                    if len(tds) < 5 and len(tds) > 1:
                        dict[tds[0].get_text()] = tds[1].get_text()
                        if len(tds) > 2:
                            dict[tds[2].get_text()] = tds[3].get_text()
                hold.append(dict)
        except:
            pass
except:
    pd.DataFrame(hold).to_csv("../data/mysister_dachang.csv", index=False, encoding="utf-8")

pd.DataFrame(hold).to_csv("../data/mysister_dachang.csv", index=False, encoding="utf-8")