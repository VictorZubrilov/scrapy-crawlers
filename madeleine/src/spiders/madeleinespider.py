# -*- coding: utf-8 -*-
from scrapy.contrib.loader.processor import TakeFirst, MapCompose, Join
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import ItemLoader
from scrapy.http.cookies import CookieJar
from scrapy.http import FormRequest, Request
from scrapy import Spider
from src.items import ProductItem
import time, re, json, os
import smtplib
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from email.MIMEText import MIMEText
import collections

class MadeleineSpider(Spider):
    name = "madeleinespider"

    check_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self):
        dispatcher.connect(self.spider_closed, signals.spider_closed)
    def spider_closed(self, spider):
        if not self.result_check:
            me = 'mmadeleinee2015@gmail.com'
            you = 'admin@catalogi.ru'
            text = u'MADELEINE_SPIDER\nНе все данные собираются с сайта (есть пустые поля), см. log.txt на сервере'
            subj = 'MADELEINE_SPIDER'

            # SMTP-сервер
            server = "smtp.gmail.com"
            port = 25
            user_name = "mmadeleinee2015@gmail.com"
            user_passwd = "madeleine78"

            # формирование сообщения
            msg = MIMEText(text, "", "utf-8")
            msg['Subject'] = subj
            msg['From'] = me
            msg['To'] = you

            # отправка
            s = smtplib.SMTP(server, port)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(user_name, user_passwd)
            s.sendmail(me, you, msg.as_string())
            s.quit()

    def start_requests(self):
        l = [Request(url="http://www.madeleine.de/mode/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/schuhe-accessoires/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/mode/abendmode/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/mode/bademode/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/mode/blazer/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/mode/blusen/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/mode/dessous/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/mode/freizeit-homewear/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/mode/hosen/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/mode/hosenanzuege/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/mode/jacken-maentel/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/mode/kleider/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/mode/kostueme/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/mode/nachtwaesche/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/mode/overalls/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/mode/roecke/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/mode/shirts-tops/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/mode/strickmode/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/schuhe-accessoires/schuhe/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/schuhe-accessoires/accessoires/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/schuhe-accessoires/schuhe/ballerinas/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/schuhe-accessoires/schuhe/boots/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/schuhe-accessoires/schuhe/mokassins/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/schuhe-accessoires/schuhe/pumps/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/schuhe-accessoires/schuhe/sandaletten/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/schuhe-accessoires/schuhe/stiefel-stiefeletten/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/schuhe-accessoires/schuhe/pantoletten/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/schuhe-accessoires/accessoires/guertel/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/schuhe-accessoires/accessoires/handschuhe/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/schuhe-accessoires/accessoires/muetzen-huete/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/schuhe-accessoires/accessoires/schals-tuecher/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/schuhe-accessoires/accessoires/schmuck/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/schuhe-accessoires/accessoires/sonnenbrillen/",
                                          callback=self.parse_page),
                Request(url="http://www.madeleine.de/schuhe-accessoires/accessoires/taschen/",
                                          callback=self.parse_page)]
        return l

        #test
        #product_path = "/viskose-shirt-im-layering-look-0a1025156.html"
        #product_path = "/chantelle-slip-mit-spitze-0a1027019.html"
        #item = ProductItem()
        #item["path"] = product_path

        #request = Request(url="http://www.madeleine.de" + product_path, callback=self.parse_product)
        #request.meta['item'] = item

        #yield request

    def parse_page(self, response):

        # ------products_paths------

        products_paths = response.xpath("//div[@id='articles']/div/a/@href").extract()

        for product_path in products_paths:
            item = ProductItem()
            item["path"] = product_path

            request = Request(url="http://www.madeleine.de" + product_path, callback=self.parse_product)
            request.meta['item'] = item

            yield request


        extr = LxmlLinkExtractor(allow="seite-\d+")
        links = extr.extract_links(response)

        for link in links:
            yield Request(url=link.url, callback=self.parse_page)

    def parse_product(self, response):
        item = response.meta['item']

        if response.xpath("//div[@class='soldout']"):
            return

        # ------name------

        item["masterID"] = response.xpath("substring-before(substring-after(//script[contains(text(), 'var masterId=')], 'var masterId=\"'), '\";')").extract()[0]
        item["name"] = response.xpath("string(//h1)").extract()[0]

        # ------care------

        item["care"] = ""

        careLabel_x = response.xpath("//ul[@id='careLabels']/li")
        if careLabel_x:
            careLabel = careLabel_x[0].xpath("text()").extract()[0] + ":"
            care_num = careLabel_x[0].xpath("substring-after(@class, '-')").extract()[0]
            careLabel = careLabel + "http://www.madeleine.de/img/site4/article/careicon-%s.png:" % care_num
            careLabel = careLabel + response.xpath("string(//div[contains(@class, 'carelabels')]/p[@class='info'])").extract()[0]
            item["care"] = careLabel

        # ------consist------

        consist_text = response.xpath("string(//p[@id='hardFacts'])").extract()[0]
        materials = re.findall("\d+%\s+(.+?)[,.]", consist_text)

        consist = ",".join(materials)
        consist = consist + ":%s" % consist_text
        item["consist"] = consist

        # ------description------

        item["description"] = response.xpath("string(//div[@class='content'])").extract()[0]

        # ------brand------

        item["brand"] = "Madeleine:http://pro-allegro.by/images/logo/madeleine.png"

        # ------images360 and video_url------

        item["images360"] = ""
        item["video_url"] = ""

        s360 = response.xpath("string(//script[contains(text(), '_Article360ViewUrl')])").extract()[0]
        if s360:
            m = re.search('zoompopup_fg\.php\?id=(\d+)&', s360)
            urls = ""
            if m:
                for i in range(1, 25):
                    if i < 10:
                        idx = "0%d" % i
                    else:
                        idx = "%d" % i
                    urls = urls + "http://madeleine.scoopzoom.de/img/360/%s/%s.jpg," % (m.group(1), idx)
            item["images360"] = urls[:-1]

            m = re.search('_ArticleVideoViewUrl = "(.*)"', s360)
            if m:
                item["video_url"] = m.group(1)

        # ------path_related------

        related_urls = response.xpath("//div[@id='tc-content300']/div/div/ul/li/a/@data-href").extract()
        path_related = ""
        for related_url in related_urls:
            path_related = path_related + related_url[23:] + ","

        item["path_related"] = path_related[:-1]

        # ------path_upsell------

        upsell_urls = response.xpath("//div[@id='mav2-outfit-list-ext']/div[@class='scroll']/ul/li/a/@href").extract()
        path_upsell = ""
        for upsell_url in upsell_urls:
            path_upsell = path_upsell + upsell_url + ","

        item["path_upsell"] = path_upsell[:-1]

        # ------breadcrumbs------

        google_tag_params = response.xpath("substring-before(substring-after(//script[contains(text(), 'var google_tag_params =')], '%s'), '%s')" % ("pcat: ", ", ")).extract()[0]
        breadcrumbs_list = google_tag_params[1:-1].split(",")
        breadcrumbs_list.reverse()

        breadcrumbs = ", ".join(breadcrumbs_list)
        item["breadcrumbs"] = breadcrumbs

        # ------id_supplier------

        item["id_supplier"] = "000000002"

        # ------sizes------

        sizes = ""

        productData = json.loads(response.xpath("substring-before(substring-after(//script[contains(text(), 'var productData=')], 'var productData='), ';')").extract()[0])
        kdbnrSxData = json.loads(response.xpath("substring-before(substring-after(//script[contains(text(), 'var kdbnrSxData=')], 'var kdbnrSxData='), ';')").extract()[0])
        articleData = json.loads(response.xpath("substring-before(substring-after(//script[contains(text(), 'var articleData=')], 'var articleData='), ';')").extract()[0])
        availabilityTextLookUp = json.loads(response.xpath("substring-before(substring-after(//script[contains(text(), 'var availabilityTextLookUp=')], 'var availabilityTextLookUp='), ';')").extract()[0])

        #print "!!!!!", response.body_as_unicode()

        sizes_in_tabs = []
        tabs_names = []

        sizes_cont = response.xpath("//div[@id='sizeParent']/div")

        tabs = sizes_cont.xpath("div/ul/li[contains(@id, 'tc-tab')]")

        for tab in tabs:
            if tab.xpath("span[@class='st-icon']"):
                tabs_names.append([tab.xpath("string(span[@class='st-icon'])").extract()[0], tab.xpath("string(span[@class!='st-icon'])").extract()[0]])
            else:
                tabs_names.append(["", tab.xpath("string(span)").extract()[0]])
            num_tab = tab.xpath("substring-after(@id, 'tc-tab')").extract()[0]

            sizes_x = sizes_cont.xpath("div[@id='tc-content%s']/div/div/div" % num_tab)

            sizes_names = []

            for size_x in sizes_x:
                sizes_names.append("".join(size_x.xpath("string(.)").extract()))
            sizes_in_tabs.append(sizes_names)

        for article in articleData.keys():
            sizes = sizes + "%s:" % article
            for i, tab_name in enumerate(tabs_names):
                sizes = sizes + "%s:%s::" % (tab_name[0], tab_name[1])
                for size in sizes_in_tabs[i]:
                    size_c = re.sub("[,/\s+]", "", size)
                    for size_data in articleData[article]:
                        if size_data[0] == size_c:
                            if size_data[2] == 3 or size_data[2] == 6:
                                sizes = sizes + "!%s|" % size
                            else:
                                sizes = sizes + "%s|" % size
                            sizes = sizes + "%s^" % availabilityTextLookUp["%d" % size_data[2]]
                            break
                sizes = sizes[:-1] + ";"
            sizes = sizes[:-1] + "#"

        item["sizes"] = sizes[:-1]

        # ------price and old_price------

        price = ""

        for article in productData.keys():
            for i, tab_name in enumerate(tabs_names):
                for size in sizes_in_tabs[i]:
                    size_c = re.sub("[,/\s+]", "", size)
                    if productData[article]["Sizes"].get(size_c) == None:
                        continue
                    size_data = productData[article]["Sizes"][size_c]

                    price = price + "%s:" % article
                    price = price + "%s:" % tab_name[1]
                    price = price + "%s:" % size
                    price = price + "%s:" % size_data["Price"].replace(",", ".")

                    if size_data["SalePrice"] == None:
                        price = price + "N;"
                    else:
                        price = price + "%s;" % size_data["SalePrice"].replace(",", ".")
            if not tabs_names:
                size_data = productData[article]["Sizes"]["ohne"]

                price = price + "%s:::%s:" % (article, size_data["Price"].replace(",", "."))

                if size_data["SalePrice"] == None:
                    price = price + "N;"
                else:
                    price = price + "%s;" % size_data["SalePrice"].replace(",", ".")

        item["price"] = price[:-1]

        # ------images------

        images = ""

        general_image = response.xpath("string(//meta[@property='og:image']/@content)").extract()[0]
        if general_image:
            url_l = general_image.split("_")
            url_l[1] = "0"
            url_l[2] = "0"
            url_l[3] = "0"
            url_l[4] = "0"
            general_image = "_".join(url_l)

        images = "%s;" % general_image

        imgToKdbnrsx_text = response.xpath("substring-before(substring-after(//script[contains(text(), 'var imgToKdbnrsx=')], 'var imgToKdbnrsx='), ';')").extract()[0].replace("'", "\"")

        if imgToKdbnrsx_text:
            imgToKdbnrsx = json.loads(imgToKdbnrsx_text, object_pairs_hook=collections.OrderedDict)

            for article in kdbnrSxData.keys():
                url = kdbnrSxData[article]["Url"]
                url_l = url.split("_")
                url_l[1] = "0"
                url_l[2] = "0"
                url_l[3] = "0"
                url_l[4] = "0"
                url = "_".join(url_l)
                img_id = kdbnrSxData[article]["ImageId"]

                if imgToKdbnrsx:
                    for img in imgToKdbnrsx.keys():
                        if imgToKdbnrsx[img] == article:
                            images = images + "%s:%s;" % (article, url.replace(img_id, img))
                else:
                    images = images + "%s:%s" % (article, url)

        else:
            for article in kdbnrSxData.keys():
                url = kdbnrSxData[article]["Url"]
        item["images"] = images[:-1]

        # ------colors------

        colors_groups = dict()

        for article in productData.keys():
            colors_group = productData[article]["ColorFamilyName"]
            article_color = [article, productData[article]["ColorName"], "http://a2.madcdn.net/img/cache/colors/%d.jpg" % productData[article]["ColorId"]]
            if colors_groups.get(colors_group) == None:
                colors_groups[colors_group] = []
            colors_groups[colors_group].append(article_color)

        request = Request(url="http://www.madeleine.de/suche/ihre-suche-%s/" % productData.keys()[0], callback=self.parse_themes)
        request.meta['item'] = item
        request.meta['colors_groups'] = colors_groups

        return request


    def parse_themes(self, response):
        item = response.meta['item']
        colors_groups = response.meta['colors_groups']

        themes = response.xpath("//div[@class='sf_items sf_colors'][2]/ul/li/@title").extract()

        item["themes"] = ",".join(themes)

        if colors_groups.get('varies') != None:
            colors_groups["varies_res"] = list(colors_groups["varies"])
            colors = []
            colors_x = response.xpath("//div[@class='sf_items sf_colors'][1]/ul/li")
            for color_x in colors_x:
                colors.append([color_x.xpath("@title").extract()[0], color_x.xpath("substring-after(a/@href, '=')").extract()[0]])


            color = colors.pop(0)
            request = Request(url="http://www.madeleine.de%s?cf=%s" % (item["path"], color[1]) , callback=self.find_colors)
            request.meta['item'] = item
            request.meta['colors_groups'] = colors_groups
            request.meta['cur_color'] = color[0]
            request.meta['colors'] = colors

            return request
        else:
            item["colors"] = self.make_colors(colors_groups)
            self.check_item(item)
            return item

    def find_colors(self, response):
        item = response.meta['item']
        colors_groups = response.meta['colors_groups']
        cur_color = response.meta['cur_color']
        colors = response.meta['colors']

        varies = colors_groups.get("varies")

        if not response.xpath("//body[contains(@class, 'tab-invalidlink')]"):
            #article = response.xpath("string(//span[@id='orderNo'])").extract()[0].replace(' ', '')
            img_id = response.xpath("substring-after(//img[contains(@id, 'mainImage')]/@id, '-')").extract()[0]

            kdbnrSxData = json.loads(response.xpath("substring-before(substring-after(//script[contains(text(), 'var kdbnrSxData=')], 'var kdbnrSxData='), ';')").extract()[0])

            for i, color in enumerate(varies):
                if kdbnrSxData.get(color[0])["ImageId"] == img_id:
                    col = varies[i]

                    for j, color_var in enumerate(colors_groups['varies_res']):
                        if (color_var[0] == varies[i][0]):
                            colors_groups['varies_res'].pop(j)
                    if colors_groups.get(cur_color) == None:
                        colors_groups[cur_color] = []
                    colors_groups[cur_color].append(col)
                    break

        if colors:
            color = colors.pop(0)
            request = Request(url="http://www.madeleine.de%s?cf=%s" % (item["path"], color[1]) , callback=self.find_colors)
            request.meta['item'] = item
            request.meta['colors_groups'] = colors_groups
            request.meta['cur_color'] = color[0]
            request.meta['colors'] = colors
            return request
        else:
            item["colors"] = self.make_colors(colors_groups)
            self.check_item(item)
            return item

    def make_colors(self, colors_groups):
        result = ""

        for group in colors_groups.keys():
            if group == "varies":
                continue

            if not colors_groups[group]:
                continue

            #if group == "varies_res" and colors_groups['varies_res']:
            #    result = result + "::"
            #else:
            result = result + "%s::" % group

            for color in colors_groups[group]:
                result = result + "%s:%s:%s," % (color[1], color[0], color[2])
            result = result[:-1] + ";"

        return result[:-1]

    def check_item(self, item):
        for i, key in enumerate(item.keys()):
            if item.get(key) != None:
                if item[key]:
                    self.check_values[i] = 1

    def result_check(self):
        result = True
        for v in self.check_values:
            if v == 0:
                result = False
        return result





