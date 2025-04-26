from tests.utils.locators import Locators
class SortableListPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://qaplayground.dev/apps/sortable-list/"
        self.locators  = Locators(self.page)
        self.color_green_rgb ="rgb(58, 227, 116)"
        self.color_green_rgba = "rgba(58, 227, 116, 1)"
        self.top_list = [ 
            {"position": 1, "name": "Jeff Bezos"},
            {"position": 2, "name": "Bill Gates"},
            {"position": 3, "name": "Warren Buffett"},
            {"position": 4, "name": "Bernard Arnault"},
            {"position": 5, "name": "Carlos Slim Helu"},
            {"position": 6, "name": "Amancio Ortega"},
            {"position": 7, "name": "Larry Ellison"},
            {"position": 8, "name": "Mark Zuckerberg"},
            {"position": 9, "name": "Michael Bloomberg"},
        ]
        self.person_names = lambda: self.locators.by_class_Name(".person-name")
        self.title = lambda: self.locators.by_xpath("//h1[contains(text(), '10 Richest People')]")
        
    def get_top_list(self):
        return self.top_list 
    
    def get_person_names(self):
        return self.person_names()
    def get_title(self):
        return self.title()
    def visit_url(self):
        self.page.get(self.url)

    