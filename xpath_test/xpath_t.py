from lxml import etree

tree = etree.parse('a.html')
# li_lst = tree.xpath("/html/body/ol/li/a[@href='feiji4'][@name='fj5']/text()")
li_lst = tree.xpath("/html/body/ol/li")

for li in li_lst:
    # ./是当前目录（相对查找）
    res = li.xpath('./a/text()')
    print(res)
    res2 = li.xpath('./a/@href')
    print(res2)
    res3 = tree.xpath("/html/body/div[1]/text()")
    print("res3: ", res3)
